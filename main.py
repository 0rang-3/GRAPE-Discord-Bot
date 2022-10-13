import discord
from keep_alive import keep_alive
from discord.ext.commands import has_permissions, CheckFailure
import bs4
from discord.utils import get
# Import the keep alive file
import keep_alive
import time
import os
import random
import asyncio

from discord.ext import commands, tasks
from discord.ext.tasks import loop







client = discord.Client()
client = commands.Bot('-')#Makes the bot prefix.
client.remove_command('help')#Removes buggy help command




currency = {}
bank = {}
bank_money = {}

#Notifies when bot is alive
@client.event
async def on_ready():
  await client.change_presence(activity=discord.Game('-help'))
  #await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.guilds)} servers!"))

  print('Connected to bot: {}'.format(client.user.name))
  print('Bot ID: {}'.format(client.user.id))



@client.command()
async def load(ctx, extension):
  print("hi")
  client.load_extension(f'cogs.{extension}')
@client.command()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')

keep_alive.keep_alive()
token = os.environ.get("DISCORD_TOKEN")
client.run(token)