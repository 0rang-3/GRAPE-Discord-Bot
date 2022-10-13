import discord
from discord.ext import commands

class Profile(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def profile(self, ctx, member : discord.Member=None):
    if member == None:
      member = ctx.message.author
    icon = member.avatar_url
    embed = discord.Embed(title=str(member)+"'s Profile Picture", description="")
    embed.set_image(url=icon)
    await ctx.send(embed=embed)
  
def setup(client):
  client.add_cog(Profile(client))