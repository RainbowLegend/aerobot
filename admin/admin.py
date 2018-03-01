import discord
from discord.ext import commands
from cogs.utils import checks
from cogs.utils.dataIO import dataIO
from cogs.utils.chat_formatting import box, pagify
from copy import deepcopy
import asyncio
import logging
import logging.handlers
import random
import os
import datetime
import re
from datetime import datetime


log = logging.getLogger("red.admin")


class Admin:
    """lol"""

    def __init__(self, bot):
        self.bot = bot
        self._announce_msg = None
        self._announce_server = None
        self._settings = dataIO.load_json('data/admin/settings.json')
        self._settable_roles = self._settings.get("ROLES", {})

    async def _confirm_invite(self, server, owner, ctx):
        answers = ("yes", "y")
        invite = await self.bot.create_invite(server)
        if ctx.message.channel.is_private:
            await self.bot.say(invite)
        else:
            await self.bot.say("Are you sure you want to post an invite to {} "
                               "here? (yes/no)".format(server.name))
            msg = await self.bot.wait_for_message(author=owner, timeout=15)
            if msg is None:
                await self.bot.say("I guess not.")
            elif msg.content.lower().strip() in answers:
                await self.bot.say(invite)
            else:
                await self.bot.say("Alright then.")

    def _get_selfrole_names(self, server):
        if server.id not in self._settable_roles:
            return None
        else:
            return self._settable_roles[server.id]

    def _is_server_locked(self):
        return self._settings.get("SERVER_LOCK", False)

    def _role_from_string(self, server, rolename, roles=None):
        if roles is None:
            roles = server.roles

        roles = [r for r in roles if r is not None]
        role = discord.utils.find(lambda r: r.name.lower() == rolename.lower(),
                                  roles)
        try:
            log.debug("Role {} found from rolename {}".format(
                role.name, rolename))
        except:
            log.debug("Role not found for rolename {}".format(rolename))
        return role

    def _save_settings(self):
        dataIO.save_json('data/admin/settings.json', self._settings)

    def _set_selfroles(self, server, rolelist):
        self._settable_roles[server.id] = rolelist
        self._settings["ROLES"] = self._settable_roles
        self._save_settings()

    def _set_serverlock(self, lock=True):
        self._settings["SERVER_LOCK"] = lock
        self._save_settings()

    

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator")
    async def addrole(self, ctx, rolename, user: discord.Member=None, *, reason: str):
        """Adds a role to a user."""
        auth = ctx.message.author
        channel = ctx.message.channel
        server = ctx.message.server
        afxuser = str(user)
        afximg = user.avatar_url
        authstr = str(auth)
        authimg = auth.avatar_url
        rolenamestr = str(rolename)
        secondaryrole = discord.Role(id='297159204181901323', server='288455332173316106')

        

        if user is None:
            user = author

        role = self._role_from_string(server, rolename)
        roleid = role.id
        roleidstr = str(roleid)
        afxuserid = user.id

        if role is None:
            await self.bot.say('That role cannot be found.')
            return

        if roleid in ['288457272663867392', '288682024515141634', '288464565791096838', '414196360321957888',
                      '414189641890267157', '414196208660119572']:
            await self.bot.say('What the fuck are you trying to do? Give a staff role to yourself? Shame on you.')
            return

        elif roleid in ['289508430350254080', '291743984525770754', '291743946642554883', '291743908306616323',
                        '291743280813703168', '291743388661841920', '291743325814521856', '291743168515538946',
                        '291743471750873088', '291743680241336321', '291743563711250442', '291743513182208000',
                        '291743627489574912', '291743828849852416', '291743751846494208', '321786146835267594',
                        '321785124230397952', '321785338987282432', '321785330439159818']:
            secondaryrole = discord.Role(id='297159204181901323', server='288455332173316106')
            secondaryrolestr = 'Town (ID: `297159204181901323`)'
            addedsecondrole = True

        elif roleid in ['289509219214950400', '291744083750158357', '291744254563319809', '291744342572269568',
                        '291744422213844992', '291744553919184897', '291744602090897408', '291744671292456960',
                        '291744520469610496', '321786150916194304', '321786146835267594']:
            secondaryrole = discord.Role(id='297159278303641600', server='288455332173316106')
            secondaryrolestr = 'Mafia (ID: `297159278303641600`)'
            addedsecondrole = True

        elif roleid in ['291744786275106817', '291745330574393344', '291745200328671243', '326914566263013386']:
            secondaryrole = discord.Role(id='297169993270034433', server='288455332173316106')
            secondaryrolestr = 'Neutral Killing (ID: `297169993270034433`)'
            addedsecondrole = True

        elif roleid in ['291745801107931142', '291745696707772417', '321785643812388864']:
            secondaryrole = discord.Role(id='297170017634746369', server='288455332173316106')
            secondaryrolestr = 'Neutral Benign (ID: `297170017634746369`)'
            addedsecondrole = True

        elif roleid in ['291745484681510922', '289509291306647552']:
            secondaryrole = discord.Role(id='297170044553789440', server='288455332173316106')
            secondaryrolestr = 'Neutral Evil (ID: `297170044553789440`)'
            addedsecondrole = True

        elif roleid in ['288682060414058516', '291746016418594827', '321785635956588544', '321786136974458921',
                        '326914120576270347']:
            secondaryrole = discord.Role(id='297170076002680840', server='288455332173316106')
            secondaryrolestr = 'Neutral Chaos (ID: `297170076002680840`)'
            addedsecondrole = True

        elif roleid in ['321784223608340480', '321784220240314370', '321784224866631690', '321784216075501569',
                        '321784193451556866','321784203127816193' ]:
            secondaryrole = discord.Role(id='291745541581307904', server='288455332173316106')
            secondaryrolestr = 'Coven (ID: `291745541581307904`)'
            addedsecondrole = True

        else:
            addedsecondrole = False

        if not channel.permissions_for(server.me).manage_roles:
            await self.bot.say('I don\'t have manage_roles.')
            return

        roleupdate = discord.Embed(description='Command successfully executed.', colour=0x66BB6A) #CHAT UPDATE ONLY.
        roleupdate.set_thumbnail(url=afximg)
        roleupdate.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-'
                                                                                     '9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkK'
                                                                                     'AvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        roleupdate.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        roleupdate.add_field(name='Affected Member:', value='<@' + afxuserid + '>', inline=True)
        roleupdate.add_field(name='Role added:', value=rolenamestr + ' (Role ID: `' + roleid + '`)', inline=True)
        roleupdate.add_field(name='Reason:', value=reason, inline=True)

        if addedsecondrole is True:
            roleupdate.add_field(name='Secondary role added:', value=secondaryrolestr)

        rulog = discord.Embed(description='Modlog Entry - `/addrole`', colour=0x66BB6A)
        rulog.set_thumbnail(url=afximg)
        rulog.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_'
                                                                                'c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR'
                                                                                '9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        rulog.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        rulog.add_field(name='Affected Member:', value='<@' + afxuserid + '>', inline=True)
        rulog.add_field(name='Role added:', value=rolenamestr + ' (Role ID: `' + roleid + '`)', inline=True)
        rulog.add_field(name='Reason:', value=reason, inline=True)
        if addedsecondrole is True:
            rulog.add_field(name='Secondary role added:', value=secondaryrolestr)

        await self.bot.add_roles(user, role)
        await self.bot.say(embed=roleupdate)
        await self.bot.send_message(self.bot.get_channel('288467626890362880'), embed=rulog)
        if addedsecondrole is True:
            await self.bot.add_roles(user, secondaryrole)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator")
    async def warn(self, ctx, user: discord.Member=None):
        """Adds the warned role to a user."""

        warned = discord.Role(id='290239154791383041', server='288455332173316106')
        channel = ctx.message.channel
        auth = ctx.message.author
        authstr = str(auth)
        authimg = auth.avatar_url
        server = ctx.message.server
        modname = ctx.message.author
        afxuser = str(user)
        afximg = user.avatar_url
        afxuserid = user.id
        
        
        if not channel.permissions_for(server.me).manage_roles:
            await self.bot.say('I don\'t have manage_roles.')
            return

        warnedupdate = discord.Embed(description='Command successfully executed.', colour=0x66BB6A) #CHAT UPDATE ONLY.
        warnedupdate.set_thumbnail(url=afximg)
        warnedupdate.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        warnedupdate.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        warnedupdate.add_field(name='Affected Member:', value='<@' + afxuserid + '>', inline=True)
        warnedupdate.add_field(name='Role added:', value='Warned (ID: `288455332173316106`)', inline=True)

        wulog = discord.Embed(description='Modlog Entry - `/warn`', colour=0x66BB6A) #modlog
        wulog.set_thumbnail(url=afximg)
        wulog.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        wulog.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        wulog.add_field(name='Affected Member:', value='<@' + afxuserid + '>', inline=True)
        wulog.add_field(name='Role added:', value='Warned (ID: `288455332173316106`)', inline=True)

        dmtobanned = discord.Embed(description='You have just warned on the server.', colour=0xE53935) #DM TO AFXUSER
        dmtobanned.set_thumbnail(url=afxuserurl)
        dmtobanned.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        dmtobanned.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        dmtobanned.add_field(name='Warned User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)
        dmtobanned.add_field(name='Reason:', value=reason)
        dmtobanned.add_field(name='Appeal using:', value='`/appeal warn [message]`')
        
        await self.bot.add_roles(user, warned)
        await self.bot.send_message(user, embed=dmtobanned)
        await self.bot.say(embed=warnedupdate)
        await self.bot.send_message(self.bot.get_channel('288467626890362880'), embed=wulog)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator")
    async def unwarn(self, ctx, user: discord.Member=None):
        """Removes the warned role to a user."""

        warned = discord.Role(id='290239154791383041', server='288455332173316106')
        channel = ctx.message.channel
        auth = ctx.message.author
        authstr = str(auth)
        authimg = auth.avatar_url
        server = ctx.message.server
        modname = ctx.message.author
        afxuser = str(user)
        afximg = user.avatar_url
        afxuserid = user.id
        
        if not channel.permissions_for(server.me).manage_roles:
            await self.bot.say('I don\'t have manage_roles.')
            return

        warnedupdate = discord.Embed(description='Command successfully executed.', colour=0xE53935) #CHAT UPDATE ONLY.
        warnedupdate.set_thumbnail(url=afximg)
        warnedupdate.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        warnedupdate.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        warnedupdate.add_field(name='Affected Member:', value='<@' + afxuserid + '>', inline=True)
        warnedupdate.add_field(name='Role removed:', value='Warned (ID: `288455332173316106`)', inline=True)

        wulog = discord.Embed(description='Modlog Entry - `/unwarn`', colour=0xE53935) #modlog
        wulog.set_thumbnail(url=afximg)
        wulog.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        wulog.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        wulog.add_field(name='Affected Member:', value='<@' + afxuserid + '>', inline=True)
        wulog.add_field(name='Role removed:', value='Warned (ID: `288455332173316106`)', inline=True)

        await self.bot.remove_roles(user, warned)
        await self.bot.say(embed=warnedupdate)
        await self.bot.send_message(self.bot.get_channel('288467626890362880'), embed=wulog)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator")
    async def aban(self, ctx, user: discord.Member, *, reason=None):
        """Bans a user. The bot will delete 1 days worth of messages."""

        author = ctx.message.author
        authstr = str(author)
        authimg = author.avatar_url
        server = author.server
        afxuser = str(user)
        afxuserurl = user.avatar_url
        afxuserid = user.id
        reasonstr = str(reason)
        afxidstr = str(afxuserid)
        senior = discord.Role(id='288464565791096838', server='288455332173316106')
        mod = discord.Role(id='288682024515141634', server='288455332173316106')
        admin = discord.Role(id='288457272663867392', server='288455332173316106')

        if mod in user.roles:
            await self.bot.say('lol hi look at this retard (<@' + author.id + '>) who tried to ban a staff')
            return
        if senior in user.roles:
            await self.bot.say('lol hi look at this retard (<@' + author.id + '>) who tried to ban a staff')
            return
        if admin in user.roles:
            await self.bot.say('lol hi look at this retard (<@' + author.id + '>) who tried to ban a staff')
            return

        banmessagechat = discord.Embed(description='Command successfully executed.', colour=0xE53935) #CHAT UPDATE
        banmessagechat.set_thumbnail(url=afxuserurl)
        banmessagechat.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        banmessagechat.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        banmessagechat.add_field(name='Banned User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)
        banmessagechat.add_field(name='Reason:', value=reason)

        banlog = discord.Embed(description='Modlog Entry - `/ban`', colour=0xE53935) #MODLOG
        banlog.set_thumbnail(url=afxuserurl)
        banlog.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        banlog.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        banlog.add_field(name='Banned User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)
        banlog.add_field(name='Reason:', value=reason)

        dmtobanned = discord.Embed(description='You have just banned from the server.', colour=0xE53935) #DM TO AFXUSER
        dmtobanned.set_thumbnail(url=afxuserurl)
        dmtobanned.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        dmtobanned.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        dmtobanned.add_field(name='Banned User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)
        dmtobanned.add_field(name='Reason:', value=reason)
        dmtobanned.add_field(name='Appeal using:', value='`/appeal ban [message]`')
        
        try:
            kickconfirmation = discord.Embed(description='Are you sure you want to ban <@' + afxidstr + '>? Type `yes` to confirm.', colour=0xE53935)
            await self.bot.say(embed=kickconfirmation)
            message = await self.bot.wait_for_message(timeout=5,
                                                      author=ctx.message.author)
            if not message:
                kickto = discord.Embed(description='I timed out after waiting too long.', colour=0xE53935)
                await self.bot.say(embed=kickto)
                return False

            elif message.clean_content.lower() != 'yes':
                kickcancel = discord.Embed(description='I guess not... command cancelled.', colour=0xE53935)
                await self.bot.say('I guess not... command cancelled.')
                return False

            await self.bot.send_message(user, embed=dmtobanned)
            await self.bot.ban(user, 1)
            await self.bot.say(embed=banmessagechat)
            await self.bot.send_message(self.bot.get_channel('288467626890362880'), embed=banlog)

        except discord.errors.Forbidden:
            await self.bot.say('`discord.errors.Forbidden` - I do not have permission to ban members, or the highest role of the target is higher than mine.')
            return

        except discord.errors.HTTPException:
            await self.bot.say('`discord.errors.HTTPException` - Banning the user failed.')
            return

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator")
    async def kick(self, ctx, user: discord.Member, *, reason=None):
        """Kicks a user."""

        author = ctx.message.author
        authstr = str(author)
        authimg = author.avatar_url
        server = author.server
        afxuser = str(user)
        afxuserurl = user.avatar_url
        afxuserid = user.id
        reasonstr = str(reason)
        afxidstr = str(afxuserid)
        senior = discord.Role(id='288464565791096838', server='288455332173316106')
        mod = discord.Role(id='288682024515141634', server='288455332173316106')
        admin = discord.Role(id='288457272663867392', server='288455332173316106')

        if mod in user.roles:
            await self.bot.say('lol hi look at this retard (<@' + author.id + '>) who tried to ban a staff')
            return
        if senior in user.roles:
            await self.bot.say('lol hi look at this retard (<@' + author.id + '>) who tried to ban a staff')
            return
        if admin in user.roles:
            await self.bot.say('lol hi look at this retard (<@' + author.id + '>) who tried to ban a staff')
            return

        banmessagechat = discord.Embed(description='Command successfully executed.', colour=0xE53935) #CHAT UPDATE
        banmessagechat.set_thumbnail(url=afxuserurl)
        banmessagechat.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        banmessagechat.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        banmessagechat.add_field(name='Kicked User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)
        banmessagechat.add_field(name='Reason:', value=reason)

        banlog = discord.Embed(description='Modlog Entry - `/kick`', colour=0xE53935) #MODLOG
        banlog.set_thumbnail(url=afxuserurl)
        banlog.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        banlog.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        banlog.add_field(name='Kicked User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)
        banlog.add_field(name='Reason:', value=reason)

        dmtobanned = discord.Embed(description='You were just kicked from the server.', colour=0xE53935) #DM TO AFXUSER
        dmtobanned.set_thumbnail(url=afxuserurl)
        dmtobanned.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        dmtobanned.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        dmtobanned.add_field(name='Kicked User:', value='<@' + afxidstr + '> (ID: `' + afxidstr + '`)', inline=True)
        dmtobanned.add_field(name='Reason:', value=reason)
        
        
        try:
            kickconfirmation = discord.Embed(description='Are you sure you want to kick <@' + afxuserid + '>? Type `yes` to confirm.', colour=0xE53935)
            await self.bot.say(embed=kickconfirmation)
            message = await self.bot.wait_for_message(timeout=5,
                                                      author=ctx.message.author)
            if not message:
                kickto = discord.Embed(description='I timed out after waiting too long.', colour=0xE53935)
                await self.bot.say(embed=kickto)
                return False

            elif message.clean_content.lower() != 'yes':
                kickcancel = discord.Embed(description='I guess not... command cancelled.', colour=0xE53935)
                await self.bot.say('I guess not... command cancelled.')
                return False

            await self.bot.send_message(user, embed=dmtobanned)
            await self.bot.kick(user)
            await self.bot.say(embed=banmessagechat)
            await self.bot.send_message(self.bot.get_channel('288467626890362880'), embed=banlog)

        except discord.errors.Forbidden:
            await self.bot.say('`discord.errors.Forbidden` - I do not have permission to kick members, or the highest role of the target is higher than mine.')
            return

        except discord.errors.HTTPException:
            await self.bot.say('`discord.errors.HTTPException` - Kicking the user failed.')
            return

    @commands.command(pass_context=True, no_pm=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator")
    async def unban(self, ctx, user: discord.User=None):
        """Unbans a user. You MUST use a Discord ID, or a tag."""

        author = ctx.message.author
        authstr = str(author)
        authimg = author.avatar_url
        server = author.server
        afxuser = str(user)
        afxuserurl = user.avatar_url
        afxuserid = user.id
        reasonstr = str(reason)
        afxidstr = str(afxuserid)

        banmessagechat = discord.Embed(description='Command successfully executed.', colour=0xE53935) #CHAT UPDATE
        banmessagechat.set_thumbnail(url=afxuserurl)
        banmessagechat.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        banmessagechat.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        banmessagechat.add_field(name='Unbanned User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)

        banlog = discord.Embed(description='Modlog Entry - `/unban`', colour=0xE53935) #MODLOG
        banlog.set_thumbnail(url=afxuserurl)
        banlog.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        banlog.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        banlog.add_field(name='Unbanned User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)

        dmtobanned = discord.Embed(description='You have just unbanned from the server.', colour=0xE53935) #DM TO AFXUSER
        dmtobanned.set_thumbnail(url=afxuserurl)
        dmtobanned.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        dmtobanned.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        dmtobanned.add_field(name='Unbanned User:', value='<@' + afxuserid + '> (ID: `' + afxidstr + '`)', inline=True)

        try:
            await self.bot.say(embed=banmessagechat)
            await self.bot.send_message(self.bot.get_channel('288467626890362880'), embed=banlog)
            await self.bot.send_message(user, embed=dmtobanned)
            await self.bot.unban('288455332173316106', user)

        except discord.errors.Forbidden:
            await self.bot.say('`discord.errors.Forbidden` - I do not have permission to unban members.')
            return

        except discord.errors.HTTPException:
            await self.bot.say('`discord.errors.HTTPException` - Unbanning the user failed.')
            return

    @commands.group(pass_context=True)
    async def gamenights(self, ctx):
        """Game Night Role Commands"""

        if ctx.invoked_subcommand is None:
            await self.bot.say('To enable GN announcements, do `/gamenights enable`.')
            await self.bot.say('To disable GN announcements, do `/gamenights disable`.')

    @gamenights.command(pass_context=True)
    async def disable(self, ctx):
        """Enable game night"""

        await self.bot.add_roles(ctx.message.author, discord.Role(id='359476128899006466', server='288455332173316106'))
        await self.bot.say('You have successfully opted out of game nights.')

    @gamenights.command(pass_context=True)
    async def enable(self, ctx):
        """Enable game night"""

        await self.bot.remove_roles(ctx.message.author, discord.Role(id='359476128899006466', server='288455332173316106'))
        await self.bot.say('You have successfully opted into game nights.')
        

    @commands.group(pass_context=True)
    async def appeal(self, ctx):
        """Appealing Commands"""

        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @appeal.command(pass_context=True)
    async def ban(self, ctx, *, msg=None):
        """Sends a ban appeal to the staff."""

        appealer = ctx.message.author
        appealerstr = str(appealer)
        appealerid = appealer.id
        appealerimg = appealer.avatar_url
        message = str(msg)

        appeal = discord.Embed(colour=0xD360F2)
        appeal.set_author(name='An appeal has been submitted.', icon_url='http://img.clipartall.com/lawyer-clip-art-clipartall-lawyer-clip-art-281_428.jpg')
        appeal.set_footer(text='ToS Community Discord Appeals', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        appeal.set_thumbnail(url=appealerimg)
        appeal.add_field(name='Appealer:', value='<@' + appealerid + '>, (ID: `' + appealerid + '`)', inline=True)
        appeal.add_field(name='Appeal Type:', value='Ban Appeal', inline=True)
        appeal.add_field(name='Appeal Contents:', value=msg, inline=True)

        try:
            await self.bot.send_message(self.bot.get_channel('297442649168936961'), embed=appeal)
            await self.bot.say('Your appeal was successfully sent.')
        
        except discord.errors.Forbidden:
            await self.bot.say('`discord.errors.Forbidden` - Contact <@222147236728012800> if this error shows')
            return

        except discord.errors.HTTPException:
            await self.bot.say('`discord.errors.HTTPException` - Sending the appeal failed.')

    @appeal.command(pass_context=True)
    async def mute(self, ctx, *, msg=None):
        """Sends a mute/channel block appeal to the staff."""

        appealer = ctx.message.author
        appealerstr = str(appealer)
        appealerid = appealer.id
        appealerimg = appealer.avatar_url
        message = str(msg)

        appeal = discord.Embed(colour=0xD360F2)
        appeal.set_author(name='An appeal has been submitted.', icon_url='http://img.clipartall.com/lawyer-clip-art-clipartall-lawyer-clip-art-281_428.jpg')
        appeal.set_footer(text='ToS Community Discord Appeals', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        appeal.set_thumbnail(url=appealerimg)
        appeal.add_field(name='Appealer:', value='<@' + appealerid + '>, (ID: `' + appealerid + '`)', inline=True)
        appeal.add_field(name='Appeal Type:', value='Mute/Channel Block Appeal', inline=True)
        appeal.add_field(name='Appeal Contents:', value=msg, inline=True)

        try:
            await self.bot.send_message(self.bot.get_channel('297442649168936961'), embed=appeal)
            await self.bot.say('Your appeal was successfully sent.')
        
        except discord.errors.Forbidden:
            await self.bot.say('`discord.errors.Forbidden` - Contact <@222147236728012800> if this error shows')
            return

        except discord.errors.HTTPException:
            await self.bot.say('`discord.errors.HTTPException` - Sending the appeal failed.')

    @appeal.command(pass_context=True)
    async def warn(self, ctx, *, msg=None):
        """Sends an appeal regarding a warned role to the staff."""

        appealer = ctx.message.author
        appealerstr = str(appealer)
        appealerid = appealer.id
        appealerimg = appealer.avatar_url
        message = str(msg)

        appeal = discord.Embed(colour=0xD360F2)
        appeal.set_author(name='An appeal has been submitted.', icon_url='http://img.clipartall.com/lawyer-clip-art-clipartall-lawyer-clip-art-281_428.jpg')
        appeal.set_footer(text='ToS Community Discord Appeals', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        appeal.set_thumbnail(url=appealerimg)
        appeal.add_field(name='Appealer:', value='<@' + appealerid + '>, (ID: `' + appealerid + '`)', inline=True)
        appeal.add_field(name='Appeal Type:', value='Warn Appeal', inline=True)
        appeal.add_field(name='Appeal Contents:', value=msg, inline=True)

        try:
            await self.bot.send_message(self.bot.get_channel('297442649168936961'), embed=appeal)
            await self.bot.say('Your appeal was successfully sent.')
        
        except discord.errors.Forbidden:
            await self.bot.say('`discord.errors.Forbidden` - Contact <@222147236728012800> if this error shows')
            return

        except discord.errors.HTTPException:
            await self.bot.say('`discord.errors.HTTPException` - Sending the appeal failed.')

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def helpreply(self, ctx, user: discord.Member, replytype: str, message: str):
        """Sends a message to a user"""

        auth = ctx.message.author
        appealerstr = str(auth)
        authimg = auth.avatar_url

        thereply = discord.Embed(description='You have recieved a response from your inquiry / bug report!', colour=0x8E24AA)
        thereply.set_footer(text='AeroSystem Help Desk, if you have another issue please send it in via commands.', icon_url='https://cdn.discordapp.com/avatars/282501616828153857/d45ca9b4f10937ef3756875dff5bad22.jpg?size=128')
        thereply.set_author(name='Help Desk Member: ' + authstr, icon_url=authimg)
        thereply.add_field(name='Reply Type:', value=replytype, inline=True)
        thereply.add_field(name='Response:', value=message, inline=True)

        await self.bot.send_message(user, embed=thereply)
        await self.bot.say('Message delivery attempt successful.')

    @commands.group(pass_context=True, no_pm=True)
    async def adminset(self, ctx):
        """Manage Admin settings"""
        if ctx.invoked_subcommand is None:
            await self.bot.send_cmd_help(ctx)

    @adminset.command(pass_context=True, name="selfroles")
    @checks.admin_or_permissions(manage_roles=True)
    async def adminset_selfroles(self, ctx, *, rolelist=None):
        """Set which roles users can set themselves.

        COMMA SEPARATED LIST (e.g. Admin,Staff,Mod)"""
        server = ctx.message.server
        if rolelist is None:
            await self.bot.say("selfrole list cleared.")
            self._set_selfroles(server, [])
            return
        unparsed_roles = list(map(lambda r: r.strip(), rolelist.split(',')))
        parsed_roles = list(map(lambda r: self._role_from_string(server, r),
                                unparsed_roles))
        if len(unparsed_roles) != len(parsed_roles):
            not_found = set(unparsed_roles) - {r.name for r in parsed_roles}
            await self.bot.say(
                "These roles were not found: {}\n\nPlease"
                " try again.".format(not_found))
        parsed_role_set = list({r.name for r in parsed_roles})
        self._set_selfroles(server, parsed_role_set)
        await self.bot.say(
            "Self roles successfully set to: {}".format(parsed_role_set))

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def announce(self, ctx, *, msg):
        """Announces a message to all servers that a bot is in."""
        if self._announce_msg is not None:
            await self.bot.say("Already announcing, wait until complete to"
                               " issue a new announcement.")
        else:
            self._announce_msg = msg
            self._announce_server = ctx.message.server

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def serverlock(self, ctx):
        """Toggles locking the current server list, will not join others"""
        if self._is_server_locked():
            self._set_serverlock(False)
            await self.bot.say("Server list unlocked")
        else:
            self._set_serverlock()
            await self.bot.say("Server list locked.")

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def partycrash(self, ctx, idnum=None):
        """Lists servers and generates invites for them"""
        owner = ctx.message.author
        if idnum:
            server = discord.utils.get(self.bot.servers, id=idnum)
            if server:
                await self._confirm_invite(server, owner, ctx)
            else:
                await self.bot.say("I'm not in that server")
        else:
            msg = ""
            servers = sorted(self.bot.servers, key=lambda s: s.name)
            for i, server in enumerate(servers, 1):
                msg += "{}: {}\n".format(i, server.name)
            msg += "\nTo post an invite for a server just type its number."
            for page in pagify(msg, delims=["\n"]):
                await self.bot.say(box(page))
                await asyncio.sleep(1.5)  # Just in case for rate limits
            msg = await self.bot.wait_for_message(author=owner, timeout=15)
            if msg is not None:
                try:
                    msg = int(msg.content.strip())
                    server = servers[msg - 1]
                except ValueError:
                    await self.bot.say("You must enter a number.")
                except IndexError:
                    await self.bot.say("Index out of range.")
                else:
                    try:
                        await self._confirm_invite(server, owner, ctx)
                    except discord.Forbidden:
                        await self.bot.say("I'm not allowed to make an invite"
                                           " for {}".format(server.name))
            else:
                await self.bot.say("Response timed out.")

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager", "Administrator")
    async def removerole(self, ctx, rolename, user: discord.Member=None, *, reason: str):
        """Removes a role from user."""
        auth = ctx.message.author
        channel = ctx.message.channel
        server = ctx.message.server
        afxuser = str(user)
        afximg = user.avatar_url
        authstr = str(auth)
        authimg = auth.avatar_url
        rolenamestr = str(rolename)
        removedsecondrole = False

        role = self._role_from_string(server, rolename)
        roleid = role.id
        afxuserid = user.id
        
        if role is None:
            await self.bot.say("Role not found.")
            return

        if role is None:
            await self.bot.say('That role cannot be found.')
            return

        if roleid in ['288457272663867392', '288682024515141634', '288464565791096838', '414196360321957888',
                      '414189641890267157', '414196208660119572']:
            await self.bot.say('What the fuck are you trying to do? Remove a staff role from someone? Shame on you.')
            return

        elif roleid in ['289508430350254080', '291743984525770754', '291743946642554883', '291743908306616323', '291743280813703168',
                      '291743388661841920', '291743325814521856', '291743168515538946', '291743471750873088', '291743680241336321',
                      '291743563711250442', '291743513182208000', '291743627489574912', '291743828849852416', '291743751846494208',
                      '321786146835267594', '321785124230397952', '321785338987282432', '321785330439159818']:
            secondaryrole = discord.Role(id='297159204181901323', server='288455332173316106')
            secondaryrolestr = 'Town (ID: `297159204181901323`)'
            addedsecondrole = True

        elif roleid in ['289509219214950400', '291744083750158357', '291744254563319809', '291744342572269568', '291744422213844992',
                        '291744553919184897', '291744602090897408', '291744671292456960', '291744520469610496', '321786150916194304', '321786146835267594']:
            secondaryrole = discord.Role(id='297159278303641600', server='288455332173316106')
            secondaryrolestr = 'Mafia (ID: `297159278303641600`)'
            addedsecondrole = True

        elif roleid in ['291744786275106817', '291745330574393344', '291745200328671243', '326914566263013386']:
            secondaryrole = discord.Role(id='297169993270034433', server='288455332173316106')
            secondaryrolestr = 'Neutral Killing (ID: `297169993270034433`)'
            addedsecondrole = True

        elif roleid in ['291745801107931142', '291745696707772417', '321785643812388864']:
            secondaryrole = discord.Role(id='297170017634746369', server='288455332173316106')
            secondaryrolestr = 'Neutral Benign (ID: `297170017634746369`)'
            addedsecondrole = True

        elif roleid in ['291745484681510922', '289509291306647552']:
            secondaryrole = discord.Role(id='297170044553789440', server='288455332173316106')
            secondaryrolestr = 'Neutral Evil (ID: `297170044553789440`)'
            addedsecondrole = True

        elif roleid in ['288682060414058516', '291746016418594827', '321785635956588544', '321786136974458921', '326914120576270347']:
            secondaryrole = discord.Role(id='297170076002680840', server='288455332173316106')
            secondaryrolestr = 'Neutral Chaos (ID: `297170076002680840`)'
            addedsecondrole = True

        elif roleid in ['321784223608340480', '321784220240314370', '321784224866631690', '321784216075501569', '321784193451556866','321784203127816193' ]:
            secondaryrole = discord.Role(id='291745541581307904', server='288455332173316106')
            secondaryrolestr = 'Coven (ID: `291745541581307904`)'
            addedsecondrole = True

        else:
            addedsecondrole = False

        if user is None:
            user = author

        roleupdate = discord.Embed(description='Command successfully executed.', colour=0xE53935) #CHAT UPDATE ONLY.
        roleupdate.set_thumbnail(url=afximg)
        roleupdate.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        roleupdate.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        roleupdate.add_field(name='Affected Member:', value='<@' + afxuserid + '>', inline=True)
        roleupdate.add_field(name='Role removed:', value=rolenamestr + ' (Role ID: `' + roleid + '`)', inline=True)
        roleupdate.add_field(name='Reason:', value=reason, inline=True)
        
        if addedsecondrole is True:
            roleupdate.add_field(name='Secondary role removed:', value=secondaryrolestr)

        rulog = discord.Embed(description='Modlog Entry - `/removerole`', colour=0xE53935) #MODLOG ENTRY
        rulog.set_thumbnail(url=afximg)
        rulog.set_footer(text='Action taken on ToS Community Discord', icon_url='https://images-ext-1.discordapp.net/.eJwNyFEOgyAMANC7cABqW4RqsuwsprAN44SI-9F4d_c-32l-22JG89n32kYAjauNuWnZ4lSr1fKFrGVtQCKu75kJAzN67DxQJ-hSdJNXcqKU_L9xCExhkKAvO9f3s-UjPZDEXDf2iR9p.2RHdV9UghhwIdEp7zT3-rCiSsLQ?width=80&height=80')
        rulog.set_author(name='Staff Member Name: ' + authstr, icon_url=authimg)
        rulog.add_field(name='Affected Member:', value='<@' + afxuserid + '>', inline=True)
        rulog.add_field(name='Role removed:', value=rolenamestr + ' (Role ID: `' + roleid + '`)', inline=True)
        rulog.add_field(name='Reason:', value=reason, inline=True)
        if addedsecondrole is True:
            rulog.add_field(name='Secondary role removed:', value=secondaryrolestr)

        if role in user.roles:
            try:
                await self.bot.remove_roles(user, role)
                await self.bot.say(embed=roleupdate)
                if addedsecondrole is True:
                    await self.bot.remove_roles(user, secondaryrole)
                    pass
                await self.bot.send_message(self.bot.get_channel('288467626890362880'), embed=rulog)
            except discord.Forbidden:
                await self.bot.say("I don't have permissions to manage roles, or my role is not high enough, or it was meant to be like that.")
        else:
            await self.bot.say("User does not have that role.")

    @commands.command(pass_context=True, no_pm=True)
    async def say(self, ctx, *, text):
        """Bot repeats what you tell it to, utility for scheduler."""
        channel = ctx.message.channel
        await self.bot.send_message(channel, text)

    @commands.group(no_pm=True, pass_context=True, invoke_without_command=True)
    async def selfrole(self, ctx, *, rolename):
        """Allows users to set their own role.

        Configurable using `adminset`"""
        server = ctx.message.server
        author = ctx.message.author
        role_names = self._get_selfrole_names(server)
        if role_names is None:
            await self.bot.say("I have no user settable roles for this"
                               " server.")
            return

        f = self._role_from_string
        roles = [f(server, r) for r in role_names if r is not None]

        role_to_add = self._role_from_string(server, rolename, roles=roles)

        try:
            await self.bot.add_roles(author, role_to_add)
        except discord.errors.Forbidden:
            log.debug("{} just tried to add a role but I was forbidden".format(
                author.name))
            await self.bot.say("I don't have permissions to do that.")
        except AttributeError:  # role_to_add is NoneType
            log.debug("{} not found as settable on {}".format(rolename,
                                                              server.id))
            await self.bot.say("That role isn't user settable.")
        else:
            log.debug("Role {} added to {} on {}".format(rolename, author.name,
                                                         server.id))
            await self.bot.say("Role added.")

    @selfrole.command(no_pm=True, pass_context=True, name="remove")
    async def selfrole_remove(self, ctx, *, rolename):
        """Allows users to remove their own roles

        Configurable using `adminset`"""
        server = ctx.message.server
        author = ctx.message.author
        role_names = self._get_selfrole_names(server)
        if role_names is None:
            await self.bot.say("I have no user settable roles for this"
                               " server.")
            return

        f = self._role_from_string
        roles = [f(server, r) for r in role_names if r is not None]

        role_to_remove = self._role_from_string(server, rolename, roles=roles)

        try:
            await self.bot.remove_roles(author, role_to_remove)
        except discord.errors.Forbidden:
            log.debug("{} just tried to remove a role but I was"
                      " forbidden".format(author.name))
            await self.bot.say("I don't have permissions to do that.")
        except AttributeError:  # role_to_remove is NoneType
            log.debug("{} not found as removeable on {}".format(rolename,
                                                                server.id))
            await self.bot.say("That role isn't user removeable.")
        else:
            log.debug("Role {} removed from {} on {}".format(rolename,
                                                             author.name,
                                                             server.id))
            await self.bot.say("Role removed.")

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def sudo(self, ctx, user: discord.Member, *, command):
        """Runs the [command] as if [user] had run it. DON'T ADD A PREFIX
        """
        new_msg = deepcopy(ctx.message)
        new_msg.author = user
        new_msg.content = self.bot.settings.get_prefixes(new_msg.server)[0] \
            + command
        await self.bot.process_commands(new_msg)

    @commands.command(pass_context=True, hidden=True)
    @checks.is_owner()  # I don't know how permissive this should be yet
    async def whisper(self, ctx, id, *, text):
        author = ctx.message.author

        target = discord.utils.get(self.bot.get_all_members(), id=id)
        if target is None:
            target = self.bot.get_channel(id)
            if target is None:
                target = self.bot.get_server(id)

        prefix = "Hello, you're getting a message from {} ({})".format(
            author.name, author.id)
        payload = "{}\n\n{}".format(prefix, text)

        try:
            for page in pagify(payload, delims=[" ", "\n"], shorten_by=10):
                await self.bot.send_message(target, box(page))
        except discord.errors.Forbidden:
            log.debug("Forbidden to send message to {}".format(id))
        except (discord.errors.NotFound, discord.errors.InvalidArgument):
            log.debug("{} not found!".format(id))
        else:
            await self.bot.say("Done.")

    async def announcer(self, msg):
        server_ids = map(lambda s: s.id, self.bot.servers)
        for server_id in server_ids:
            if self != self.bot.get_cog('Admin'):
                break
            server = self.bot.get_server(server_id)
            if server is None:
                continue
            if server == self._announce_server:
                continue
            chan = server.default_channel
            log.debug("Looking to announce to {} on {}".format(chan.name,
                                                               server.name))
            me = server.me
            if chan.permissions_for(me).send_messages:
                log.debug("I can send messages to {} on {}, sending".format(
                    server.name, chan.name))
                await self.bot.send_message(chan, msg)
            await asyncio.sleep(1)

    async def announce_manager(self):
        while self == self.bot.get_cog('Admin'):
            if self._announce_msg is not None:
                log.debug("Found new announce message, announcing")
                await self.announcer(self._announce_msg)
                self._announce_msg = None
            await asyncio.sleep(1)

    async def server_locker(self, server):
        if self._is_server_locked():
            await self.bot.leave_server(server)


def check_files():
    if not os.path.exists('data/admin/settings.json'):
        try:
            os.mkdir('data/admin')
        except FileExistsError:
            pass
        else:
            dataIO.save_json('data/admin/settings.json', {})


def setup(bot):
    check_files()
    n = Admin(bot)
    bot.add_cog(n)
    bot.add_listener(n.server_locker, "on_server_join")
    bot.loop.create_task(n.announce_manager())
