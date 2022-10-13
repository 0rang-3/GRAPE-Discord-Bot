import discord
from discord.ext import commands
from discord.utils import get

class ServerInfo(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def serverinfo(self, ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    if name == "Game Lodge":
      owner = "Octorok#5020"
    else:
      owner = str(ctx.guild.owner)
  
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)


    if description == "None":
      embed = discord.Embed(
        title=name + "Server Information",
        description="",
        color=discord.Color.blue()
      )
    else:
      embed = discord.Embed(
        title=name + " Server Information",
        description=description,
        color=discord.Color.blue()
      )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    await ctx.send(embed=embed)

def setup(client):
  client.add_cog(ServerInfo(client))