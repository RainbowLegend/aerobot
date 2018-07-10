import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify
from copy import deepcopy
from collections import defaultdict
import asyncio
import logging
import logging.handlers
import random
import os
import datetime
import re
from datetime import datetime

class RuleLoader:
    """Loads up the #info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def rulesembed(self, ctx):
      """Rule loading embed"""
      
      # Code in here
        salem = 'https://cdn.discordapp.com/attachments/358673822100226049/466346883477143552/salem.jpg'
        embed = discord.Embed(colour=0x27AE60)
        embed.set_author(name='Section 1: Server Rules)', icon_url=salem)
        embed.add_field(name='This is an English Speaking Server.',
                        value='Users may speak in languages other than English only if using a non-English word here and there. Otherwise, please speak only English.',inline=False)
        embed.add_field(name='Do not harass other users.',
                        value='This is effective both within the server and in places including, but not limited to, DMs, other servers, and in-game.',inline=False)
        embed.add_field(name='Do not spam.',
                        value='5 messages in a Rapid Succesion will result in a mute. One lining and spam are two different things, though.',inline=False)
        embed.add_field(name='Do not use overly offensive language.',
                        value='This includes, but is not limited to, racist and discriminatory remarks, over use of swearing, and harsh remarks directed at individuals.',inline=False)
        embed.add_field(name='Do not post suspicious links or links with malicious intent.',
                        value='This includes, but is not limited to viruses, IP Trackers, or Pornographic Images not in nsfw.',inline=False)
        embed.add_field(name='Do not advertise.',
                        value='This includes, but is not limited to any other discord server, reference for personal gain, or your own channel. Please ask a mod if you would like to post.',inline=False)
        embed.add_field(name='Keep all channels on topic.',
                        value="""Each channel has a reason. You will be punished if you don't use them accordingly:
                        
-<#290849989683445761> Is for general town of salem discussion.
-<#288677153334231040> Is for finding matches and sharing in game names.
-<#304800218908590090> Is for trial-reports and using the Trial Bot Commands.
-<#304799721464004609> Is for sharing stories about your Town of Salem experience, good or bad.
-<#304799816813379585> Is for sharing and finding strategies from other members.
-<#288455332173316106> Is where new players will be welcomed.
-<#425124003838033920> Is where all Not Safe For Work Content will go.
-<#294178185711452180> Is for random talk. Other games, memes, art, pets, anything. Just no nsfw.
-<#292018256888463360> Suggestions to make the server better.
-<#288463362357067777> Are for bot commands.""",inline=False)
        embed.add_field(name='Do not abuse Staff Tags.',
                        value='This includes, but is not limited to, phantom tagging, spamming staff tags, and tagging for unnecessary reasons.',inline=False)
        embed.add_field(name='
                        
      # End code here
      
def setup(bot):
    bot.add_cog(RuleLoader(bot))
