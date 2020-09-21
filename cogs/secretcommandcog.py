import random

from discord.ext import commands

from modules import bot_ext


be = bot_ext.BotExt()


class SecretCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # pien -----
    @commands.command()
    async def pien(self, ctx):
        emoji = [
            "\U0001F97A",
            "\U0001F418"
        ]
        type = random.randint(0, 3)
        if type == 0: await ctx.message.add_reaction(random.choice(emoji))
        elif type == 1: await ctx.send(random.choice(emoji))
        elif type == 2:
            for e in random.choice([
                ["\U0001F1F5", "\U0001F1EE", "\U0001F1EA", "\U0001F1F3"],
                ["\U0001F1F5", "\U0001F1E6", "\U0001F1F4", "\U0001F1F3"]
             ]): await ctx.message.add_reaction(e)
        else: await ctx.send(random.choice([
            "ぴえん",
            "ぱおん"
        ]))
    #-----------


def setup(bot):
    bot.add_cog(SecretCommandCog(bot))
