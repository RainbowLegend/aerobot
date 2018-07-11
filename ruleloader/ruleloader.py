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
       embed = discord.Embed(colour=0xFDAECB)
       embed.set_author(name='Section 1: Server Rules', icon_url=salem)
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
       embed.add_field(name='Do not use alts to avoid punishment.',
                         value='If you would like to protest a punishment, using an alt (alternate account) to evade it is not going to resolve anything. This will result in further punishment and usually a ban.',inline=False)
       embed.add_field(name='Please be courteous to everyone.',
                         value='While you do not need to like every member of this server, we would like to ask that you are courteous to all. Treat others how you would like to be treated. If you have any issues with other members, please DM a staff member with your concerns.',inline=False)
       embed.add_field(name='Do not share the personal information of others without consent.',
                         value='While you may be alright with sharing this info about yourself, others may not want it shared. Please be respectful of other users’ privacy.',inline=False)
       await self.bot.say(embed=embed)
        
         
     @commands.command(no_pm=True, pass_context=True)
     @commands.has_any_role("Administrator", "AeroBot Manager")
     async def rulesembed2(self, ctx):
       """Rule loading embed"""
       body = 'https://media.discordapp.net/attachments/294178185711452180/466383542520250378/body.png'
       embed = discord.Embed(colour=0xFF9900)
       embed.set_author(name='Section 2: Game Rules', icon_url=body)
       embed.add_field(name='All rules already present in Town of Salem apply to games in this server.',
                         value='This includes, but is not limited to, gamethrowing, spamming, or cheating.',inline=False)
       embed.add_field(name='Do not use this server to cheat.',
                         value='Whether in the text chat or either voice chat, this server will not be used to cheat in-game. This includes talking about ongoing games. Only info that is publicly known (for instance, the role of an uncleaned person in the graveyard) may be shared anywhere in the server during ongoing games. If you are unsure of what you can share, do not share it at all.', inline=False)
       embed.add_field(name='Do not intentionally leave or AFK While still alive during a game.',
                         value='While all cases will be investigated for legitimate reasons, any intentional breaks or leaving early will be punished.',inline=False)
       embed.add_field(name='Do not metagame.',
                         value='Metagaming can include, but is not limited to, asking for specific attributes, abilities, or win conditions.',inline=False)
       embed.add_field(name='Do not witch-hunt players based on who they are or names.',
                         value='This includes both targeting based on who the player actually is as well as targeting for failure to follow name schemes. If you have problems with players, please report them rather than target them in-game. Do not report them for not following a theme.',inline=False)
       embed.add_field(name='Do not flame, insult, or harass players for plays they make in-game.',
                         value='Please try and help other players improve rather than put them down for any mistakes. If these mistakes break rules, please contact a staff member rather than berate other players.',inline=False)
       await self.bot.say(embed=embed)
         
     @commands.command(no_pm=True, pass_context=True)
     @commands.has_any_role("Administrator", "AeroBot Manager")
     async def rulesembed3(self, ctx):
       """Rule loading embed"""        
       mic = 'https://media.discordapp.net/attachments/294178185711452180/466385729572831255/mic.png?width=398&height=398'
       embed = discord.Embed(colour=0xFBF606)
       embed.set_author(name='Section 3: Voice Chat and Music Rules', icon_url=mic)
       embed.add_field(name='All in-game cheating rules apply.',
                         value='If you can not do it in text channels, you can not do it in Voice Channels.', inline=False)
       embed.add_field(name='Do not remain AFK in VC for a long period of time',
                         value='If you remain defeaned for fifteen or more minutes, you will be moved to the Jailor’s Cell (AFK Voice Chat)', inline=False)
       embed.add_field(name='Keep all music to the music channel.',
                         value='There is a music channel for a reason. Keep all music to this channel, please.', inline=False)
       embed.add_field(name='Do not play songs specifically to annoy others.',
                         value='This includes, but is not limited to, playing very loud songs (i.e. “ear rape”), troll songs, meme songs, or playing songs on repeat multiple tlmes in a short amount of time.', inline=False)
       await self.bot.say(embed=embed)
         
     @commands.command(no_pm=True, pass_context=True)
     @commands.has_any_role("Administrator", "AeroBot Manager")
     async def rulesembed4(self, ctx):
       """Rule loading embed""" 
       gae = 'https://media.discordapp.net/attachments/288681936870703105/466390095151235072/Untitled.png?width=400&height=300'
       embed = discord.Embed(colour=0xE60042)
       embed.set_author(name='Section 4: Moderator/Senior Moderator Rules',icon_url=gae)
       embed.add_field(name='You have been trusted with Perms. Do not abuse them.',
                         value='This includes, but is not limited to, changing roles without consent, deleting messages that do not break rules, punishing people who do not rightfully deserve it, and so on. Use common sense for what is and is not okay.',inline=False)
       embed.add_field(name='Do not go pinning a ton of messages around the channels for no reason.',
                         value='If it is important for the channel, go ahead and pin it. A joke here and there? Go ahead and pin it. However, do not flood the pins with useless messages.',inline=False)
       embed.add_field(name='Treat EVERY member the same for punishments.',
                         value='You are here, first and foremost, to moderate the channels. Never change a punishment simply for who the person is.',inline=False)
       embed.add_field(name='Treat all of your fellow staff with respect.',
                         value='While you do not need to like all of the staff members, you need to be able to get along and treat others with respect for any staff work to work. Treat the others how you would like to be treated.',inline=False)
       embed.add_field(name='Senior Moderators.',
                         value='Just moderators that are more trusted and have more permissons.',inline=False)
       await self.bot.say(embed=embed)
         
     @commands.command(no_pm=True, pass_context=True)
     @commands.has_any_role("Administrator", "AeroBot Manager")
      async def rulesembed5(self, ctx):
        """Rule loading embed""" 
        icon = ctx.message.server.icon_url
        embed = discord.Embed(0x9B0029)
        embed.set_author(name='Section 5: Final Note', icon_url=icon, description="""**If you believe someone is breaching the rules, please contact staff either in a direct message or the channel it happened.**"""
        embed = discord.Embed(colour=0x9B0029, description="""**If you believe someone is breaching the rules, please contact staff either in a direct message or the channel it happened.**
        
        *If a staff member is in breach of their rules, please DM an Administrator.*""")
        embed.set_author(name='Section 5: Final Note', icon_url=icon)
        embed.set_footer(text='If you have any question about the rules, please feel free to DM a Staff Member.',icon_url=icon)
          
        await self.bot.say(embed=embed)
    # End code here
       
 def setup(bot):
     bot.add_cog(RuleLoader(bot))
