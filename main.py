import discord
from discord.ext import commands
import os

from bot_commands import dice_cmd
from bot_commands import filetype_cmd
from bot_commands import ctf_cmd
from bot_commands import ftc_cmd
from bot_commands import covid_cmd
from bot_commands import convert_cmd


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

# -----

@client.command(name="ftc")
async def ftc(ctx, fahrenheit_number):
    response = ftc_cmd.convert_fahrenheit_to_celsius(fahrenheit_number)
    await ctx.send(response)

# -----

@client.command(name="covid")
async def covid(ctx, country_name):
    try:
        returned_country_name, cases, deaths, recoveries, fatality_percent, last_updated = covid_cmd.webscrape_coronavirus_data(country_name)

        embed = discord.Embed(title="Coronavirus Statistics for " + returned_country_name,
                              description="Global Graph: https://www.worldometers.info/coronavirus/",
                              color=discord.Color.blue()
                              )

        embed.add_field(name="Cases:", value=cases, inline=True)            # Discord.py embed formatting
        embed.add_field(name="Deaths:", value=deaths, inline=True)
        embed.add_field(name="Recoveries:", value=recoveries, inline=True)
        embed.add_field(name="Fatality:", value=fatality_percent, inline=True)
        embed.add_field(name="Last Updated:", value=last_updated, inline=True)

        await ctx.send(embed=embed)
    except:
        await ctx.send("```Error. Example of proper usage:\n\n%covid canada```")

# -----

@client.command(name="convert")
async def convert(ctx, amount_of_dollars, current_currency, desired_currency):
    response = convert_cmd.convert_to_currency(amount_of_dollars, current_currency, desired_currency)
    await ctx.send(response)

# ===== =====


client.run(os.environ["BOT_TOKEN_HOST"])