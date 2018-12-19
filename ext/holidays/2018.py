"""
MystLegend 2018
This cog is for use as-is. No guarantee will be provided it works.
This cog will be deprecated 05JAN2019.
"""
import discord
from discord.ext import commands
import random


class Holidays2018:
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def holidaylist(self, ctx):
        """Naughty or nice?
        
        1/10 chance of being an elf
        3/10 chance of being nice
        6/10 chance of being a bad boye."""
        elf = discord.utils.get(ctx.guild.roles, name="Elf")
        nice_list = discord.utils.get(ctx.guild.roles, name="Nice List")
        naughty_list = discord.utils.get(ctx.guild.roles, name="Naughty List)
        
        if any(r.id in (elf.id, nice_list.id, naughty_list.id) for r in ctx.author.roles):
            return await ctx.send("You already have a Christmas role!")
        
        chance = random.randint(1, 10)
        
        if chance == 1:
            await ctx.author.add_roles(elf, reason="A true good boy. (Holidays 2018)")
            return await ctx.send("**Superb luck you have!** You are an *elf*.")
        elif chance in (2, 3, 4):
            await ctx.author.add_roles(nice_list, reason='You\'ve been alright, I guess. (Holidays 2018)')
            return await ctx.send("**What a respectable young fellow!** Have a spot on my *nice list*.")
        elif chance in (5, 6, 7, 8, 9, 10):
            await ctx.author.add_roles(naughty_list, reason='A bad man. (Holidays 2018)')
            return await ctx.send("**Oh I can already see the coal!** Repent on your sins and sit down on my *naughty list*.")


def setup(bot):
    bot.load_extension(Holidays2018(bot))
