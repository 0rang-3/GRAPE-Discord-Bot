import discord
from discord.ext import commands

class Spam_DM(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  async def spam_dm(self, ctx, member: discord.Member, amount, *, spam):
    await ctx.channel.purge(limit=1)
    author = ctx.message.author
    channel_author = await author.create_dm()
    await channel_author.send('Done! ✅')
    channel = await member.create_dm()
    for x in range(int(amount)):
      await channel.send(spam)
  
def setup(client):
  client.add_cog(Spam_DM(client))