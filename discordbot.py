"""from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix="$")
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
        
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def pong(ctx):
    await ctx.send("ping")


bot.run(token)
"""

import os
import traceback

from discord.ext import commands


INITIAL_EXTENSIONS = [
    "cogs.commandcog"
]


class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)
        for cog in INITIAL_EXTENSIONS:
            try: self.load_extension(cog)
            except Exception: traceback.print_exc()


if __name__ == "__main__":
    bot = MyBot(command_prefix="$")
    bot.run(os.environ["DISCORD_BOT_TOKEN"])
