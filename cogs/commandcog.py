from discord.ext import commands


class CommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self,ctx):
        await ctx.send("pong")

    @commands.command()
    async def pien(self,ctx):
        await ctx.send("ぱおん")


def setup(bot):
    bot.add_cog(CommandCog(bot))
