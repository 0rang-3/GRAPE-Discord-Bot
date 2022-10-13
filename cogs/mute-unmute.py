import discord
from discord.ext import commands

class Mute_Unmute(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_permissions(mute_members=True)
  async def mute(self, ctx, member : discord.Member):
    await member.edit(mute = True)
    await ctx.send(f"{member.mention} is muted!")

  @commands.command()
  @commands.has_permissions(mute_members=True)
  async def unmute(ctx, member : discord.Member):
    await member.edit(mute = False)
    await ctx.send(f"{member.mention} is unmuted!")
  
def setup(client):
  client.add_cog(Mute_Unmute(client))