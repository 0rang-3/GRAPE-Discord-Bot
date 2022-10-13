import discord
from discord.ext import commands

class MCwiki(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def mcwiki(self, ctx):
    await ctx.channel.send("https://minecraft.gamepedia.com/Minecraft_Wiki")
  
def setup(client):
  client.add_cog(MCwiki(client))