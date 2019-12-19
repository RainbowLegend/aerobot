import discord
from discord.ext import commands

class Voice(commands.Cog):

  def __init__(self, bot):
    self.bot = bot
    self.voice_roles = { # voice roles mapped by their channel
      "Voice Channel 1": "Voice Chatter 1",
      "Voice Channel 2": "Voice Chatter 2"
    }
    
  @commands.Cog.listener()
  async def on_voice_state_update(self, member, before, after):
    channel = before.channel | after.channel
    
    if channel.name in self.voice_roles:
      r_name = self.voice_roles[channel.name] # Get the role name
      role = None
      
      try:
        role = [r for r in member.guild.roles if r.name == r_name][0]
      except: # list index out of range error
        print(r_name+" is not a registered role in "+ member.guild.name)
      
      try:
        if after.channel and role:
          await member.add_roles(role)
        elif role:
          await member.remove_roles(role)
      except:
        print("Bot does not have manage roles permissions")
          
def setup(bot):
  bot.add_cog(Voice(bot));
