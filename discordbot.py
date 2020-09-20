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
