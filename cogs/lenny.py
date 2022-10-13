import discord
from discord.ext import commands
import random

class Lenny(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def lenny(self, ctx,lenny_choice=None):
    if lenny_choice == None:
      lenny_choice = random.randint(1,20)

    if lenny_choice == 1:
      await ctx.channel.send("( ͡° ͜ʖ ͡°)")
    elif lenny_choice == 2:
      await ctx.channel.send("( ͠° ͟ʖ ͡°)")
    elif lenny_choice == 3:
      await ctx.channel.send("( ͡~ ͜ʖ ͡°)")
    elif lenny_choice == 4:
      await ctx.channel.send("( ͡ʘ ͜ʖ ͡ʘ)")
    elif lenny_choice == 5:
      await ctx.channel.send("( ͡o ͜ʖ ͡o)")
    elif lenny_choice == 6:
      await ctx.channel.send("(° ͜ʖ °)")
    elif lenny_choice == 7:
      await ctx.channel.send("( ‾ʖ̫‾)")
    elif lenny_choice == 8:
      await ctx.channel.send("(ง ͠° ͟ل͜ ͡°)ง")
    if lenny_choice == 9:
      await ctx.channel.send("( ✧≖ ͜ʖ≖)")
    elif lenny_choice == 10:
      await ctx.channel.send("(▀̿Ĺ̯▀̿ ̿)")
    elif lenny_choice == 11:
      await ctx.channel.send("༼  ͡° ͜ʖ ͡° ༽")
    elif lenny_choice == 12:
      await ctx.channel.send("( ͡ಥ ͜ʖ ͡ಥ)")
    elif lenny_choice == 13:
      await ctx.channel.send("( ͡° ʖ̯ ͡°)")
    elif lenny_choice == 14:
      await ctx.channel.send("( ಠ ͜ʖಠ)")
    elif lenny_choice == 15:
      await ctx.channel.send("(͡ ͡° ͜ つ ͡͡°) ")
    elif lenny_choice == 16:
      await ctx.channel.send("[̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅]")
    elif lenny_choice == 17:
      await ctx.channel.send("(✿❦ ͜ʖ ❦)")
    elif lenny_choice == 18:
      await ctx.channel.send("ᕦ( ͡° ͜ʖ ͡°)ᕤ")
    elif lenny_choice == 19:
      await ctx.channel.send("¯\_( ͡° ͜ʖ ͡°)_/¯")
    elif lenny_choice == 20:
      await ctx.channel.send("(╯ ͠° ͟ʖ ͡°)╯┻━┻")
    else:
      await ctx.send("Error!")
  
def setup(client):
  client.add_cog(Lenny(client))