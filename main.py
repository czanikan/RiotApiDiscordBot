import os
import discord
from discord.ext import commands
#from settings import *

bot = commands.Bot(command_prefix = "!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run('NzgzMDk0MzkyODYzODUwNTA2.X8VvfA.0--rnaWqGvZHkoBk_lsrtF0gNdU')