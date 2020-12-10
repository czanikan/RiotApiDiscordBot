import discord
from discord.ext import commands
from riotwatcher import LolWatcher, ApiError, RiotWatcher
import pandas as pd
import json

# golbal variables
api_key = 'RGAPI-fee01dd3-7717-447e-9cf3-6efee7821af2'
watcher = LolWatcher(api_key)
my_region = 'eun1'

me = watcher.summoner.by_name(my_region, 'Goblinatron')
id = me['accountId']
my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
print(my_ranked_stats)
##if my_ranked_stats[0]['queueType'] == "RANKED_SOLO_5x5":
#    print("ranked")
#else:
 #   print("no ranked")


class RiotBot (commands.Cog):
    def __init__(self, bot): 
        self.bot = bot

    @commands.command()
    async def rb(self, ctx, name):
        
        async with ctx.channel.typing():
            me = watcher.summoner.by_name(my_region, name)
            id = me['accountId']
            my_ranked_stats = watcher.league.by_summoner(my_region, me['id'])
            
            embed = discord.Embed(title = "RiotBot - Summoner's info")
            embed.add_field(name="Name: ", value=me['name'])
            embed.add_field(name="Summoner Level: ", value=str(me['summonerLevel']))

            if (['queueType'] not in my_ranked_stats):
                embed.add_field(name="Ranked Solo 5x5: ", value='None')
            else:
                if (my_ranked_stats[0]['queueType'] == "Ranked Solo 5x5"):
                    embed.add_field(name="Ranked Solo 5x5: ", value=my_ranked_stats[0]['tier'] + " " + my_ranked_stats[0]['rank'])
                elif my_ranked_stats[1]['queueType'] == "Ranked Solo 5x5":
                    embed.add_field(name="Ranked Solo 5x5: ", value=my_ranked_stats[1]['tier'] + " " + my_ranked_stats[1]['rank'])
                else: 
                    embed.add_field(name="Ranked Solo 5x5: ", value='None')
            


            #if 'queueType' not in my_ranked_stats[1]:
            #    embed.add_field(name="Ranked Flex: ", value='None')
            #else:
            #    embed.add_field(name="Ranked Flex: ", value=my_ranked_stats[1]['tier'] + " " + my_ranked_stats[1]['rank'])

            await ctx.send(embed = embed)

    @commands.command()
    async def champ(self, ctx, name):
        
        async with ctx.channel.typing():
            static_champ_list = watcher.static_data.champions(my_region)
            champ = name

            embed = discord.Embed(title = "RiotBot - Champion's info")
            embed.add_field(name="Champ info: ", value=static_champ_list['data'][champ])

            await ctx.send(embed = embed)



    

def setup(bot):
    bot.add_cog(RiotBot(bot))

