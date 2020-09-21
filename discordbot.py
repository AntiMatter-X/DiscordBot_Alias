import os
import traceback

from discord.ext import commands


INITIAL_EXTENSIONS = [
    "cogs.commandcog",
    "cogs.eventcog",
    "cogs.secretcommandcog"
]


class MyBot(commands.Bot):
    def __init__(self, command_prefix, help_command, case_insensitive):
        super().__init__(command_prefix, help_command=help_command, case_insensitive=case_insensitive)
        for cog in INITIAL_EXTENSIONS:
            try: self.load_extension(cog)
            except Exception: traceback.print_exc()


if __name__ == "__main__":
    bot = MyBot(command_prefix=os.environ["DISCORD_BOT_PREFIX"], help_command=None, case_insensitive=True)
    bot.run(os.environ["DISCORD_BOT_TOKEN"])
