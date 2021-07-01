#TODO:
#- Implement more advanced Counting Channels (Track several roles in one channel)
#- Split main.py into several files. probably utils.py, bot.py, commands.py, and maybe one file for every command
#- 
import discord
import config
from discord.ext import commands
from tests import Main_Test


PREFIX = config.PREFIX
BOT_TOKEN = config.BOT_TOKEN
intents = discord.Intents.default()
intents.members = True
intents.presences = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    print("Bot is ready")


@bot.listen("on_message")
async def on_message(message):
    global PREFIX
    if not message.mentions:
        return
    for mention in message.mentions:
        if mention == bot.user:
            await message.channel.send(f"My prefix is: {PREFIX}")



@bot.command(name="run_tests", help="Runs all the tests")
async def run_tests(ctx):
    await ctx.send("Running tests...")
    await Main_Test.run(ctx)

bot.run(BOT_TOKEN)
