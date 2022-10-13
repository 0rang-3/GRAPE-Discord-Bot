import discord
from discord.ext import commands
import random

class Giveaway(commands.Cog):
  
  def __init__(self, client):
    self.client = client
  
  @commands.command()
  @commands.has_permissions(administrator=True)
  async def giveaway(self, ctx, ctx_time=None, *, prize=None):
    if prize==None:
      await ctx.send("Incorrect Syntax! The correct one is: -giveaway <time s|m|h|d> <prize>")
      return
    
    def convert(time):
      pos = ["s","m","h","d"]

      time_dict = {"s" : 1, "m" : 60, "h" : 3600, "d": 3600*24}

      unit = time[-1]

      if unit not in pos:
        return -1
      try:
        val = int(time[:-1])
      except:
        return -2

      return val * time_dict[unit]


  
    await ctx.channel.purge(limit=1)

    time_convert = convert(ctx_time)
    if time_convert == -1:
      await ctx.send(f"You didn't answer with a proper unit. Use (s|m|h|d) next time!")
      return
    elif time_convert == -2:
      await ctx.send(f"The time just be an integer. Please enter an integer next time.")
      return
  

    embed = discord.Embed(title = "Giveaway!", description = f"{prize}", color = ctx.author.color)

    embed.add_field(name = "Hosted by:", value = ctx.author.mention)

    embed.set_footer(text = f"Ends {ctx_time} from now!")

    my_msg = await ctx.send(embed = embed)

    await my_msg.add_reaction("🎉")

    dm = await ctx.message.author.create_dm()
    await dm.send("Make sure you remember to type `-giveaway_winner "+str(my_msg.id)+" "+prize+"` after "+ctx_time+". I highly suggest setting up a calendar event or an alarm so that you don't forget.")

  @commands.command()
  async def giveaway_winner(self, ctx, msgid=None, *, prize=None):
    await ctx.channel.purge(limit=1)

    if prize == None:
      await ctx.send("Make sure you type the prize at the end. **Syntax:** -giveaway_winner <message_id> <prize>")
      await ctx.send("**Note:** The whole command is provided when you started the giveaway (_Pois0n DMed you). The message id is found in that message.")
      return

    message = await ctx.fetch_message(msgid)

    users = []
    for reaction in message.reactions:
      async for user in reaction.users():
        users.append(user)
    del users[0]
    winner = random.choice(users)

    await ctx.send(f"We have a winner! Congratulations {winner.mention}, you won the prize: "+prize+"!")

    dm = await winner.create_dm()
    await dm.send("Congratulations, you won a giveaway! You prize is: "+prize+"! The admins from "+str(ctx.guild.name)+" will contact you shortly so you can receive your prize!")
  
def setup(client):
  client.add_cog(Giveaway(client))