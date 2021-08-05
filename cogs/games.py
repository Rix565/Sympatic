import asyncio

from discord.ext import commands
from discord.ext.commands import bot_has_permissions, BotMissingPermissions
import discord
from jedit import *
import random
class Games(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @bot_has_permissions(manage_threads=True)
    async def animal_catch(self, ctx):
        UserID = str(ctx.author.id)
        database = reader("././db.json")
        try:
            if database['users'][UserID]['games'][str(1)]:
                thread = await ctx.channel.start_thread(name="Jeu Animal Catch pour " + ctx.author.name, message=ctx.message)
                await discord.Thread.send(thread, "Bienvenue ! Vous allez jouer au jeu Animal Catch. Tenez vous prêt !")
                await asyncio.sleep(5)
                await discord.Thread.send(thread, "3...")
                await asyncio.sleep(1)
                await discord.Thread.send(thread, "2...")
                await asyncio.sleep(1)
                await discord.Thread.send(thread, "1...")
                await asyncio.sleep(1)
                await discord.Thread.send(thread, "Go !")
                await asyncio.sleep(1)
                await discord.Thread.send(thread, "Un animal va venir, patientez un peu...")
                await asyncio.sleep(random.randint(1, 10))
                await discord.Thread.send(thread, "UN ANIMAL EST LÀ ! Mettez la réaction :white_check_mark: pour l'avoir !!")

                def check(reaction, user):
                    return user == ctx.message.author and str(reaction.emoji) == '✅'
                try:
                    reaction, user = await self.client.wait_for('reaction_add', timeout=7.0, check=check)
                except asyncio.TimeoutError:
                    await discord.Thread.send(thread, 'Trop tard, il est parti...')
                    await asyncio.sleep(1)
                    await discord.Thread.send(thread, 'Destruction du fil dans 5 secondes !')
                    await asyncio.sleep(5)
                    await discord.Thread.delete(thread)
                    await ctx.send("Dommage, vous avez perdu... Vous aurez plus de chance, la prochaine fois !")
                else:
                    await discord.Thread.send(thread, "VOUS AVEZ GAGNÉ ! Vous avez gagné un animal + 10$ !")
                    database['users'][UserID]['rank']['animals'] += 1
                    database['users'][UserID]['rank']['money'] += 10
                    with open("././db.json", 'w', encoding='utf8') as jsonFile:
                        json.dump(database, jsonFile, indent=4)
                    await asyncio.sleep(1)
                    await discord.Thread.send(thread, 'Destruction du fil dans 5 secondes !')
                    await asyncio.sleep(5)
                    await discord.Thread.delete(thread)
                    await ctx.send("Félicitations ! Vous avez GAGNÉ !")
        except:
            await ctx.send("Tu n'as pas encore acheté ce jeu, ou tu es dans un fil !")
    @animal_catch.error
    async def error_handler(self, ctx, error):
        if isinstance(error, BotMissingPermissions):
            await ctx.send(f"J'ai besoin de la permission de pouvoir gérer les fils/en créer ! Demande à un adminstateur de l'ajouter !")
        else:
            raise error

def setup(client):
    client.add_cog(Games(client))