import asyncio

import discord, color_table
import random
from jedit import *
from discord.ext import commands

class UltraMiniGames(commands.Cog):
    def __init__(self, client):
        self.client = client
    @commands.command()
    async def dice(self, ctx):
        dice = random.randint(1, 6)
        color_list = [c for c in color_table.colors.values()]
        embed = discord.Embed(title="Le dé", color=random.choice(color_list))
        embed.add_field(name=":video_game: Le dé est tombé !", value="->Il est tombé sur... " + str(dice) + " !")
        await ctx.send(embed=embed)

    @commands.command()
    async def doublemoney(self, ctx, money=None):
        if money is None:
            await ctx.send("Vous avez oublier de mettre l'argent que vous voulez potentiellement doubler !")
            return
        try:
            UserID = str(ctx.author.id)
            money = int(money)
            database = reader("././db.json")
            if money > database['users'][UserID]['rank']['money']:
                await ctx.send("Hmm... Faites un prêt à la banque.")
                return
            rand = random.randint(1, 2)
            await ctx.send("Vous avez.... (roulement de tambours)")
            await asyncio.sleep(5)
            if rand == 2:
                database["users"][UserID]['rank']['money'] -= money
                money = money * 2
                database["users"][UserID]['rank']['money'] += money
                await ctx.send("... GAGNÉ ! :confetti_ball: Félicitations ! Vous avez gagné "+str(money)+ "$ !")
            else:
                database["users"][UserID]['rank']['money'] -= money
                await ctx.send("PERDU... Désolé... vous avez perdu "+str(money)+"$ ... :cry:")
            with open("././db.json", 'w', encoding='utf8') as jsonFile:
                json.dump(database, jsonFile, indent=4)
        except:
            await ctx.send(":thinking: Hmm... Vous êtes sûr que vous avez vraiment mis des nombres et pas juste du texte ?")
            return

def setup(client):
    client.add_cog(UltraMiniGames(client))