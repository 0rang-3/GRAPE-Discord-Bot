import discord
from discord.ext import commands

class Version(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def version(self, ctx, args=None):
    if args == None:
      await ctx.channel.send("This bot is on: Grape 1.5 - The Clean Update. **Try:** `-version 1.5`")
    if args == "1.5":
      embed = discord.Embed(title="1.5 New Features - the Clean Update", description="A list of ALL the Grape 1.5 Features", color=0xfcba03)
      embed.add_field(name="Features:", value="Removed AFK Command, Removed Currency Features, Removed Calculator, Allows Anyone to Use Giveaway Command (See Patch Notes 390, Reason: Orange SMP)")
      await ctx.send(embed=embed)
    if args == "1.4":
      embed = discord.Embed(title="1.4 Features - the Currrency Update", description="A list of ALL the Grape 1.4 Features", color=0xfcba03)
      embed.add_field(name="Features:", value="Register (registers a Grape Coins Accout for you), Balance (checks for Grape Coins Balance), Fish, Hunt, Rob, Work, Buy, Shop, Use (an item)")
      await ctx.send(embed=embed)
    if args == "1.3" or args == "rocket_league" or args == "rl":
      embed = discord.Embed(title="1.3 Features - the Rocket League Update", description="A list of ALL the Grape 1.3 Features", color=0xfcba03)
      embed.add_field(name="Features:", value="Rocket League Command (Description, Wiki, Cars, Item Shop)")
      await ctx.send(embed=embed)
    if args == "1.2" or args == "afk":
      embed = discord.Embed(title="1.2 Features - The AFK Update", description="A list of ALL the Grape 1.2 Features", color=0xfcba03)
      embed.add_field(name="Features:", value="AFK Feature (Renames you to [your name] AFK for a selected amount of minutes), Mute and Unmute in a Voice Channel, Search YouTube, Timer, Say Command (Repeats what you say), Invite (Add Pois0n to your own server), Server Info (for Admins), Profile (sends a picture of a user's profile picture), Calculator.")
      embed.set_footer(text="Released on February 3, 2021")
      await ctx.send(embed=embed)
    if args == "1.1" or args == "minecraft" or args == "mc":
      embed = discord.Embed(title="1.1 Features - The Minecraft Update", description="A list of ALL the Grape 1.1 Features", color=0xfcba03)
      embed.add_field(name="Features:", value="Periodic Table of Blocks in Minecraft and Minecraft Search (searches the Minecraft wiki for the value specified).")
      embed.set_footer(text="Released on December 28, 2021")
      await ctx.send(embed=embed)
    if args == "1.0" or args == "original":
      await ctx.channel.send("Grape actually started off as two bots - Gaming Bot (which is now Grape) and Iron Golem. Gaming Bot had two features (the Kick and Ban Feature) and Iron Golem had one feature (to send you the link of the Minecraft Wiki). These two bots (both make from the same person, _Ven0m#4019) merged into one bot (_Ven0m decided to do this). The 1.0 Update added no new features, but only merged the two bots.")
  
def setup(client):
  client.add_cog(Version(client))