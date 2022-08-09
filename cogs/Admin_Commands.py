import discord
from discord.ext import commands
import requests

class Admin_Commands(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has connected to Discord!')

    @commands.command(name="Ping", aliases=['ping','PING'], brief='Anyone can use!', description='Used to check the bot is still responsive')
    async def cake(self,ctx):
        embed=discord.Embed(title="Ground Control to Major Tom")
        await ctx.send(embed=embed)




def setup(bot):
    bot.add_cog(Admin_Commands(bot))