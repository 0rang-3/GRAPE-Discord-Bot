import discord
from discord.ext import commands
import time

class Ping(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command(pass_context=True)
  async def ping(self, ctx):
    message = await ctx.channel.send("Pong")
    before = time.monotonic()
    await message.edit(content="Pong!")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f"Pong! `{int(ping)}ms`")
  
def setup(client):
  client.add_cog(Ping(client))