import discord
from discord.ext import commands
import os

from bot_commands import dice_cmd


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


client.run(os.environ["BOT_TOKEN_HOST"])