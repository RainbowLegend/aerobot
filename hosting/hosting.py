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

class Hosting:
    """Host commands"""

    default = {}

    def __init__(self, bot):
        db = dataIO.load_json("data/selftosroles/roles.json")
        self.bot = bot
        self.db = defaultdict(lambda: default.copy(), db)

    @commands.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "Administrator", "Game Night Moderator")
    async def togglehost(self, ctx):
        author = ctx.message.author
        localRoleAdmin = discord.Role(id='414196360321957888', server='288455332173316106')
        localRoleSeniorMod = discord.Role(id='414189641890267157', server='288455332173316106')
        localRoleMod = discord.Role(id='414196360321957888', server='288455332173316106')
        administrator = discord.Role(id='288457272663867392', server='288455332173316106')
        seniorModerator = discord.Role(id='288464565791096838', server='288455332173316106')
        moderator = discord.Role(id='288682024515141634', server='288455332173316106')

        # Checks to find which role in the hierarchy they need

        if moderator in author.roles:  #  If they are a Moderator...
            localRole = localRoleMod
        elif seniorModerator in author.roles: #  If they are a Senior Mod...
            localRole = localRoleSeniorMod
        elif administrator in author.roles:
            localRole = localRoleAdmin
        else:
            return

        if localRole in author.roles:  #  If the hosting role is in the author
            await self.bot.remove_roles(author, localRole)  # Remove the role
            await self.bot.say('Successfully removed the Hosting role.')
        else:  # If the hosting role not in the author
            await self.bot.add_roles(author, localRole)  # Add the role
            await self.bot.say('Successfully added the Hosting role.')

    @commands.command(pass_context=True)
    async def joingame(self, ctx, *, ign):
        author = "<@" + str(ctx.message.author.id) + ">"
        ign = str(ign)

        if str(ctx.message.channel.id) not in ['358331904233046016', '358660402462326784', '296069608216068098']:
            await self.bot.say("<#358331904233046016>")
            return
        else:
            pass

        await self.bot.send_message(self.bot.get_channel("407003125128495104"), author + " - **" + ign + "**")
        await self.bot.say(author + " **||** Your IGN has been sent to the host.")

    @commands.group(pass_context=True)
    async def host(self, ctx):
        """Notifications for games"""

    @host.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator", "Game Moderator",
                           "Game Night Moderator", "Temp Host", "Gamenight Host")
    async def gamemodes(self, ctx):
        """Vote for today's gamemodes"""

        toscd = discord.Server(id='288455332173316106')
        optinrole = discord.Role(id='379748801197637644', server='288455332173316106')

        classic = discord.Emoji(id='386748316894887938', server=toscd)
        rp = discord.Emoji(id='386742079252070401', server=toscd)
        custom = discord.Emoji(id='386742078975115265', server=toscd)
        eve = discord.Emoji(id='386742078912069633', server=toscd)
        rm = discord.Emoji(id='386748316886499328', server=toscd)
        aa = discord.Emoji(id='386742078421467159', server=toscd)
        rain = discord.Emoji(id='386742078845222937', server=toscd)
        vigil = discord.Emoji(id='386742078471667714', server=toscd)

        await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                 colour=discord.Colour(0x880999), mentionable=True)

        msg = await self.bot.say("""<a:animpartyblob1:401122373236948993> <a:animpartyblob2:401122373367234570> <a:animpartyblob3:401122373396463616> <a:animpartyblob4:401122373262376971> <a:animpartyblob5:401122373425823744> <a:animpartyblob6:401122373614567434> <a:animpartyblob7:401122373698322432> <a:animpartyblob8:401122373270503427> <a:animpartyblob9:401122373434343431>
<@&379748801197637644> **||** We're voting for today's gamemodes! React to a gamemode to react.
You may choose more than 1.

**You may choose from these options:**
<:NormalClassic:386748316894887938> - Classic.
<:NormalRankedPractice:386742079252070401> - Ranked Practice.
<:CustomCustom:386742078975115265> - Custom.
<:CustomEvilsvEvils:386742078912069633> - Evils v Evils.
<:CustomRapidMode:386748316886499328> - Rapid Mode.
<:ChaosAllAny:386742078421467159> - All Any.
<:ChaosRainbow:386742078845222937>- Rainbow.
<:ChaosVigilantics:386742078471667714> - Vigilantics.""")
        
        await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                 colour=discord.Colour(0x880999), mentionable=False)

        await self.bot.add_reaction(msg, classic)
        await self.bot.add_reaction(msg, rp)
        await self.bot.add_reaction(msg, custom)
        await self.bot.add_reaction(msg, eve)
        await self.bot.add_reaction(msg, rm)
        await self.bot.add_reaction(msg, aa)
        await self.bot.add_reaction(msg, rain)
        await self.bot.add_reaction(msg, vigil)
    
    @host.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator", "Game Moderator",
                           "Game Night Moderator", "Temp Host", "Gamenight Host")
    async def start(self, ctx, *, gamemode):
        """Notify a game is starting"""

        channel = ctx.message.channel
        channelid = str(channel.id)
        authorid = str(ctx.message.author.id)

        toscd = discord.Server(id='288455332173316106')
        optinrole = discord.Role(id='379748801197637644', server='288455332173316106')

        if gamemode is None:
            gamemode = "Not defined"

        gamemode = str(gamemode)
        auth = str(ctx.message.author.id)

        await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                 colour=discord.Colour(0x880999), mentionable=True)

        await self.bot.say("""<@&379748801197637644> **||** A new game of **""" + gamemode + """** is starting.


Use `/joingame [Town of Salem IGN]` or `/jg [ToS IGN]` to join. You will shortly after get a party invite.""")

        await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                 colour=discord.Colour(0x880999), mentionable=False)

        await self.bot.send_message(self.bot.get_channel('407003125128495104'), "Names for the game of **" + str(gamemode) + "** are being posted below.")

    @host.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator", "Game Moderator",
                           "Game Night Moderator", "Temp Host", "Gamenight Host")
    async def final(self, ctx, *, gamemode):
        """Notify a game is starting"""

        toscd = discord.Server(id='288455332173316106')
        optinrole = discord.Role(id='379748801197637644', server='288455332173316106')

        if gamemode is None:
            gamemode = "Not defined"

        gamemode = str(gamemode)
        auth = str(ctx.message.author.id)

        await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                 colour=discord.Colour(0x880999), mentionable=True)

        await self.bot.say("""<@&379748801197637644> **||** This is the final call for a game of **""" + gamemode + """** is starting.
The game will start shortly.

Use `/joingame [Town of Salem IGN]` or `/jg [ToS IGN]` to join. You will shortly after get a party invite.""")
        
        await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                 colour=discord.Colour(0x880999), mentionable=False)


def check_folders():
    if not os.path.exists("data/selftosroles"):
        print("Creating data/selftosroles folder...")
        os.makedirs("data/selftosroles")


def check_files():
    if not dataIO.is_valid_json("data/hosting/selftosroles/roles.json"):
        print("Creating emptydata/hosting/selftosroles/roles.json...")
        dataIO.save_json("data/hosting/selftosroles/roles.json", {})


def setup(bot):
    n = Hosting(bot)
    bot.add_cog(n)     
