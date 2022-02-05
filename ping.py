from discord import embeds
from discord.ext import commands
import discord
import asyncio
from discord.ext.commands.core import has_permissions
from discord.ext.commands import CommandNotFound
from discord.ext.commands.errors import CommandInvokeError, CommandOnCooldown, MissingPermissions, MissingRequiredArgument, CommandNotFound
from discord.ext import tasks


bot = commands.AutoShardedBot(command_prefix='!') ## CHANGE PREFIX
bot.remove_command('help')

token = "" ## CHANGE DISCORD TOKEN

DefaultColour = discord.Colour(0x0062ff)  ## DEFAULT
SuccessColour = discord.Colour(0x0ac200)  ## SUCCESS
ErrorColour = discord.Colour(0xff0000)    ## ERROR


##on ready event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    activity = discord.Game(name="PING!") 
    await bot.change_presence(status=discord.Status.online, activity=activity)

async def my_task(ctx):
    while True:
        await ctx.send(f"> @everyone PING!") ##CAN CHANGE DEFAULT MESSAGE
        await asyncio.sleep(1)
    

@bot.command()
@has_permissions(ban_members = True)
async def start(ctx):
    bot.loop.create_task(my_task(ctx))

bot.run(token) 