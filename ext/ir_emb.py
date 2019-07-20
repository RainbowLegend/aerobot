import discord
from discord.ext import commands


class Embeds:
    """Embeds for #rules and #info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def rulesembed(self, ctx):
        """Rule loading embed"""

        # Code in here
        salem = 'https://cdn.discordapp.com/attachments/358673822100226049/466346883477143552/salem.jpg'
        embed = discord.Embed(colour=0xFDAECB)
        embed.set_author(name='Section 1: Server Rules', icon_url=salem)
        embed.add_field(name='This is an English Speaking Server.',
                        value='Users may speak in languages other than English only if using a non-English word here '
                              'and there. Otherwise, please speak only English.',
                        inline=False)
        embed.add_field(name='Do not harass other users.',
                        value='This is effective both within the server and in places including, but not limited to, '
                              'DMs, other servers, and in-game.',
                        inline=False)
        embed.add_field(name='Do not spam.',
                        value='5 messages in a Rapid Succesion will result in a mute. One lining and spam are two '
                              'different things, though.',
                        inline=False)
        embed.add_field(name='Do not use overly offensive language.',
                        value='This includes, but is not limited to, racist and discriminatory remarks, '
                              'over use of swearing, and harsh remarks directed at individuals.',
                        inline=False)
        embed.add_field(name='Do not post suspicious links or links with malicious intent.',
                        value='This includes, but is not limited to viruses, IP Trackers, or Pornographic '
                              'Images not in nsfw.',
                        inline=False)
        embed.add_field(name='Do not advertise.',
                        value='This includes, but is not limited to any other discord server, reference for personal '
                              'gain, or your own channel. Please ask a mod if you would like to post.',
                        inline=False)
        embed.add_field(name='Keep all channels on topic.',
                        value="Each channel has a reason. You will be punished if you don't use them accordingly:\n\n"


                              "-<#290849989683445761> For general talk that includes any topic allowed within rules; "
                              "memes and shitposting are not allowed.\n"

                              "-<#288677153334231040> Is for finding matches and sharing in game names.\n"

                              "-<#304800218908590090> Is for trial-reports and using the Trial Bot Commands.\n"

                              "-<#304799721464004609> Is for sharing stories about your Town of Salem experience, "
                              "good or bad.\n"

                              "-<#288455332173316106> Is where new players will be welcomed.\n"

                              "-<#425124003838033920> Is where all Not Safe For Work Content will go.\n"

                              "-<#294178185711452180> Is for random talk. Other games, memes, art, pets, anything. "
                              "Just no nsfw.\n"

                              "-<#292018256888463360> Suggestions to make the server better.\n"

                              "-<#288463362357067777> Are for bot commands.\n", inline=False)
        embed.add_field(name='Do not abuse Staff Tags.',
                        value='This includes, but is not limited to, phantom tagging, spamming staff tags, '
                              'and tagging for unnecessary reasons.',
                        inline=False)
        embed.add_field(name='Do not use alts to avoid punishment.',
                        value='If you would like to protest a punishment, using an alt (alternate account) to evade '
                              'it is not going to resolve anything. This will result in further punishment and usually '
                              'a ban.',
                        inline=False)
        embed.add_field(name='Please be courteous to everyone.',
                        value='While you do not need to like every member of this server, we would like to ask that '
                              'you are courteous to all. Treat others how you would like to be treated. If you have '
                              'any issues with other members, please DM a staff member with your concerns.',
                        inline=False)
        embed.add_field(name='Do not share the personal information of others without consent.',
                        value='While you may be alright with sharing this info about yourself, others may not want '
                              'it shared. Please be respectful of other users’ privacy.',
                        inline=False)
        await ctx.send(embed=embed)

        body = 'https://media.discordapp.net/attachments/294178185711452180/466383542520250378/body.png'
        embed = discord.Embed(colour=0xFF9900)
        embed.set_author(name='Section 2: Game Rules', icon_url=body)
        embed.add_field(name='All rules already present in Town of Salem apply to games in this server.',
                        value='This includes, but is not limited to, gamethrowing, spamming, or cheating.',
                        inline=False)
        embed.add_field(name='Do not use this server to cheat.',
                        value='Whether in the text chat or either voice chat, this server will not be used to cheat '
                              'in-game. This includes talking about ongoing games. Only info that is publicly known '
                              '(for instance, the role of an uncleaned person in the graveyard) may be shared anywhere '
                              'in the server during ongoing games. If you are unsure of what you can share, do not '
                              'share it at all.',
                        inline=False)
        embed.add_field(name='Do not intentionally leave or AFK While still alive during a game.',
                        value='While all cases will be investigated for legitimate reasons, any intentional breaks '
                              'or leaving early will be punished.',
                        inline=False)
        embed.add_field(name='Do not metagame.',
                        value='Metagaming can include, but is not limited to, asking for specific attributes, '
                              'abilities, or win conditions.',
                        inline=False)
        embed.add_field(name='Do not witch-hunt players based on who they are or names.',
                        value='This includes both targeting based on who the player actually is as well as targeting '
                              'for failure to follow name schemes. If you have problems with players, please report '
                              'them rather than target them in-game. Do not report them for not following a theme.',
                        inline=False)
        embed.add_field(name='Do not flame, insult, or harass players for plays they make in-game.',
                        value='Please try and help other players improve rather than put them down for any mistakes. '
                              'If these mistakes break rules, please contact a staff member rather than berate other '
                              'players.',
                        inline=False)
        await ctx.send(embed=embed)

        mic = 'https://media.discordapp.net/attachments/294178185711452180/466385729572831255/mic.png?width=' \
              '398&height=398'
        embed = discord.Embed(colour=0xFBF606)
        embed.set_author(name='Section 3: Voice Chat and Music Rules', icon_url=mic)
        embed.add_field(name='All in-game cheating rules apply.',
                        value='If you can not do it in text channels, you can not do it in Voice Channels.',
                        inline=False)
        embed.add_field(name='Do not remain AFK in VC for a long period of time',
                        value='If you remain defeaned for fifteen or more minutes, you will be moved to the '
                              'Jailor’s Cell (AFK Voice Chat)',
                        inline=False)
        embed.add_field(name='Keep all music to the music channel.',
                        value='There is a music channel for a reason. Keep all music to this channel, please.',
                        inline=False)
        embed.add_field(name='Do not play songs specifically to annoy others.',
                        value='This includes, but is not limited to, playing very loud songs (i.e. “ear rape”), '
                              'troll songs, meme songs, or playing songs on repeat multiple tlmes in a short amount '
                              'of time.',
                        inline=False)
        await ctx.send(embed=embed)

        gae = 'https://media.discordapp.net/attachments/288681936870703105/466390095151235072/' \
              'Untitled.png?width=400&height=300'
        embed = discord.Embed(colour=0xE60042)
        embed.set_author(name='Section 4: Moderator/Senior Moderator Rules', icon_url=gae)
        embed.add_field(name='You have been trusted with Perms. Do not abuse them.',
                        value='This includes, but is not limited to, changing roles without consent, deleting messages '
                              'that do not break rules, punishing people who do not rightfully deserve it, and so on. '
                              'Use common sense for what is and is not okay.',
                        inline=False)
        embed.add_field(name='Do not go pinning a ton of messages around the channels for no reason.',
                        value='If it is important for the channel, go ahead and pin it. A joke here and there? Go '
                              'ahead and pin it. However, do not flood the pins with useless messages.',
                        inline=False)
        embed.add_field(name='Treat EVERY member the same for punishments.',
                        value='You are here, first and foremost, to moderate the channels. Never change a punishment '
                              'simply for who the person is.',
                        inline=False)
        embed.add_field(name='Treat all of your fellow staff with respect.',
                        value='While you do not need to like all of the staff members, you need to be able to get '
                              'along and treat others with respect for any staff work to work. Treat the others how '
                              'you would like to be treated.',
                        inline=False)
        embed.add_field(name='Senior Moderators.',
                        value='Just moderators that are more trusted and have more permissons.', inline=False)
        await ctx.send(embed=embed)

        icon = ctx.message.guild.icon_url
        embed = discord.Embed(colour=0x9B0029,
                              description="**If you believe someone is breaching the rules, please "
                                          "contact staff either in a direct message or the channel it happened.**\n\n"
                                          "**If a staff member is in breach of their rules, please DM an "
                                          "Administrator.**")
        embed.set_author(name='Section 5: Final Note',
                         icon_url='https://images-ext-2.discordapp.net/external/G1VU3IuTKV8JDAoLn428_qiADS7h-'
                                  'R3gENCZdwmFQYc/http/clipart-finder.com/data/mini/accessories-text-editor.png')
        embed.set_footer(text='If you have any question about the rules, please feel free to DM a Staff Member.',
                         icon_url=icon)
        await ctx.send(embed=embed)
    
    @commands.command()
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def infoembed(self,ctx): 
        """Embeds for Information"""

        confused = "https://images-ext-1.discordapp.net/.eJwVxdsOgiAAANB_8V0dKE57q7UsJ7rM5uDNCxO8lEvQpPXvrfNyPoZ6DcbO4FJO8862xVi2bDbZW5rQasRcP19NOU3Wg0mbbRGox1WkIno252xNhb_QAizlOKy0yCZyA6DekMYb4lVx8iqIeONgRWAgY5hwAvkQ6x7FMBP_aXhBpMOadrzH3X0l-R7SAruJJgjnd5QcWxfDqxM_DopuUWD5pE3aMBUs9Mqln4FbD12lVBSw3vj-AKnwRL4.GEFDeMo9tife0f1qscOh0Ynk5V4"

        embed = discord.Embed(colour=0x27AE60)
        embed.set_author(name='Frequently Asked Questions (F.A.Q.)', icon_url=confused)
        embed.add_field(name='Why are there ToS roles? How can I get them?',
                        value='Type `/tosrole [Role name]` in <#288463362357067777>. It changes nothing except for your colour. It is purely cosmetic.', inline=False)
        embed.add_field(name='How do I get game notifications?', value="""- Type `/gnotif enable`
