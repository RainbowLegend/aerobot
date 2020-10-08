import uuid
import json
from discord.ext import commands


class FormValidator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="contestvote")
    async def form_validation(self, ctx):
        FORM_LINK = "https://docs.google.com/forms/d/e/1FAIpQLSeNjEFFuXI2k4-K1Bn6r4dvjxElxiML3Gt-KnbZmvHV6jpGjQ/" \
                    "viewform?entry.1763648885="
        author = ctx.author
        with open("forms.json", "r") as f:
            db = json.load(f)
        if author.id in db.keys():
            return await ctx.author.send(f"You have already requested a form link!\n"
                                         f"Identifier: `{db[author.id]}`\n"
                                         f"Link: {FORM_LINK}{db[author.id]}/")
        uid = uuid.uuid4()
        db[author.id] = uid
        with open("forms.json", "w") as f:
            json.dump(db, f)
        return await ctx.author.send(f"Identifier: `{uid}`\n"
                                     f"Link: {FORM_LINK}{uid}/")


def setup(bot):
    bot.add_cog(FormValidator(bot))
