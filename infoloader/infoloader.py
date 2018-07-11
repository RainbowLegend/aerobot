# update 9June18 - Changed names of Staff -elijah
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

class InfoLoader:
    """Loads up the #info"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def infofaq(self, ctx):
        """lol"""

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
        """lol v2?"""

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
        """lolv2.5"""

        icon = ctx.message.server.icon_url
        embed = discord.Embed(colour=0xCFFF63)
        embed.add_field(name='Administrators', value="""- <@298166754331459586>
- <@222147236728012800>
- <@167736120400936960>
- <@333621621116108800>""", inline=False)
        embed.add_field(name='Senior Moderators', value="""- <@231785539370614784>
- <@267723762563022849>
- <@235542999063461888> 
- <@182942393371197440>
- <@189125691504066561>""", inline=False)
        embed.add_field(name='Moderators', value="""- <@233753965353893898>
- <@179645538533244929>
- <@155507643115503617>
- <@228700305263558656>
- <@70221374404173824>
- <@321759261925441538>""", inline=False)
        embed.add_field(name='ToS Global Moderators', value="""- <@224737113210355712>""", inline=False)
        embed.set_author(name='Staff List', icon_url=icon)

        await self.bot.say(embed=embed)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def infostaff(self, ctx):
        """lol v3!"""

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
        embed.set_footer(text='If you think any Staff Member is abusing their permissions or not doing a good job, DM an Administrator immediately. If the person you have concerns about is an Administrator, DM the Owner, henlo.', icon_url=ctx.message.server.icon_url)
        await self.bot.say(embed=embed)

    @commands.command(no_pm=True, pass_context=True)
    @commands.has_any_role("Administrator", "AeroBot Manager")
    async def inforolestown(self, ctx):
        """lol v4!"""

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
        """lol v4!"""

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
        """lol v4!"""

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
        """lol v4!"""

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
    bot.add_cog(InfoLoader(bot))