- To disable it, do `/gnotif disable`
- If there is a game, you will get pinged for it.
- Tell the host your username.""", inline=False)
        embed.add_field(name='What is Tatsumaki?', value="""**Tatsumaki is a Discord Bot with all kinds of features, including profile pages, reputation points, and top people in the server. Please do `t!help` in <#288463362357067777> to learn more.**
- Some fun commands include `t!fish` and `t!slots`
- `t!rep` is a command to give a "rep" point to someone. This is just purely a number, it does nothing more.
- `t!daily` is a command to get 200 free credits each day. Or you can give someone else credits by tagging them at the end.
- `t!credits` shows you your credit balance.""", inline=False)
        embed.add_field(name='What is the Muted role?', value="When someone has the Muted role, they can not talk anywhere. The reason they have the role is most likely because they spammed, flamed, etc. (basically they broke a rule)", inline=False)
        embed.add_field(name='How do I report someone?', value="""- Direct Message (DM) a Moderator or Administrator.
- To direct message one, click on their name and type in the "Message @[name]" box.""", inline=False)
        embed.add_field(name='Is there anything else I should know?', value="""Yes. By staying in this server you agree to the fact that we collect your end user data (basically the messages you send).
We collect this to make your experience better, and in the case of possibly deleted messages with offensive content, we can better trace it.""")
        embed.add_field(name='How can I invite a friend?', value='If you want to invite a friend, send them this discord link: https://discord.gg/kDkxMQ9')

        await self.bot.say(embed=embed)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def infolinks(self, ctx):
        """Second"""

        servericon = 'https://images-ext-2.discordapp.net/.eJwNxl9TgjAAAPDvwkNvgxwUzruuW_wxwWZAqPnicQzYhGhuQ9Cu716_p9-PMcjOWBhMa6EWlsW_iqZSoJo0mJmUq_Jb0kIIs6-0ZVbRSK5hsGmu-A0Tzy3xy3nnpGc1jEpITBwnWwEUOvRYAht2AMJoOUe9DdtPfCoGMuz6g9NlclbHoVxudeLFg_vQRvhGHl1_SiLAMhqRfXmO8-MaTV4wsTbGlw2qbQXy0_vBD_Z-DXmKhAnTV7pFecPYuKKBcG8fNpAez9Q6eR451expfn_HKt4w_T_j9w-p4E0N.N4BSDi3wRU9I4JQI9vvWg_rO3oo'
        witch = 'https://images-ext-2.discordapp.net/.eJwNyDsOgzAMANC7ZCdO-FVCqjhG5zQywSLYiLgwVNwd3vj-5rdnM5hZdRsADkqMqujtSQsFyxJFFkL7LKicXMlUlZBxBVpDwgII2MOHNM524wQ7HlRIGHJQLDrG77t2vnUv37uma7rWXDdUQyd6.2qJdJ7hOx0fCYiIFYZwJuYW5JEQ'
        embed = discord.Embed(colour=0xBF5FFF)
        embed.set_author(name='Some important links related to Town of Salem', icon_url=witch)
        embed.add_field(name='ToS Browser', value='http://www.blankmediagames.com/TownOfSalem/', inline=False)
        embed.add_field(name='ToS on Steam', value='http://store.steampowered.com/app/334230/', inline=False)
        embed.add_field(name='Official Forums', value='https://www.blankmediagames.com/phpbb/', inline=False)
        embed.add_field(name='Unofficial Subreddit', value='https://www.reddit.com/r/TownofSalemgame/', inline=False)
        embed.add_field(name='Trial System', value='http://blankmediagames.com/Trial/', inline=False)
        embed.add_field(name='PTR (Public Test Realm)', value='http://www.blankmediagames.com/TownOfSalem/PublicTestRealm/', inline=False)
        embed.set_footer(text='If there are any links you feel should be added to this list, DM an Administrator.', icon_url=servericon)

        await self.bot.say(embed=embed)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def infostafflist(self, ctx):
        """Third"""

        icon = ctx.message.server.icon_url
        embed = discord.Embed(colour=0xCFFF63)
        embed.add_field(name='Administrators', value="""- <@222147236728012800>
