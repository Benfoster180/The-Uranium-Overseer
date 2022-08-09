import discord
from discord.ext import commands
import requests
import discord
import os
import time
import asyncio
import tweepy
import asyncio
import time

sim_text = ""


all_tweets = []
passed = []
num = 0
lock = False
numb = 0 # used to make list to a string
more_then_two_slash = False # used to only allow one / to added
text = str()

#API KEYS go here!
auth = tweepy.OAuthHandler("Twiiter API KEYS", "Twiiter API KEYS")
auth.set_access_token("Twiiter API KEYS", "Twiiter API KEYS")
api = tweepy.API(auth)

def get_data():
    tweets = api.user_timeline(screen_name="numerco",count=5 ,include_rts = False,tweet_mode = 'extended')
    oldest_id = tweets[-1].id
    all_tweets.extend(tweets)
    print('N of tweets downloaded till now {}'.format(len(all_tweets)))

    for info in tweets[:1]:
            #print("ID: {}".format(info.id))
            #print(info.created_at)
            #print(info.full_text)
            #print("\n")
        sim_text == info.full_text
        return info.full_text
class Price_Update(commands.Cog):

    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'{self} has connected to Discord!')
        guild = self.bot.get_guild("Your Discord Sever ID")
        member = guild.get_member("Discord Bot ID")
        await member.edit(nick="Fetching Price!")
        await asyncio.sleep(5)
        #Defines varibles we need
        all_tweets = []
        passed = []
        num = 0
        lock = False
        numb = 0 # used to make list to a string
        more_then_two_slash = False # used to only allow one / to added
        text = str()

        Run_text = get_data()
        #Code running day - day
        
        while True:
    
            if Run_text[num] == "L":
                lock = True
                num = len(Run_text)

            elif Run_text[num] == '/':
                if more_then_two_slash != True:
                    passed.append(Run_text[num]) 
                    num = num + 1
                    more_then_two_slash = True

            #runs until we have done
            if num != len(Run_text):
                try:
                    a = int(Run_text[num])
                    #print(a)
                    passed.append(a)
                    #print(passed)
                    num = num + 1

                #Skips all letters
                except:
                    num = num + 1

            if num == len(Run_text):
                numb=0
                #print(len(passed))
                for i in range(len(passed)):
                    text = text + str(passed[numb])
                    numb = numb + 1
                    #print(text)
                if text == text:
                    print("I'm running")
                   
                    guild = self.bot.get_guild(Your Discord Sever ID)
                    member = guild.get_member("Discord Bot ID")
                    await member.edit(nick=text)
                    await asyncio.sleep(10)
                    
                    
            
                    await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="Mase by Cursed#2172"))
                    passed.clear()
                    #print("after clear",len(passed))
                    lock = False
                    numb = 0
                    num = 0
                    more_then_two_slash = False
                    #print("it run")
                    text = ""
                    Run_text = get_data()
                    await asyncio.sleep(600)




def setup(bot):
    bot.add_cog(Price_Update(bot))
