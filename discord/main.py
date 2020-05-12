from discord.ext import commands
import os

bot = commands.Bot(command_prefix='>')


@bot.command(description="End your current chat", aliases=['e'])
async def end(ctx):
    await ctx.send("W.I.P.")


if "DISCORD_TOKEN" in os.environ:
    bot.run(os.environ.get("DISCORD_TOKEN"), bot=True, reconnect=True)
else:
    print("You must define 'DISCORD_TOKEN'!")
