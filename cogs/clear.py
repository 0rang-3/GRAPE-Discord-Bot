import discord
from discord.ext import commands

class Clear(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_permissions(manage_messages=True)
  async def clear(self, ctx, amount):
    if amount == "all":
      await ctx.channel.purge(limit=None)
    else:
      amount2 = int(amount) + 1
      await ctx.channel.purge(limit = int(amount2))
  
def setup(client):
  client.add_cog(Clear(client))