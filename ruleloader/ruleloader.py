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

      # End code here
      
def setup(bot):
    bot.add_cog(RuleLoader(bot))
