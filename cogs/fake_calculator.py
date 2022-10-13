import discord
from discord.ext import commands

class Fake_Calculator(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def fake_addition(self, ctx, number1, operation, number2):
    number3 = int(number1+number2)
    await ctx.channel.send(number1+" + "+number2+" = "+str(number3))
  
def setup(client):
  client.add_cog(Fake_Calculator(client))