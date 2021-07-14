import discord
from discord.ext import commands
import os

from bot_commands import dice_cmd
from bot_commands import filetype_cmd
from bot_commands import ctf_cmd


# ===== Bot setup/startup =====
client = commands.Bot(command_prefix="%")
@client.event
async def on_ready():
    print("Bot is now ready.")
# ===== =====


# ===== Commands =====
@client.command(name="dice")
async def dice(ctx):
    dice_result = dice_cmd.roll_dice()
    await ctx.send(f"You rolled a {dice_result}.")

# -----

@client.command(name="filetype")
async def filetype(ctx, filetype_user_input):
    response = filetype_cmd.display_file_information(filetype_user_input)
    await ctx.send(response)

# -----

@client.command(name="ctf")
async def ctf(ctx, celsius_number):
    response = ctf_cmd.convert_celsius_to_fahrenheit(celsius_number)
    await ctx.send(response)

# ===== =====


client.run(os.environ["BOT_TOKEN_HOST"])