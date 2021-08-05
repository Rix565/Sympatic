import asyncio

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
        calc = int((int(database['users'][UserID]['rank']['lvl']) * int(database['options']['xp_multiplier']))) + basexp
        embed.set_thumbnail(url=ctx.message.author.avatar.url)
        embed.add_field(name="XP", value=str(database['users'][UserID]['rank']['xp']) + "/" + str(calc))
        embed.add_field(name="Level", value=database['users'][UserID]['rank']['lvl'])
        embed.add_field(name="Money", value=str(database['users'][UserID]['rank']['money']) + "$")
        if int(database['users'][UserID]['rank']['animals']) <= 1:
            embed.add_field(name="Animaux", value=str(database['users'][UserID]['rank']['animals']) + " animal")
        else:
            embed.add_field(name="Animaux", value=str(database['users'][UserID]['rank']['animals']) + " animaux")
        await ctx.send(embed=embed)

    @commands.command()
    async def delete_account(self, ctx):
        UserID = str(ctx.author.id)
        database = reader("././db.json")
        if not UserID in database['users']:
            await ctx.send("Vous n'avez pas de compte!")
            return
        await ctx.send(":warning: ATTENTION ! :warning:\nVous vous apprêtez à supprimer (donc réinitialiser) votre compte ! Êtes vous sûr ? (ajouter la réaction ✅ pour continuer.)")

        def check(reaction, user):
            return user == ctx.message.author and str(reaction.emoji) == '✅'

        try:
            reaction, user = await self.client.wait_for('reaction_add', timeout=5.0, check=check)
        except asyncio.TimeoutError:
            await ctx.send("Opération annulé.")
        else:
            del database['users'][UserID]
            with open("././db.json", 'w', encoding='utf8') as jsonFile:
                json.dump(database, jsonFile, indent=4)
            await ctx.send("Compte supprimé/réinitialisé. Merci d'avoir utilisé Sympatic !")


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
        calc = int((int(database['users'][UserID]['rank']['lvl']) * int(database['options']['xp_multiplier']))) + basexp
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
            database["users"][UserID] = {"rank": {"lvl": 0, "xp": 0, "money": 0, "animals": 0}, "games": {"game1": False}}
            with open("././db.json", 'w', encoding='utf8') as jsonFile:
                json.dump(database, jsonFile, indent=4)
    @commands.command()
    async def buygame(self, ctx, game_id=None):
        await self.initialize_user(ctx)
        UserID = str(ctx.author.id)
        database = reader("././db.json")
        if game_id is None:
            await ctx.send("Donne l'id du jeu en question !")
            return
        if str(game_id) in database['games']:
            try:
                if database['users'][UserID]['games'][str(game_id)]:
                    await ctx.send("Vous avez déjà acheté ce jeu !")
                    return
            except:
                pass
            if database["users"][UserID]['rank']["money"] >= database['games'][str(game_id)]['moneytobuy']:
                database["users"][UserID]['rank']["money"] -= database['games'][str(game_id)]['moneytobuy']

                database["users"][UserID]['games'][str(game_id)] = True
                with open("././db.json", 'w', encoding='utf8') as jsonFile:
                    json.dump(database, jsonFile, indent=4)
                await ctx.send("Vous avez acheté le jeu "+ str(database['games'][str(game_id)]['name']) +" !")
            else:
                await ctx.send("C'est trop... **CHER !** (K.O !)")
        else:
            await ctx.send("Hmm... Ça n'a pas l'air d'être un jeu existant, ça.")
            return

def setup(client):
    client.add_cog(Rank(client))
