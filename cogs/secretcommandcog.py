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
        type = random.randint(0, 2)
        if type == 0: await ctx.message.add_reaction(random.choice(emoji))
        elif type == 1: await ctx.send(random.choice(emoji))
        else: await ctx.send(random.choice([
            "ぴえん",
            "ぱおん"
        ]))
    #-----------


def setup(bot):
    bot.add_cog(SecretCommandCog(bot))
