import discord
from discord.ext import commands

class Rocket_League(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def rocket_league(self, ctx, args=None):
    if args == None:
      await ctx.channel.send("Rocket League is a vehicular soccer video game developed and published by Psyonix. The game was first released for Microsoft Windows and PlayStation 4 in July 2015, with ports for Xbox One and Nintendo Switch being released later on, and a graphics update for Xbox Series X/S in 2020.")
    elif args == "wiki":
      await ctx.channel.send("https://rocketleague.fandom.com/wiki/Rocket_League_Wiki")
    elif args == "cars":
      await ctx.channel.send("https://rocketleague.fandom.com/wiki/Vehicle")
    elif args == "shop":
      await ctx.channel.send("Find the latest item shop on https://rocket-league.com/items/shop")
  
def setup(client):
  client.add_cog(Rocket_League(client))