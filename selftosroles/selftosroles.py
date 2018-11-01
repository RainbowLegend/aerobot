class SelfToSRoles:
    """Self ToS Role assignment system. ~Danners"""

    default = {}

    def __init__(self, bot):
        db = dataIO.load_json("data/selftosroles/roles.json")
        self.bot = bot
        self.db = defaultdict(lambda: default.copy(), db)

    #  Declare global vars
    global townRole
    townRole = discord.Role(id='297159204181901323', server = '288455332173316106')

    global mafia
    mafia = discord.Role(id='297159278303641600', server='288455332173316106')

    global nkRole
    nkRole = discord.Role(id='297169993270034433', server='288455332173316106')

    global nbRole
    nbRole = discord.Role(id='297170017634746369', server = '288455332173316106')

    global neRole
    neRole = discord.Role(id='297170044553789440', server='288455332173316106')

    global coven
    coven = discord.Role(id='291745541581307904', server='288455332173316106')

    global ncRole
    ncRole = discord.Role(id='297170076002680840', server='288455332173316106')

    #  Declare role-removal functions

    async def store_currentrole(self, ctx, role, role2):
        await self.bot.add_roles(ctx.message.author, role2)
        roleid = role.id
        roleid2 = role2.id
        userid = ctx.message.author.id
        if userid in self.db:
            del self.db[userid]
            self.save()
            pass
        self.db[userid] = []
        self.db[userid].append(roleid)
        self.db[userid].append(roleid2)
        self.save()

        await self.bot.add_roles(ctx.message.author, role)

    async def _remove_roles(self, ctx):
        server = ctx.message.server
        user = ctx.message.author

        to_remove = []

        for role_id in self.db[user.id]:
            role = discord.utils.get(server.roles, id=role_id)
            if role:
                to_remove.append(role)

        self.save()

        await self.bot.remove_roles(user, *to_remove)

    @commands.command(pass_context=True)
    @commands.has_any_role("Senior Moderator", "Moderator", "AeroBot Manager",
                           "Administrator", "Game Moderator", "game night moderator")
    async def pingnotif(self, ctx):
        questionOne = await self.bot.say("Would you like to ping `all`, `classic` or `coven`?")
        mentioned = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)
        covenNotification = discord.Role(id='358655924342095874', server='288455332173316106')
        toscd = discord.Server(id='288455332173316106')
        optinrole = discord.Role(id='379748801197637644', server='288455332173316106')

        # If an invalid response or nothing is entered, command cancels and returns.
        if mentioned is None:
            await self.bot.say("Command cancelled.")
            await self.bot.delete_message(questionOne)
            return

        # If the coven choice is picked, continue here.
        elif mentioned.clean_content.lower() == "coven":
            await self.bot.delete_message(questionOne)
            await self.bot.delete_message(mentioned)
            roleToPing = "coven"
            questionTwo = await self.bot.say("Good. We'll be pinging the `Coven Notifications` role. "
                                             "What would you like to say?")
            messagecontent = await self.bot.wait_for_message(author=ctx.message.author, timeout=60)

            # If an invalid response or nothing is entered, command cancels and returns.
            if messagecontent is None:
                await self.bot.delete_message(questionTwo)
                await self.bot.say("Command cancelled.")
                return

            # If a message is entered, the command continues.
            else:
                await self.bot.delete_message(questionTwo)
                await self.bot.delete_message(messagecontent)
                confirmation = await self.bot.say("Okay, good. "
                                                  "Confirm (Y/n) this is what you would like the message to say: "
                                                  "```" + str(messagecontent.clean_content) + "```")
                confResponse = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)

                # If the user's response is Y/y, continue here. Sends the final message.
                if confResponse.clean_content.lower() in ['y', 'yes']:

                    await self.bot.edit_role(toscd, covenNotification, name="Coven Notifications",
                                             colour=discord.Colour(0x550a94), mentionable=True)

                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    
                    await self.bot.say("<@&358655924342095874> **||** Message from <@"
                                       + str(ctx.message.author.id) + ">")
                    await self.bot.say(str(messagecontent.clean_content))

                    await self.bot.edit_role(toscd, covenNotification, name="Coven Notifications",
                                             colour=discord.Colour(0x550a94), mentionable=False)

                    return


                # If the user's response is N/n, command cancels and returns.
                if confResponse.clean_content.lower() in ['n', 'no']:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    await self.bot.say("Command cancelled.")
                    return

                # If nothing or invalid is entered, command is cancelled and returns.
                else:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    await self.bot.say("command cancelled.")
                    return

        elif mentioned.clean_content.lower() == "classic":
            await self.bot.delete_message(questionOne)
            await self.bot.delete_message(mentioned)
            roleToPing = "classic"
            questionTwo = await self.bot.say("Good. We'll be pinging the `Game Notifications` role."
                                             " What would you like to say?")
            messagecontent = await self.bot.wait_for_message(author=ctx.message.author, timeout=60)

            # If an invalid response or nothing is entered, command cancels and returns.
            if messagecontent is None:
                await self.bot.delete_message(questionTwo)
                await self.bot.say("Command cancelled.")
                return

            # If a message is entered, the command continues.
            else:
                await self.bot.delete_message(questionTwo)
                await self.bot.delete_message(messagecontent)
                confirmation = await self.bot.say("Okay, good. "
                                                  "Confirm (Y/n) this is what you would like the message to say: "
                                                  "```" + str(messagecontent.clean_content) + "```")
                confResponse = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)

                # If the user's response is Y/y, continue here. Sends the final message.
                if confResponse.clean_content.lower() in ['y', 'yes']:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)

                    await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                             colour=discord.Colour(0x880999), mentionable=True)
                    
                    await self.bot.say("<@&379748801197637644> **||** "
                                       "Message from: <@" + str(ctx.message.author.id) + ">")
                    await self.bot.say(str(messagecontent.clean_content))

                    await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                             colour=discord.Colour(0x880999), mentionable=False)

                    return

                    # If the user's response is N/n, command cancels and returns.
                if confResponse.clean_content.lower() in ['n', 'no']:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    await self.bot.say("Command cancelled.")
                    return

                    # If nothing or invalid is entered, command is cancelled and returns.
                else:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    await self.bot.say("command cancelled.")
                    return
            
        elif mentioned.clean_content.lower() == "all":
            await self.bot.delete_message(questionOne)
            await self.bot.delete_message(mentioned)
            roleToPing = "all"
            questionTwo = await self.bot.say("Good. We'll be pinging both the Coven and Game Notifications role. "
                                             "What would you like to say?")
            messagecontent = await self.bot.wait_for_message(author=ctx.message.author, timeout=60)

            # If an invalid response or nothing is entered, command cancels and returns.
            if messagecontent is None:
                await self.bot.delete_message(questionTwo)
                await self.bot.say("Command cancelled.")
                return

            # If a message is entered, the command continues.
            else:
                await self.bot.delete_message(questionTwo)
                await self.bot.delete_message(messagecontent)
                confirmation = await self.bot.say("Okay, good. "
                                                  "Confirm (Y/n) this is what you would like the message to say: "
                                                  "```" + str(messagecontent.clean_content) + "```")
                confResponse = await self.bot.wait_for_message(author=ctx.message.author, timeout=15)

                # If the user's response is Y/y, continue here. Sends the final message.
                if confResponse.clean_content.lower() in ['y', 'yes']:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)

                    await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                             colour=discord.Colour(0x880999), mentionable=True)
                    await self.bot.edit_role(toscd, covenNotification, name="Coven Notifications",
                                 colour=discord.Colour(0x550a94), mentionable=True)
                    
                    await self.bot.say("<@&379748801197637644> <@&358655924342095874> **||** "
                                       "Message from: <@" + str(ctx.message.author.id) + ">")
                    await self.bot.say(str(messagecontent.clean_content))

                    await self.bot.edit_role(toscd, optinrole, name="Game Notifications",
                                             colour=discord.Colour(0x880999), mentionable=False)
                    await self.bot.edit_role(toscd, covenNotification, name="Coven Notifications",
                                             colour=discord.Colour(0x550a94), mentionable=False)
                    return

                # If the user's response is N/n, command cancels and returns.
                if confResponse.clean_content.lower() in ['n', 'no']:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    await self.bot.say("Command cancelled.")
                    return

                # If nothing or invalid is entered, command is cancelled and returns.
                else:
                    await self.bot.delete_message(confirmation)
                    await self.bot.delete_message(confResponse)
                    await self.bot.say("command cancelled.")
                    return
        else:
            await self.bot.say("I guess it was <@" + str(ctx.message.author.id) + "> that fucked up this time. "
                                                                                  "what a surprise.")
            return
        
    @commands.command(pass_context=True)
    async def nsfw(self, ctx):
        """NSFW Commands"""
        nsfw = discord.Role(id='425123783863435276', server = '288455332173316106')
        if nsfw in ctx.message.author.roles:
            await self.bot.remove_roles(ctx.message.author, nsfw)
            await self.bot.say("<@" + ctx.message.author.id + ">, you have been unassigned the NSFW role.")
            return
        else:
            await self.bot.add_roles(ctx.message.author, nsfw)
            await self.bot.say("<@" + ctx.message.author.id + ">, you have been assigned the NSFW role.")
            return
                                
    @commands.group(pass_context=True)
    async def gnotif(self, ctx):
        """Notifications for games"""

        channel = ctx.message.channel
        channelid = str(channel.id)
        authorid = str(ctx.message.author.id)

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            if ctx.invoked_subcommand is None:
                await self.bot.say('Use either `/gnotif enable` to enable notifcations or '
                                   '`/gnotif disable` to disable notifications.')
        else:
            await self.bot.say('<@' + authorid + '> **||** This command is only usable in '
                                                 '<#288455332173316106> or <#288463362357067777>.')
            return

    @gnotif.command(pass_context=True)
    async def enable(self, ctx):
        """Enable Gnotifs"""

        channel = ctx.message.channel
        channelid = str(channel.id)
        authorid = str(ctx.message.author.id)

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return

        user = ctx.message.author
        optinrole = discord.Role(id='379748801197637644', server='288455332173316106')

        await self.bot.add_roles(user, optinrole)
        await self.bot.say('You will now **recieve** game notifications. Use `/gnotif disable` to *disable* them.')

    @gnotif.command(pass_context=True)
    async def disable(self, ctx):
        """Disable Gnotifs"""

        channel = ctx.message.channel
        channelid = str(channel.id)
        authorid = str(ctx.message.author.id)

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return

        user = ctx.message.author
        optinrole = discord.Role(id='379748801197637644', server='288455332173316106')

        await self.bot.remove_roles(user, optinrole)
        await self.bot.say('You will now **not** recieve game notifications. Use `/gnotif enable` to *enable* them.')

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def testr(self, ctx):
        """hi"""

        emoteLib = discord.Server(id='401122122400923648')

        animpartyblob1 = discord.Emoji(name='animpartyblob1', server=emoteLib)
        pbID = str(animpartyblob1.id)

        await self.bot.say("<a:animpartyblob1:401122373236948993> <a:animpartyblob2:401122373367234570> "
                           "<a:animpartyblob3:401122373396463616> <a:animpartyblob4:401122373262376971>"
                           " <a:animpartyblob5:401122373425823744> <a:animpartyblob6:401122373614567434> "
                           "<a:animpartyblob7:401122373698322432> <a:animpartyblob8:401122373270503427> "
                           "<a:animpartyblob9:401122373434343431>")

    @commands.command(pass_context=True)
    async def getuserid(self, ctx, user : discord.User):
        """Get a user's ID. If the bot cannot find the person, try making sure capitalization is followed
        or use the full ping including the discriminator."""

        userid = str(user.id)
        authid = str(ctx.message.author.id)

        await self.bot.say('<@' + authid + "> **||** That user's ID is **`" + userid + "`**")

    

    @commands.group(pass_context=True)
    async def tosrole(self, ctx):
        """Self-applying ToS Role Commands"""

        #Declare Variables

        channel = ctx.message.channel
        channelid = str(channel.id)
        authorid = str(ctx.message.author.id)

        #Check for correct channels

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            if ctx.invoked_subcommand is None:
                await self.bot.say('<@' + authorid + '> **||** For a list of roles, please check <#288752291463299083>.'
                                                     ' Make sure capitalization is also followed.')
        else:
            await self.bot.say('<@' + authorid + '> **||** This command is only usable in '
                                                 '<#288455332173316106> or <#288463362357067777>.')
            return

    @tosrole.command(pass_context=True)
    async def Jailor(self, ctx):
        """Applies the Jailor role."""

        channel = ctx.message.channel
        channelid = str(channel.id)
        jailor = discord.Role(id='289508430350254080', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Jailor.')
        await self.store_currentrole(ctx, townRole, jailor)
        await self.bot.add_roles(author, townRole)
        await self.bot.add_roles(author, jailor)

    @tosrole.command(pass_context=True)
    async def Veteran(self, ctx):
        """Applies the Veteran role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        veteran = discord.Role(id='291743946642554883', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Veteran.')#chat message
        await self.store_currentrole(ctx, townRole, veteran)
        await self.bot.add_roles(author, townRole)#role
        await self.bot.add_roles(author, veteran)#roleclass

    @tosrole.command(pass_context=True)
    async def Vigilante(self, ctx):
        """Applies the Vigilante role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        vigilante = discord.Role(id='291743984525770754', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Vigilante.')#chat message
        await self.store_currentrole(ctx, townRole, vigilante)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, vigilante)#role

    @tosrole.command(pass_context=True)
    async def VampireHunter(self, ctx):
        """Applies the Vampire Hunter role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        vamphunter = discord.Role(id='291743908306616323', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)
            await asyncio.sleep(1)

        await self.store_currentrole(ctx, townRole, vamphunter)
        await self.bot.add_roles(author, vamphunter)#role
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Vampire Hunter.')#chat message

    @tosrole.command(pass_context=True)
    async def Investigator(self, ctx):
        """Applies the Investigator role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        investigator = discord.Role(id='291743168515538946', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Investigator.')#chat message
        await self.store_currentrole(ctx, townRole, investigator)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, investigator)#role

    @tosrole.command(pass_context=True)
    async def Lookout(self, ctx):
        """Applies the Lookout role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        lookout = discord.Role(id='291743325814521856', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Lookout.')#chat message
        await self.store_currentrole(ctx, townRole, lookout)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, lookout)#role

    @tosrole.command(pass_context=True)
    async def Sheriff(self, ctx):
        """Applies the Sheriff role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        sheriff = discord.Role(id='291743280813703168', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Sheriff.')#chat message
        await self.store_currentrole(ctx, townRole, sheriff)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, sheriff)#role

    @tosrole.command(pass_context=True)
    async def Spy(self, ctx):
        """Applies the Spy role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        spy = discord.Role(id='291743388661841920', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Spy.')#chat message
        await self.store_currentrole(ctx, townRole, spy)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, spy)#role

    @tosrole.command(pass_context=True)
    async def Escort(self, ctx):
        """Applies the Escort role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        escort = discord.Role(id='291743471750873088', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Escort.')#chat message
        await self.store_currentrole(ctx, townRole, escort)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, escort)#role

    @tosrole.command(pass_context=True)
    async def Mayor(self, ctx):
        """Applies the Mayor role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        mayor = discord.Role(id='291743563711250442', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Mayor.')#chat message
        await self.store_currentrole(ctx, townRole, mayor)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, mayor)#role

    @tosrole.command(pass_context=True)
    async def Medium(self, ctx):
        """Applies the Medium role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        medium = discord.Role(id='291743513182208000', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Medium.')#chat message
        await self.store_currentrole(ctx, townRole, medium)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, medium)#role

    @tosrole.command(pass_context=True)
    async def Retributionist(self, ctx):
        """Applies the Retributionist role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        retributionist = discord.Role(id='291743627489574912', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Retributionist.')#chat message
        await self.store_currentrole(ctx, townRole, retributionist)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, retributionist)#role

    @tosrole.command(pass_context=True)
    async def Transporter(self, ctx):
        """Applies the Transporter role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        transporter = discord.Role(id='291743680241336321', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Transporter.')#chat message
        await self.store_currentrole(ctx, townRole, transporter)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, transporter)#role

    @tosrole.command(pass_context=True)
    async def Doctor(self, ctx):
        """Applies the Doctor role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        doctor = discord.Role(id='291743828849852416', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Doctor.')#chat message
        await self.store_currentrole(ctx, townRole, doctor)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, doctor)#role

    @tosrole.command(pass_context=True)
    async def BodyGuard(self, ctx):
        """Applies the BodyGuard role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        bodyguard = discord.Role(id='291743751846494208', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to BodyGuard.')#chat message
        await self.store_currentrole(ctx, townRole, bodyguard)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, bodyguard)#role

    @tosrole.command(pass_context=True)
    async def Trapper(self, ctx):
        """Applies the BodyGuard role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        trapper = discord.Role(id='321785341340286976', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Trapper.')#chat message
        await self.store_currentrole(ctx, townRole, trapper)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, trapper)#role

    @tosrole.command(pass_context=True)
    async def Crusader(self, ctx):
        """Applies the BodyGuard role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        crusader = discord.Role(id='321785124230397952', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Crusader.')#chat message
        await self.store_currentrole(ctx, townRole, crusader)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, crusader)#role

    @tosrole.command(pass_context=True)
    async def Psychic(self, ctx):
        """Applies the BodyGuard role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        psychic = discord.Role(id='321785338987282432', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Psychic.')#chat message
        await self.store_currentrole(ctx, townRole, psychic)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, psychic)#role

    @tosrole.command(pass_context=True)
    async def Tracker(self, ctx):
        """Applies the BodyGuard role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        tracker = discord.Role(id='321785330439159818', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Tracker.')#chat message
        await self.store_currentrole(ctx, townRole, tracker)
        await self.bot.add_roles(author, townRole)#roleclass
        await self.bot.add_roles(author, tracker)#role

    @tosrole.command(pass_context=True)
    async def Godfather(self, ctx):
        """Applies the Godfather role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        godfather = discord.Role(id='289509219214950400', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Godfather.')#chat message
        await self.store_currentrole(ctx, mafia, godfather)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, godfather)#role

    @tosrole.command(pass_context=True)
    async def Mafioso(self, ctx):
        """Applies the Mafioso role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        mafioso = discord.Role(id='291744083750158357', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Mafioso.')#chat message
        await self.store_currentrole(ctx, mafia, mafioso)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, mafioso)#role

    @tosrole.command(pass_context=True)
    async def Blackmailer(self, ctx):
        """Applies the Blackmailer role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        blackmailer = discord.Role(id='291744254563319809', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Blackmailer.')#chat message
        await self.store_currentrole(ctx, mafia, blackmailer)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, blackmailer)#role

    @tosrole.command(pass_context=True)
    async def Consigliere(self, ctx):
        """Applies the Consigliere role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        consig = discord.Role(id='291744342572269568', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Consigliere.')#chat message
        await self.store_currentrole(ctx, mafia, consig)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, consig)#role

    @tosrole.command(pass_context=True)
    async def Consort(self, ctx):
        """Applies the Consort role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        consort = discord.Role(id='291744422213844992', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Consort.')#chat message
        await self.store_currentrole(ctx, mafia, consort)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, consort)#role

    @tosrole.command(pass_context=True)
    async def Disguiser(self, ctx):
        """Applies the Disguiser role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        disg = discord.Role(id='291744520469610496', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Disguiser.')#chat message
        await self.store_currentrole(ctx, mafia, disg)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, disg)#role

    @tosrole.command(pass_context=True)
    async def Forger(self, ctx):
        """Applies the Forger role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        forg = discord.Role(id='291744553919184897', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Forger.')#chat message
        await self.store_currentrole(ctx, mafia, forg)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, forg)#role

    @tosrole.command(pass_context=True)
    async def Framer(self, ctx):
        """Applies the Framer role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        framer = discord.Role(id='291744602090897408', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Framer.')#chat message
        await self.store_currentrole(ctx, mafia, framer)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, framer)#role

    @tosrole.command(pass_context=True)
    async def Janitor(self, ctx):
        """Applies the Janitor role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        janit = discord.Role(id='291744671292456960', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Janitor.')#chat message
        await self.store_currentrole(ctx, mafia, janit)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, janit)#rol

    @tosrole.command(pass_context=True)
    async def Ambusher(self, ctx):
        """Applies the Janitor role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        ambusher = discord.Role(id='321786150916194304', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Ambusher.')#chat message
        await self.store_currentrole(ctx, mafia, ambusher)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, ambusher)#role

    @tosrole.command(pass_context=True)
    async def Hypnotist(self, ctx):
        """Applies the Janitor role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        hypnotist = discord.Role(id='321786146835267594', server='288455332173316106')


        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Hypnotist.')#chat message
        await self.store_currentrole(ctx, mafia, hypnotist)
        await self.bot.add_roles(author, mafia)#roleclass
        await self.bot.add_roles(author, hypnotist)#role

    @tosrole.command(pass_context=True)
    async def Arsonist(self, ctx):
        """Applies the Arsonist role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        arsonist = discord.Role(id='291744786275106817', server='288455332173316106')


        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Arsonist.')#chat message
        await self.store_currentrole(ctx, nkRole, arsonist)
        await self.bot.add_roles(author, nkRole)#roleclass
        await self.bot.add_roles(author, arsonist)#rol

    @tosrole.command(pass_context=True)
    async def SerialKiller(self, ctx):
        """Applies the Lookout role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        sk = discord.Role(id='291745200328671243', server='288455332173316106')


        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Serial Killer.')#chat message
        await self.store_currentrole(ctx, nkRole, sk)
        await self.bot.add_roles(author, nkRole)#roleclass
        await self.bot.add_roles(author, sk)#rol

    @tosrole.command(pass_context=True)
    async def Werewolf(self, ctx):
        """Applies the Werewolf role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        ww = discord.Role(id='291745330574393344', server='288455332173316106')


        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Werewolf.')#chat message
        await self.store_currentrole(ctx, nkRole, ww)
        await self.bot.add_roles(author, nkRole)#roleclass
        await self.bot.add_roles(author, ww)#role

    @tosrole.command(pass_context=True)
    async def Amnesiac(self, ctx):
        """Applies the Amnesiac role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        amne = discord.Role(id='291745696707772417', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Amnesiac.')#chat message
        await self.store_currentrole(ctx, nbRole, amne)
        await self.bot.add_roles(author, nbRole)#roleclass
        await self.bot.add_roles(author, amne)#rol

    @tosrole.command(pass_context=True)
    async def Survivor(self, ctx):
        """Applies the Survivor role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        surv = discord.Role(id='291745801107931142', server='288455332173316106')


        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Survivor.')#chat message
        await self.store_currentrole(ctx, nbRole, surv)
        await self.bot.add_roles(author, nbRole)#roleclass
        await self.bot.add_roles(author, surv)#role

    @tosrole.command(pass_context=True)
    async def GuardianAngel(self, ctx):
        """Applies the Survivor role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        guardianangel = discord.Role(id='321785643812388864', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Guardian Angel.')#chat message
        await self.store_currentrole(ctx, nbRole, guardianangel)
        await self.bot.add_roles(author, nbRole)#roleclass
        await self.bot.add_roles(author, guardianangel)#role

    @tosrole.command(pass_context=True)
    async def Executioner(self, ctx):
        """Applies the Executioner role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        exe = discord.Role(id='289509291306647552', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Executioner.')#chat message
        await self.store_currentrole(ctx, neRole, exe)
        await self.bot.add_roles(author, neRole)#roleclass
        await self.bot.add_roles(author, exe)#role

    @tosrole.command(pass_context=True)
    async def Witch(self, ctx):
        """Applies the Witch role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        witch = discord.Role(id='400981824706445328', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Witch.')#chat message
        await self.store_currentrole(ctx, neRole, witch)
        await self.bot.add_roles(author, neRole)#roleclass
        await self.bot.add_roles(author, witch)#role

    @tosrole.command(pass_context=True)
    async def Jester(self, ctx):
        """Applies the Lookout role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        jest = discord.Role(id='291745484681510922', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Jester.')#chat message
        await self.store_currentrole(ctx, neRole, jest)
        await self.bot.add_roles(author, neRole)#roleclass
        await self.bot.add_roles(author, jest)#role
        
    @tosrole.command(pass_context=True)
    async def Necromancer(self, ctx):
        """Applies the Witch role."""#description
        channel = ctx.message.channel
        channelid = str(channel.id)
        necromancer = discord.Role(id='321784223608340480', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Necromancer.')#chat message
        await self.store_currentrole(ctx, coven, necromancer)
        await self.bot.add_roles(author, coven)#roleclass
        await self.bot.add_roles(author, necromancer)#role

    @tosrole.command(pass_context=True)
    async def Medusa(self, ctx):
        """Applies the Witch role."""#description
        channel = ctx.message.channel
        channelid = str(channel.id)
        medusa = discord.Role(id='321784220240314370', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Medusa.')#chat message
        await self.store_currentrole(ctx, coven, medusa)
        await self.bot.add_roles(author, coven)#roleclass
        await self.bot.add_roles(author, medusa)#role

    @tosrole.command(pass_context=True)
    async def CovenLeader(self, ctx):
        """Applies the Witch role."""#description
        channel = ctx.message.channel
        channelid = str(channel.id)
        covenleader = discord.Role(id='321784224866631690', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        
        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Coven Leader.')#chat message
        await self.store_currentrole(ctx, coven, covenleader)
        await self.bot.add_roles(author, coven)#roleclass
        await self.bot.add_roles(author, covenleader)#role

    @tosrole.command(pass_context=True)
    async def Poisoner(self, ctx):
        """Applies the Witch role."""#description
        channel = ctx.message.channel
        channelid = str(channel.id)
        poisoner = discord.Role(id='321784203127816193', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Poisoner.')#chat message
        await self.store_currentrole(ctx, coven, poisoner)
        await self.bot.add_roles(author, coven)#roleclass
        await self.bot.add_roles(author, poisoner)#role

    @tosrole.command(pass_context=True)
    async def PotionMaster(self, ctx):
        """Applies the Witch role."""#description
        channel = ctx.message.channel
        channelid = str(channel.id)
        potionmaster = discord.Role(id='321784216075501569', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Potion Master.')#chat message
        await self.store_currentrole(ctx, coven, potionmaster)
        await self.bot.add_roles(author, coven)#roleclass
        await self.bot.add_roles(author, potionmaster)#role

    @tosrole.command(pass_context=True)
    async def HexMaster(self, ctx):
        """Applies the Witch role."""#description
        channel = ctx.message.channel
        channelid = str(channel.id)
        author = ctx.message.author
        hexmaster = discord.Role(id='321784193451556866', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return

        if author.id in self.db:
            await self._remove_roles(ctx)
        
        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Hex Master.')#chat message
        await self.store_currentrole(ctx, hexmaster, coven)
        await self.bot.add_roles(author, coven)#roleclass
        await self.bot.add_roles(author, hexmaster)#role

    @tosrole.command(pass_context=True)
    async def Vampire(self, ctx):
        """Applies the Vampire role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        vamp = discord.Role(id='291746016418594827', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Vampire.')#chat message
        await self.store_currentrole(ctx, ncRole, vamp)
        await self.bot.add_roles(author, ncRole)#roleclass
        await self.bot.add_roles(author, vamp)#role

    @tosrole.command(pass_context=True)
    async def Baker(self, ctx):
        """Applies the Baker role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        baker = discord.Role(id='288682060414058516', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Baker.')#chat message
        await self.store_currentrole(ctx, ncRole, baker)
        await self.bot.add_roles(author, ncRole)#roleclass
        await self.bot.add_roles(author, baker)#role

    @tosrole.command(pass_context=True)
    async def Pirate(self, ctx):
        """Applies the Baker role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        pirate = discord.Role(id='321785635956588544', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Pirate.')#chat message
        await self.store_currentrole(ctx, ncRole, pirate)
        await self.bot.add_roles(author, ncRole)#roleclass
        await self.bot.add_roles(author, pirate)#rol

    @tosrole.command(pass_context=True)
    async def Plaguebearer(self, ctx):
        """Applies the Baker role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        plaugebearer = discord.Role(id='321786136974458921', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Plaguebearer.')#chat message
        await self.store_currentrole(ctx, ncRole, plaugebearer)
        await self.bot.add_roles(author, ncRole)#roleclass
        await self.bot.add_roles(author, plaugebearer)#role

    @tosrole.command(pass_context=True)
    async def Pestilence(self, ctx):
        """Applies the Baker role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        pest = discord.Role(id='326914120576270347', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Pestilence.')#chat message
        await self.store_currentrole(ctx, ncRole, pest)
        await self.bot.add_roles(author, ncRole)#roleclass
        await self.bot.add_roles(author, pest)#role

    @tosrole.command(pass_context=True)
    async def Juggernaut(self, ctx):
        """Applies the Baker role."""#description

        channel = ctx.message.channel
        channelid = str(channel.id)
        jugg = discord.Role(id='326914566263013386', server='288455332173316106')

        if channelid in ['288463362357067777', '288455332173316106', '296069608216068098']:
            pass
        else:
            pass
            return
        
        author = ctx.message.author

        if author.id in self.db:
            await self._remove_roles(ctx)

        await self.bot.say('<@' + ctx.message.author.id + '> **||** Your role has been changed to Juggernaut.')#chat message
        await self.store_currentrole(ctx, nkRole, jugg)
        await self.bot.add_roles(author, nkRole)#roleclass
        await self.bot.add_roles(author, jugg)#role

    

    

    def save(self):
        dataIO.save_json("data/selftosroles/roles.json", self.db)


def check_folders():
    if not os.path.exists("data/selftosroles"):
        print("Creating data/selftosroles folder...")
        os.makedirs("data/selftosroles")

def check_files():
    if not dataIO.is_valid_json("data/hosting/selftosroles/roles.json"):
        print("Creating emptydata/hosting/selftosroles/roles.json...")
        dataIO.save_json("data/hosting/selftosroles/roles.json", {})

def setup(bot):
    n = SelfToSRoles(bot)
    bot.add_cog(n)     
