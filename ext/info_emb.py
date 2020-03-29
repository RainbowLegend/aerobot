# update 9June18 - Changed names of Staff -elijah
import discord
from discord.ext import commands
import asyncio
import logging
import logging.handlers
import random
import os
import datetime
import re
from datetime import datetime

class InfoLoader(commands.Cog):
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
        embed.add_field(name='How do I get Game / Hunger Games notifications?', value="""- Head over to <#693659198290001960>, and react with the corresponding roles.
- To disable them, you simply remove your reaction.
- If there is a game aligned with the role, you will be pinged.
- Tell the host your username if using Gamenights.""", inline=False)
        embed.add_field(name='What is the Muted role?', value="When someone has the Muted role, they can not talk anywhere. The reason they have the role is most likely because they spammed, flamed, etc. (basically they broke a rule)", inline=False)
        embed.add_field(name='How do I report someone?', value="""- Direct Message (DM) a Moderator or Administrator.
- To direct message one, click on their name and type in the "Message @[name]" box.""", inline=False)
        embed.add_field(name='Is there anything else I should know?', value="""Yes. By staying in this server you agree to the fact that we collect your end user data (basically the messages you send).
We collect this to make your experience better, and in the case of possibly deleted messages with offensive content, we can better trace it.""")
        embed.add_field(name='How can I invite a friend?', value='If you want to invite a friend, send them this discord link: https://discord.gg/hunmV9')

        await ctx.send(embed=embed)



        # servericon = ctx.guild.icon_url
        # witch = 'https://images-ext-2.discordapp.net/.eJwNyDsOgzAMANC7ZCdO-FVCqjhG5zQywSLYiLgwVNwd3vj-5rdnM5hZdRsADkqMqujtSQsFyxJFFkL7LKicXMlUlZBxBVpDwgII2MOHNM524wQ7HlRIGHJQLDrG77t2vnUv37uma7rWXDdUQyd6.2qJdJ7hOx0fCYiIFYZwJuYW5JEQ'
        # embed = discord.Embed(colour=0xBF5FFF)
        # embed.set_author(name='Some important links related to Town of Salem', icon_url=witch)
        # embed.add_field(name='ToS Browser', value='http://www.blankmediagames.com/TownOfSalem/', inline=False)
        # embed.add_field(name='ToS on Steam', value='http://store.steampowered.com/app/334230/', inline=False)
        # embed.add_field(name='Official Forums', value='https://www.blankmediagames.com/phpbb/', inline=False)
        # embed.add_field(name='Unofficial Subreddit', value='https://www.reddit.com/r/TownofSalemgame/', inline=False)
        # embed.add_field(name='Trial System', value='http://blankmediagames.com/Trial/', inline=False)
        # embed.add_field(name='PTR (Public Test Realm)', value='http://www.blankmediagames.com/TownOfSalem/PublicTestRealm/', inline=False)
        # embed.set_footer(text='If there are any links you feel should be added to this list, DM an Administrator.', icon_url=servericon)

        # await ctx.send(embed=embed)
        
        
        
        # icon = ctx.guild.icon_url
        # embed = discord.Embed(colour=0xCFFF63)
        # embed.add_field(name='Owner',value="""- <@222147236728012800>""", inline=False)
        # embed.add_field(name='Administrators', value="""- <@321759261925441538>
# - <@167736120400936960>""", inline=False)
        # embed.add_field(name='Senior Moderators', value="""- <@221764425483288576>
# - <@652485289675194389>
# - <@155507643115503617>""", inline=False)
        # embed.add_field(name='Moderators', value="""- <@347120208722395148>
# - <@397013342495047680>
# - <@96801273969414144>
# - <@201913365377843200>""", inline=False)
        # embed.add_field(name='ToS Global Moderators', value="""- <@224737113210355712>""", inline=False)
        # embed.set_author(name='Staff List', icon_url=icon)

        # await ctx.send(embed=embed)



        # spy = 'https://images-ext-2.discordapp.net/.eJwNyFEKgzAMANC79N9mretAQTyEJ-gk64I1KTYqMnb37X2-j9m3bHrzVi09wEGJURXv9qSFomWZRRZC-19QObmRV1NjxhVojQkrtNA-YCqXLZxgw4MqCUOOilXH-Tn4mwvO-c51IXhvvj_u-yZa.VyMAY7O3cPIU09jtrPQ4X92HbrQ'
        # embed = discord.Embed(colour=0x5DADE2)
        # embed.set_author(name='What can the staff roles do?', icon_url=spy)
        # embed.add_field(name='What can Former Staff do?', value="""- It really cant do anything, it's just former staff. Some are given special perms depending
# on who they are, but besides that nothing. Take a current listed staff's word over everything.""")
        # embed.add_field(name='What are Moderators?', value="""- As the name suggests, Moderators are people who moderate the server, but at a lower end.
# - Moderators can delete messages, hand out punishments, create roles, etc.
# - Moderators will be in most gamenights and will be there to make sure it follows rules.
# - Moderators have the power to manage the messages in channels. This includes pinning and deleting messages. They can also block you from channels.""", inline=False)
        # embed.add_field(name='What are Senior Moderators?', value="""- Senior Moderators can be considered as Semi-Administrators. They help moderate the games as well as moderate the server.
# - Senior Moderators have every permisson Moderators have.
# - Moderators can kick or ban users aswell, but can also force nicknames if the user's name is offensive, block you from any channel, mute you, and assign roles. They also have perms in the voice chats.""", inline=False)
        # embed.add_field(name='What are Administrators?', value="""- Administrators run the server and keep everything together. This role has the most power.
