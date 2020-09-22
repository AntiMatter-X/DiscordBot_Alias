import random

from discord.ext import commands

from modules import bot_ext


be = bot_ext.BotExt()


class SecretCommandCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # pien -----
    @commands.command(aliases=["paon"])
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
            "ぱおん",
            "https://www.youtube.com/watch?v=U1hdYYosOYc",
            "https://www.youtube.com/watch?v=MDWYEdNox1g",
            "https://www.youtube.com/watch?v=iJ-H3gx2P9Y",
            "https://www.youtube.com/watch?v=jat2xxVaz_U",
            "https://www.youtube.com/watch?v=7l4xJbSA5Jg",
            "https://www.youtube.com/watch?v=TTn4WzxRoyw"
        ]))
    #-----------

    # cat -----
    @commands.command()
    async def cat(self, ctx):
        type = random.randint(0, 1)
        if type == 0: await ctx.send("\U0001F431")
        else: await ctx.send(random.choice([
            "にゃーん",
            "\U0001F431",
            "https://f.easyuploader.app/eu-prd/upload/20200922112534_505462776f304c4b7741.gif",
            "https://www.youtube.com/watch?v=wPizs7AqRkE"
        ]))
    #----------


def setup(bot):
    bot.add_cog(SecretCommandCog(bot))
