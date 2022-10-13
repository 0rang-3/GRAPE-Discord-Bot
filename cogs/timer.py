import discord
from discord.ext import commands
import time

class Timers(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  #Timer Seconds
  @commands.command()
  async def timer_seconds(self, ctx, amount_of_time):
    await ctx.channel.send("Time starts now!")
    if int(amount_of_time) > 5:
      amount_of_time_for_loop = int(amount_of_time) - 5
      for x in range(amount_of_time_for_loop):
        time.sleep(1)
      await ctx.channel.send("5")
      time.sleep(1)
      await ctx.channel.send("4")
      time.sleep(1)
      await ctx.channel.send("3")
      time.sleep(1)
      await ctx.channel.send("2")
      time.sleep(1)
      await ctx.channel.send("1")
      time.sleep(1)
      await ctx.channel.send(ctx.message.author.mention+" TIME UP!")
      return
    else:
      time.sleep(int(amount_of_time))
      await ctx.channel.send(ctx.message.author.mention+" TIME UP!")

    @commands.command()
    async def timer_minutes(self, ctx, amount_of_time):
      await ctx.channel.send("Time starts now!")
      if int(amount_of_time) > 5:
        amount_of_time_for_loop = int(amount_of_time) - 5
      for x in range(amount_of_time_for_loop):
        time.sleep(60)
        await ctx.channel.send("5 minutes left")
        time.sleep(60)
        await ctx.channel.send("4 minutes left")
        time.sleep(60)
        await ctx.channel.send("3 minutes left")
        time.sleep(60)
        await ctx.channel.send("2 minutes left")
        time.sleep(60)
        await ctx.channel.send("1 minute left")
        time.sleep(60)
        await ctx.channel.send(ctx.message.author.mention+" TIME UP!")
        return
      else:
        time.sleep(int(amount_of_time) * 60)
        await ctx.channel.send(ctx.message.author.mention+" TIME UP!")
  
def setup(client):
  client.add_cog(Timers(client))