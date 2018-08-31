import discord
from discord.ext import commands
import datetime, re
import json, asyncio
import copy
import logging
import traceback
import aiohttp
import sys
import json

with open("config.json") as dataf:
    returnconfig = json.load(dataf)

def get_prefix(bot, message):

    prefixes = ['<']

    if not message.guild:
        return '?'

    return commands.when_mentioned_or(*prefixes)(bot, message)


initial_extensions = ['cogs.simple']

 # lets configure that Bot prefix, if you want to change this, go ahead! Do note that documentations might not work properly if you do.
bot = commands.Bot(command_prefix=get_prefix, description='A cool bot made with <3 by Tristan Farkas')

# Load in those cogs.
if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f'Kanelbulle couldn not load: {extension}.', file=sys.stderr)
            traceback.print_exc()

@bot.event
async def on_ready():
    print(bot.user.name)
    print('Signed into bot user.')

  # All of the following commands are currently MANDATORY, these commands are part of the MAIN system other commands are added using a seperate file.



# @bot.command()
# async def info(ctx):
#    embed = discord.Embed(title="Kanelbulle", description="Made with <3 by Tristan Farkas.", color=0xeee657)
#    embed.add_field(name="Author", value="@tristanfarkas#0001")
#    embed.add_field(name="Github repository", value="https://github.com/trilleplay/kanelbulle/")
#    embed.add_field(name="Server count", value=f"{len(bot.guilds)}")
#    embed.add_field(name="Invite", value="Right now Kanelbulle is private due to resource limitations. If you would like to apply/request access, you may do so over at my discord server: https://discord.gg/FBMrcYM in the #invite-kanelbulle channel. ")

#    await ctx.send(embed=embed)

bot.remove_command('help')

@bot.command()
async def help(ctx):
    embed = discord.Embed(title="Kanelbulle", description="Made with <3 by Tristan Farkas.", color=0xedab49)

    embed.add_field(name="<add X Y", value="Gives the addition of **X** and **Y**", inline=False)
    embed.add_field(name="<multiply X Y", value="Gives the multiplication of **X** and **Y**", inline=False)
    embed.add_field(name="<info", value="Gives some helpful stats about Kanelbulle.", inline=False)
    embed.add_field(name="<help", value="Prints out information/docs on how to use Kanelbulle.", inline=False)

    await ctx.send(embed=embed)

bot.run(returnconfig['token'])