- <@167736120400936960>
- <@333621621116108800>""", inline=False)
        embed.add_field(name='Senior Moderators', value="""- <@298166754331459586>
- <@332715657437118485>
- <@267723762563022849>
- <@189125691504066561>""", inline=False)
        embed.add_field(name='Moderators', value="""- <@155507643115503617>
- <@326913617503059978>
- <@350698340096409602>
- <@110362755390771200>
- <@321759261925441538>
- <@316671807052578827>""", inline=False)
        embed.set_author(name='Staff List', icon_url=icon)

        await self.bot.say(embed=embed)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def infostaff(self, ctx):
        """Fourth"""

        spy = 'https://images-ext-2.discordapp.net/.eJwNyFEKgzAMANC79N9mretAQTyEJ-gk64I1KTYqMnb37X2-j9m3bHrzVi09wEGJURXv9qSFomWZRRZC-19QObmRV1NjxhVojQkrtNA-YCqXLZxgw4MqCUOOilXH-Tn4mwvO-c51IXhvvj_u-yZa.VyMAY7O3cPIU09jtrPQ4X92HbrQ'
        embed = discord.Embed(colour=0x5DADE2)
        embed.set_author(name='What can the staff roles do?', icon_url=spy)
        embed.add_field(name='What are Game Moderators?', value="""- As the name suggests, Game Moderators are players who frequently play Town of Salem and have knowledge of what's breaking the rules and what's not.
