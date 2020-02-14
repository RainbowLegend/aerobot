import discord
from discord.ext import commands
import random
lelijah = """
            _.._        ,------------.
         ,'      `.    ( No Dick Here!)
        /  __) __` \    `-,----------'
       (  (`-`(-')  ) _.-'
       /)  \  = /  (
      /'    |--' .  \
     (  ,---|  `-.)__`
      )(  `-.,--'   _`-.
     '/,'          (  Uu",
      (_       ,    `/,-' )
      `.__,  : `-'/  /`--'
        |     `--'  |
        `   `-._   /
         \        (
         /\ .      \.  Ojo
        / |` \     ,-\
       /  \| .)   /   \
      ( ,'|\    ,'     :
      | \,`.`--"/      }
      `,'    \  |,'    /
     / "-._   `-/      |
     "-.   "-.,'|     ;
    /        _/["---'""]
   :        /  |"-     '
   '           |      /
               `      | """


class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def penis(self, ctx, user: discord.Member=None):
        """:b:enis?"""
        if user.id == 555897749762080778:
            return await ctx.send(lelijah)
        elif user is None:
            user = ctx.author
        state = random.getstate()
        random.seed(user.id)
        random.setstate(state)
        await ctx.send(f"Size: 8{'=' * random.randint(0, 30)}D")


def setup(bot):
    bot.add_cog(Misc(bot))
