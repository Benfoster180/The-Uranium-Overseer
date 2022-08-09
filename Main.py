import discord
import os
from discord.ext import commands

bot = discord.Client()
bot = commands.Bot(command_prefix="$")

@bot.command()
async def load(ctx):
    if str(ctx.author.id) == "374830592140771330" or str(ctx.author.id) == "737907882200399875":
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.load_extension(f'cogs.{filename[:-3]}')
        embed=discord.Embed(title="Locked and Loaded")
        await ctx.send(embed=embed)
    

@bot.command()
async def unload(ctx):
    if str(ctx.author.id) == "374830592140771330" or str(ctx.author.id) == "737907882200399875":
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                bot.unload_extension(f'cogs.{filename[:-3]}')
        embed=discord.Embed(title="Please Run $load to restart the bot!")
        await ctx.send(embed=embed)

    




for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')



bot.run("Discord Token here")