- When a report on Discord concerning a broken in-game rule, the Game Moderators will handle it.
- Game Moderators are in most games and can take action immediately.
- Game Moderators have the power to manage the messages in ToS related channels. This includes pinning and deleting messages. They can also block you from the ToS related channels.""", inline=False)
        embed.add_field(name='What are Moderators?', value="""- Moderators can be considered as Semi-Administrators. They help moderate the games as well as moderate the server.
- Moderators have the power to manage messages in every channel.
- Moderators can kick or ban users, force nicknames if the user's name is offensive, block you from any channel, mute you, and assign roles. They also have perms in the voice chats.""", inline=False)
        embed.add_field(name='What are Administrators?', value="""- Administrators run the server and keep everything together. This role has the most power.
- Administrators can do EVERYTHING. They have every permission.
- Administrators will oversee the entire server and make the important decisions.""", inline=False)
        embed.set_footer(text='If you think any Staff Member is abusing their permissions or not doing a good job, DM an Administrator immediately. If the person you have concerns about is an Administrator, DM the Owner, Anna <3#4007', icon_url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def inforolestown(self, ctx):
        """Fifth"""

        servericon = ctx.message.server.icon_url
        mayor = 'https://images-ext-1.discordapp.net/.eJwNyMEOgjAMANB_2Z11qx6QxJh45yMGKbNhtIRViDH-u7zj-7r3VlznXmZrB7BzFjIj9AfPnLzoqDoz-XPB9JBGp6amQgvwkjJVaKEdoFehzzNlv0qGjXaurAIlGVV7jMMdQ7zGgDfEiOHifn_IoihU.OugSQlTAgY1a15a8FYg1qTutY5I'
        godfather = 'https://images-ext-1.discordapp.net/.eJwVyMEOgjAMANB_2Z0VFqJCYjzyGaZiGQ2jJVuFg_Hf1bzbe7tXTq53s9nWA-wchcyo9QcvjF50VF2Y_G_B9JBKp6pgohV4xUgFOujOMOhzQpsp34PfJEKmnQurQEKjYrfxcQ11c6r_2nBpgvt8AUJHKUk.dbMZvDxsrwMlCW7kqEQhT8ZJb24'
        executioner = 'https://images-ext-2.discordapp.net/.eJwNyMEOgjAMANB_2Z2VTgkJifHuX1RSZ8NoyVbgYPx3fcf3CXstYQpv920COCQruzPGUxahqDabLcLxv-B2amevrlHhFWSlzA1GGBkeJMVq3DRD5UOamEIh5-b3-XlLPQ7YJ0zpesEhfH91Byej.TceIIgMCxo7EAw_kWDBKZY7Sy_A'
        coven = 'https://vignette4.wikia.nocookie.net/town-of-salem/images/3/3c/CovenIcon.png/revision/latest?cb=20170601055927'
        

        embed = discord.Embed(colour=0x45BF00)
        embed.set_author(name='List of Town Roles', icon_url=mayor)
        embed.add_field(name='Town Killing', value="""- Jailor
- Veteran
- Vigilante
- VampireHunter""", inline=False)
        embed.add_field(name='Town Investigative', value="""- Investigator
- Lookout
- Sheriff
- Spy
- Psychic
- Tracker""", inline=False)
        embed.add_field(name='Town Support', value="""- Escort
- Mayor
- Medium
- Retributionist
- Transporter""", inline=False)
        embed.add_field(name='Town Protective', value="""- Doctor
- BodyGuard
- Crusader
- Trapper""", inline=False)
        embed.set_footer(text='Use `/tosrole [role]` to get a role!', icon_url=servericon)

        await self.bot.send_message(ctx.message.channel, embed=embed)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def inforolesmaf(self, ctx):
        """sixth"""

        servericon = ctx.message.server.icon_url
        mayor = 'https://images-ext-1.discordapp.net/.eJwNyMEOgjAMANB_2Z11qx6QxJh45yMGKbNhtIRViDH-u7zj-7r3VlznXmZrB7BzFjIj9AfPnLzoqDoz-XPB9JBGp6amQgvwkjJVaKEdoFehzzNlv0qGjXaurAIlGVV7jMMdQ7zGgDfEiOHifn_IoihU.OugSQlTAgY1a15a8FYg1qTutY5I'
        godfather = 'https://images-ext-1.discordapp.net/.eJwVyMEOgjAMANB_2Z0VFqJCYjzyGaZiGQ2jJVuFg_Hf1bzbe7tXTq53s9nWA-wchcyo9QcvjF50VF2Y_G_B9JBKp6pgohV4xUgFOujOMOhzQpsp34PfJEKmnQurQEKjYrfxcQ11c6r_2nBpgvt8AUJHKUk.dbMZvDxsrwMlCW7kqEQhT8ZJb24'
        executioner = 'https://images-ext-2.discordapp.net/.eJwNyMEOgjAMANB_2Z2VTgkJifHuX1RSZ8NoyVbgYPx3fcf3CXstYQpv920COCQruzPGUxahqDabLcLxv-B2amevrlHhFWSlzA1GGBkeJMVq3DRD5UOamEIh5-b3-XlLPQ7YJ0zpesEhfH91Byej.TceIIgMCxo7EAw_kWDBKZY7Sy_A'
        coven = 'https://vignette4.wikia.nocookie.net/town-of-salem/images/3/3c/CovenIcon.png/revision/latest?cb=20170601055927'

        mafia = discord.Embed(colour=0xA00000)
        mafia.set_author(name='List of Mafia Roles', icon_url=godfather)
        mafia.add_field(name='Mafia Killing', value="""- Godfather
- Mafioso
- Ambusher""", inline=False)
        mafia.add_field(name='Mafia Support', value="""- Blackmailer
- Consigliere
- Consort""", inline=False)
        mafia.add_field(name='Mafia Deception', value="""- Disguiser
- Forger
- Framer
- Janitor
- Hypnotist""", inline=False)
        mafia.set_footer(text='Use `/tosrole [role]` to get a role!', icon_url=servericon)
        await self.bot.say(embed=mafia)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def inforolesne(self, ctx):
        """seventh"""

        servericon = ctx.message.server.icon_url
        mayor = 'https://images-ext-1.discordapp.net/.eJwNyMEOgjAMANB_2Z11qx6QxJh45yMGKbNhtIRViDH-u7zj-7r3VlznXmZrB7BzFjIj9AfPnLzoqDoz-XPB9JBGp6amQgvwkjJVaKEdoFehzzNlv0qGjXaurAIlGVV7jMMdQ7zGgDfEiOHifn_IoihU.OugSQlTAgY1a15a8FYg1qTutY5I'
        godfather = 'https://images-ext-1.discordapp.net/.eJwVyMEOgjAMANB_2Z0VFqJCYjzyGaZiGQ2jJVuFg_Hf1bzbe7tXTq53s9nWA-wchcyo9QcvjF50VF2Y_G_B9JBKp6pgohV4xUgFOujOMOhzQpsp34PfJEKmnQurQEKjYrfxcQ11c6r_2nBpgvt8AUJHKUk.dbMZvDxsrwMlCW7kqEQhT8ZJb24'
        executioner = 'https://images-ext-2.discordapp.net/.eJwNyMEOgjAMANB_2Z2VTgkJifHuX1RSZ8NoyVbgYPx3fcf3CXstYQpv920COCQruzPGUxahqDabLcLxv-B2amevrlHhFWSlzA1GGBkeJMVq3DRD5UOamEIh5-b3-XlLPQ7YJ0zpesEhfH91Byej.TceIIgMCxo7EAw_kWDBKZY7Sy_A'
        coven = 'https://vignette4.wikia.nocookie.net/town-of-salem/images/3/3c/CovenIcon.png/revision/latest?cb=20170601055927'

        ne = discord.Embed(colour=0xACACAC)
        ne.set_author(name='List of Neutral Roles', icon_url=executioner)
        ne.add_field(name='Neutral Killing', value="""- Arsonist
- SerialKiller
- Werewolf
- Juggernaut""", inline=False)
        ne.add_field(name='Neutral Evil', value="""- Executioner
- Jester
- Witch""", inline=False)
        ne.add_field(name='Neutral Benign', value="""- Amnesiac
- Survivor
- GuardianAngel""", inline=False)
        ne.add_field(name='Neutral Chaos', value="""
- Vampire
- Pirate
- Plaguebearer
- Pestilence
- Baker""", inline=False)
        ne.set_footer(text='Use `/tosrole [role]` to get a role!', icon_url=servericon)

        await self.bot.say(embed=ne)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def inforolescoven(self, ctx):
        """8th"""

        servericon = ctx.message.server.icon_url
        mayor = 'https://images-ext-1.discordapp.net/.eJwNyMEOgjAMANB_2Z11qx6QxJh45yMGKbNhtIRViDH-u7zj-7r3VlznXmZrB7BzFjIj9AfPnLzoqDoz-XPB9JBGp6amQgvwkjJVaKEdoFehzzNlv0qGjXaurAIlGVV7jMMdQ7zGgDfEiOHifn_IoihU.OugSQlTAgY1a15a8FYg1qTutY5I'
        godfather = 'https://images-ext-1.discordapp.net/.eJwVyMEOgjAMANB_2Z0VFqJCYjzyGaZiGQ2jJVuFg_Hf1bzbe7tXTq53s9nWA-wchcyo9QcvjF50VF2Y_G_B9JBKp6pgohV4xUgFOujOMOhzQpsp34PfJEKmnQurQEKjYrfxcQ11c6r_2nBpgvt8AUJHKUk.dbMZvDxsrwMlCW7kqEQhT8ZJb24'
        executioner = 'https://images-ext-2.discordapp.net/.eJwNyMEOgjAMANB_2Z2VTgkJifHuX1RSZ8NoyVbgYPx3fcf3CXstYQpv920COCQruzPGUxahqDabLcLxv-B2amevrlHhFWSlzA1GGBkeJMVq3DRD5UOamEIh5-b3-XlLPQ7YJ0zpesEhfH91Byej.TceIIgMCxo7EAw_kWDBKZY7Sy_A'
        witch = 'https://vignette4.wikia.nocookie.net/town-of-salem/images/3/3c/CovenIcon.png/revision/latest?cb=20170601055927'

        coven = discord.Embed(colour=0xBF5FFF)
        coven.set_author(name='List of Coven Roles', icon_url=witch)
        coven.add_field(name='Coven Evil', value="""- Coven Leader
- HexMaster
- Medusa
- Necromancer
- Poisoner
- PotionMaster""", inline=False)
        coven.set_footer(text='Use `/tosrole [role]` to get a role!', icon_url=servericon)

        await self.bot.say(embed=coven)


def setup(bot):
    bot.add_cog(Embeds(bot))
