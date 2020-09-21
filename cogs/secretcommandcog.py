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
        type = random.randint(0, 2)
        if type == 0: await ctx.message.add_reaction("\U0001F97A")
        elif type == 1: await ctx.send("\U0001F97A")
        else: await ctx.send("ぱおん")
    #-----------


def setup(bot):
    bot.add_cog(SecretCommandCog(bot))
