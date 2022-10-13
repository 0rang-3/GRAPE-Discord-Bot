import discord
from discord.ext import commands
import random

class Help(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def help(self, ctx, args=None, args2=None):
    print("hi")
    if args == None and args2 == None:
      embed = discord.Embed(title="Help Menu", description="The different commands are in Categories. And... **look out for SECRET commands!** **Syntax:** -help <category> (**Note:** The bot prefix is -)", color=0xFFFFF)#Declaring the help command is an embed.
      embed.add_field(name="Minecraft", value="Gives you the help menu for Minecraft Based Commands. ")
      embed.add_field(name="Rocket League", value="Gives your the help menu for Rocket League Based Commands.")
      embed.add_field(name="Admin", value="Commands for Admins.")
      embed.add_field(name="Timers", value="A list of timers in this bot")
      embed.add_field(name="Currency", value="All the Currency Commands are listed here")
      embed.add_field(name="Other", value="A bunch of random (and useless somewhat 😜)  commands.")
      embed.set_image(url= "https://antmaps.org/?mode=species&species=Solenopsis.invicta")
      embed.set_footer(text="Made by _Ven0m#4019")
      await ctx.send(embed=embed)#sends the embed.
      return

    #Minecraft Based Commands
    if args == "minecraft":
      embed = discord.Embed(title="Minecraft", description="This is the Minecraft Help Menu", color=0xFFFFF)#Declaring the help command is an embed.
      embed.add_field(name="Table of Blocks", value="Posts a picture of the Minecraft blocks. **Syntax:** -ptable")
      embed.add_field(name="Minecraft Wiki", value="Gives you the link to the Minecraft Wiki. **Syntax:** -mcwiki")
      
      embed.set_image(url= "https://antmaps.org/?mode=species&species=Solenopsis.invicta")
      embed.set_footer(text="Made by _Ven0m#4019")
      await ctx.send(embed=embed)
      return

    #Rocket League Based Commands
    if args == "rocket" and args2 == "league":
      embed = discord.Embed(title="Rocket League", description="This is the Rocket League Help Menu.", color=0xFFFFF)#Declaring the help command is an embed.
      embed.add_field(name="Rocket League Wiki", value="Gives you the link to the Rocket League Wiki. **Syntax:** -rocket_league wiki")
      embed.add_field(name="Rocket League Cars", value="Gives you the link to the Rocket League Wiki Vehicle Section. **Syntax:** -rocket_league cars")
      embed.add_field(name="Rocket League Item Shop", value="Sends you what is currently on the Item Shop in Rocket League. **Syntax:** -rocket_league shop")
      
      embed.set_footer(text="Made by _Ven0m#4019")
      await ctx.send(embed=embed)
      return

    #Admin Commands
    if args == "admin":
      embed = discord.Embed(title="Admin Menu", description="This is the Admin Help Menu.", color=0xFFFFF)
      embed.add_field(name="Kick", value="The kick command kicks the specified user. You need have the Admin role to use this command. Also, this bot needs to have the Adminstrator permission to do this command. **Syntax:** -kick @<user>")
      embed.add_field(name="Ban", value="The ban command bans the specified user. You need to have the Admin role to use this command. Also, this bot needs to have the Adminstrator permission to do this command. **Syntax:** -ban @<user>")
      embed.add_field(name="Server Info", value="gives you infomation about the server. **Syntax:** -serverinfo")
      embed.add_field(name="Mute", value="The mute command mutes the specified user when they are in a voice channel. **Syntax:** -mute @<user>")
      embed.add_field(name="Unmute", value="The unmute command unmutes the specified user when they are in a voice channel. **Syntax:** -unmute @<user>")
      embed.add_field(name="Clear", value="Clears messages in a channel. **Syntax:** -clear <amount of messages>. Or -clear all to clear all the messages in a channel.")
      
      embed.set_image(url= "https://antmaps.org/?mode=species&species=Solenopsis.invicta")
      embed.set_footer(text="Made by _Ven0m#4019")
      await ctx.send(embed=embed)
      return
  
    #Timers
    if args == "timers" or args == "timer":
      embed = discord.Embed(title="Timers Menu", description="This is the Timers Help Menu", color=0xFFFFF)
      embed.add_field(name="Timer Seconds", value="Times the specified number of seconds. **Syntax:** -timer_seconds <number of seconds>")
      embed.add_field(name="Timer Minutes", value="Timers the specified number of minutes. **Syntax:** -timer_minutes <number of minutes>")

      embed.set_footer(text="Made by _Ven0m#4019")
      await ctx.send(embed=embed)
      return
  
    
    #Other
    if args == "other":
      embed = discord.Embed(title="Other Commands Menu", description="This is the Other Commands Help Menu.", color=0xFFFFF)
      embed.add_field(name="Version", value="Tells you the version of this bot. **Syntax:** -version")
      embed.add_field(name="Giveaway", value="A very easy way to do giveaways in your server. **Syntax:** -giveaway <time s|m|h|d> <prize>")
      embed.add_field(name="Profile", value="Send you a user's profile picture. **Syntax:** -profile @<user>")
      embed.add_field(name="Say", value="Says what you want. **Syntax:** -say <what to say>")
      embed.add_field(name="Ping", value="Checks the latency of the bot. **Syntax:** -ping")

      embed.set_image(url= "https://antmaps.org/?mode=species&species=Solenopsis.invicta")
      embed.set_footer(text="Made by _Ven0m#4019")
      await ctx.send(embed=embed)
      return

    #ERROR SCREEN
    else:
      embed = discord.Embed(title="Error!", description="Oh no!", color=0xdb0404)
      error_code = random.randint(10010, 51091)
      try_example_random = random.randint(0, 5)
      if try_example_random == 0:
        try_example = "minecraft"
      if try_example_random == 1:
        try_example = "rocket league"
      if try_example_random == 2:
        try_example = "admin"
      if try_example_random == 3:
        try_example = "timers"
      if try_example_random == 4:
        try_example = "other"
      if try_example_random == 4:
        try_example = "currency"
      embed.add_field(name="**Try:** -help "+try_example, value="When typing the category, use all lowercase characters.")
      embed.set_footer(text="Made by _Ven0m#4019, Error Code: "+str(error_code))
      await ctx.send(embed=embed)
  
def setup(client):
  client.add_cog(Help(client))