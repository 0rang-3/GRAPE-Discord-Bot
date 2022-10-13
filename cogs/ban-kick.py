import discord
from discord.ext import commands

class Ban_Kick(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_permissions(ban_members=True)
  async def ban(self, ctx, member : discord.Member, *, reason=None):
    channel_dm = await member.create_dm()
    name = str(ctx.guild.name)
    if reason == None:
      await channel_dm.send("You were banned from "+name+".")
      await ctx.channel.send(f"{member.mention} was banned.")
      await member.ban(reason=reason)
    else:
      await channel_dm.send("You were banned from "+name+" "+str(reason)+".")
      await ctx.channel.send(f"{member.mention} was banned "+str(reason)+".")
      await member.ban(reason=reason)

  @commands.command()
  @commands.has_permissions(kick_members=True)
  async def kick(self, ctx, member : discord.Member, *, reason=None):
    channel_dm = await member.create_dm()
    name = str(ctx.guild.name)
    if reason == None:
      await channel_dm.send("You were kicked from "+name+".")
      await ctx.channel.send(f"{member.mention} was kicked.")
      await member.kick(reason=reason)
    else:
      await channel_dm.send("You were kicked from "+name+" "+str(reason)+".")
      await ctx.channel.send(f"{member.mention} was kicked "+str(reason)+".")
      await member.kick(reason=reason)
  
def setup(client):
  client.add_cog(Ban_Kick(client))