# - Administrators can do EVERYTHING. They have every permission.
# - Administrators will oversee the entire server and make the important decisions.""", inline=False)
        # embed.set_footer(text='If you think any Staff Member is abusing their permissions or not doing a good job, DM an Administrator immediately. If the person you have concerns about is an Administrator, DM the Owner, henlo.', icon_url=ctx.message.server.icon_url)
        # await ctx.send(embed=embed)



        servericon = ctx.guild.icon_url
        mayor = 'https://images-ext-1.discordapp.net/.eJwNyMEOgjAMANB_2Z11qx6QxJh45yMGKbNhtIRViDH-u7zj-7r3VlznXmZrB7BzFjIj9AfPnLzoqDoz-XPB9JBGp6amQgvwkjJVaKEdoFehzzNlv0qGjXaurAIlGVV7jMMdQ7zGgDfEiOHifn_IoihU.OugSQlTAgY1a15a8FYg1qTutY5I'
        godfather = 'https://images-ext-1.discordapp.net/.eJwVyMEOgjAMANB_2Z0VFqJCYjzyGaZiGQ2jJVuFg_Hf1bzbe7tXTq53s9nWA-wchcyo9QcvjF50VF2Y_G_B9JBKp6pgohV4xUgFOujOMOhzQpsp34PfJEKmnQurQEKjYrfxcQ11c6r_2nBpgvt8AUJHKUk.dbMZvDxsrwMlCW7kqEQhT8ZJb24'
        executioner = 'https://images-ext-2.discordapp.net/.eJwNyMEOgjAMANB_2Z2VTgkJifHuX1RSZ8NoyVbgYPx3fcf3CXstYQpv920COCQruzPGUxahqDabLcLxv-B2amevrlHhFWSlzA1GGBkeJMVq3DRD5UOamEIh5-b3-XlLPQ7YJ0zpesEhfH91Byej.TceIIgMCxo7EAw_kWDBKZY7Sy_A'
        witch = 'https://vignette4.wikia.nocookie.net/town-of-salem/images/3/3c/CovenIcon.png/revision/latest?cb=20170601055927'
        

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

        await ctx.send(embed=embed)



        servericon = ctx.guild.icon_url
        mayor = 'https://images-ext-1.discordapp.net/.eJwNyMEOgjAMANB_2Z11qx6QxJh45yMGKbNhtIRViDH-u7zj-7r3VlznXmZrB7BzFjIj9AfPnLzoqDoz-XPB9JBGp6amQgvwkjJVaKEdoFehzzNlv0qGjXaurAIlGVV7jMMdQ7zGgDfEiOHifn_IoihU.OugSQlTAgY1a15a8FYg1qTutY5I'
        godfather = 'https://images-ext-1.discordapp.net/.eJwVyMEOgjAMANB_2Z0VFqJCYjzyGaZiGQ2jJVuFg_Hf1bzbe7tXTq53s9nWA-wchcyo9QcvjF50VF2Y_G_B9JBKp6pgohV4xUgFOujOMOhzQpsp34PfJEKmnQurQEKjYrfxcQ11c6r_2nBpgvt8AUJHKUk.dbMZvDxsrwMlCW7kqEQhT8ZJb24'
        executioner = 'https://images-ext-2.discordapp.net/.eJwNyMEOgjAMANB_2Z2VTgkJifHuX1RSZ8NoyVbgYPx3fcf3CXstYQpv920COCQruzPGUxahqDabLcLxv-B2amevrlHhFWSlzA1GGBkeJMVq3DRD5UOamEIh5-b3-XlLPQ7YJ0zpesEhfH91Byej.TceIIgMCxo7EAw_kWDBKZY7Sy_A'
        witch = 'https://vignette4.wikia.nocookie.net/town-of-salem/images/3/3c/CovenIcon.png/revision/latest?cb=20170601055927'

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
        await ctx.send(embed=mafia)



        servericon = ctx.message.server.icon_url
        mayor = 'https://images-ext-1.discordapp.net/.eJwNyMEOgjAMANB_2Z11qx6QxJh45yMGKbNhtIRViDH-u7zj-7r3VlznXmZrB7BzFjIj9AfPnLzoqDoz-XPB9JBGp6amQgvwkjJVaKEdoFehzzNlv0qGjXaurAIlGVV7jMMdQ7zGgDfEiOHifn_IoihU.OugSQlTAgY1a15a8FYg1qTutY5I'
        godfather = 'https://images-ext-1.discordapp.net/.eJwVyMEOgjAMANB_2Z0VFqJCYjzyGaZiGQ2jJVuFg_Hf1bzbe7tXTq53s9nWA-wchcyo9QcvjF50VF2Y_G_B9JBKp6pgohV4xUgFOujOMOhzQpsp34PfJEKmnQurQEKjYrfxcQ11c6r_2nBpgvt8AUJHKUk.dbMZvDxsrwMlCW7kqEQhT8ZJb24'
        executioner = 'https://images-ext-2.discordapp.net/.eJwNyMEOgjAMANB_2Z2VTgkJifHuX1RSZ8NoyVbgYPx3fcf3CXstYQpv920COCQruzPGUxahqDabLcLxv-B2amevrlHhFWSlzA1GGBkeJMVq3DRD5UOamEIh5-b3-XlLPQ7YJ0zpesEhfH91Byej.TceIIgMCxo7EAw_kWDBKZY7Sy_A'
        witch = 'https://vignette4.wikia.nocookie.net/town-of-salem/images/3/3c/CovenIcon.png/revision/latest?cb=20170601055927'

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
        await ctx.send(embed=ne)



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
        await ctx.send(embed=coven)


def setup(bot):
    bot.add_cog(InfoLoader(bot))
