from discord.ext import commands
import discord, color_table
from main import thebot
from jedit import *
import random

class Rank(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def rank(self, ctx):
        await self.initialize_user(ctx)
        UserID = str(ctx.message.author.id)
        color_list = [c for c in color_table.colors.values()]
        database = reader("././db.json")
        embed = discord.Embed(title="Rank de " + ctx.author.name, color=random.choice(color_list))
        basexp = 50
        calc = int((int(database['users'][UserID]['rank']['lvl']) * 10)) + basexp
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name="XP", value=str(database['users'][UserID]['rank']['xp']) + "/" + str(calc))
        embed.add_field(name="Level", value=database['users'][UserID]['rank']['lvl'])
        embed.add_field(name="Money", value=str(database['users'][UserID]['rank']['money']) + "$")
        await ctx.send(embed=embed)

    @commands.Cog.listener()
    async def on_message(self, message):
        UserID = str(message.author.id)
        if message.channel.type is discord.ChannelType.private:
            return
        if message.author.id == thebot.user.id:
            return
        await self.initialize_user(message)
        database = reader("././db.json")
        database["users"][UserID]['rank']["xp"] += 1
        basexp = 50
        calc = int((int(database['users'][UserID]['rank']['lvl']) * 10)) + basexp
        if database["users"][UserID]['rank']["xp"] == calc:
            database['users'][UserID]['rank']['lvl'] += 1
            database['users'][UserID]['rank']['xp'] = 0
            database['users'][UserID]['rank']['money'] += calc
            await message.author.send(":confetti_ball: Vous avez gagné un niveau ! Vous êtes maintenant au niveau " + str(database['users'][UserID]['rank']['lvl']) + " ! Bravo ! Vous avez gagné "+ str(calc) +" $ !")
        with open("././db.json", 'w', encoding='utf8') as jsonFile:
            json.dump(database, jsonFile, indent=4)

    async def initialize_user(self, message):
        UserID = str(message.author.id)
        if message.channel.type is discord.ChannelType.private:
            return
        if message.author.id == thebot.user.id:
            return
        database = reader("././db.json")
        if UserID not in database['users']:
            database["users"][UserID] = {"rank": {"lvl": 0, "xp": 0, "money": 0}}
            with open("././db.json", 'w', encoding='utf8') as jsonFile:
                json.dump(database, jsonFile, indent=4)

def setup(client):
    client.add_cog(Rank(client))
