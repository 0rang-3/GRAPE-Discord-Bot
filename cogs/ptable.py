import discord
from discord.ext import commands

class PTable(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def ptable(self, ctx):
    await ctx.channel.send("https://static.wikia.nocookie.net/minecraft_gamepedia/images/1/19/Block_overview.png/revision/latest/scale-to-width-down/460?cb=20200821110146")
  
def setup(client):
  client.add_cog(PTable(client))