from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>')
web_hooks = {}


@bot.command(description="End your current chat", aliases=['e'])
async def end(ctx):
    await ctx.send("W.I.P.")


def create_session():
    web_hooks["channelid"] = "newwebhook"
    return "channelid"


async def start():
    if "DISCORD_TOKEN" in os.environ:
        bot.run(os.environ.get("DISCORD_TOKEN"), bot=True, reconnect=True)
    else:
        print("You must define 'DISCORD_TOKEN'!")
