# on fait les imports des modules
import logging
import os
import mkdir
from discord.ext import commands
from tokenbot import *

Bot_is_Lock = False  # variable que tu vas importer dans les autres class

print("Project Sympatic 1.00.3")
print("Connexion en cours à Discord...")


thebot = commands.Bot(
    # Creation du bot
    command_prefix="sym!",
    description='Sympatic!',
    owner_id='475215232961085440',
    case_insensitive=True
)

admins = [475215232961085440]

# on enlève la commande help
thebot.remove_command('help')

# on créer des commandes

def starter():
    mkdir.mkdir("./cogs")
    for filename in os.listdir('./cogs'):
        # on vérifie que le fichier est bien l'extension python
        if filename.endswith('.py'):
            cog = filename[:-3]
            try:
                print(f'Chargement du cog : \n {cog}')
                thebot.load_extension(f'cogs.{cog}')
            except:
                print(f'Rechargement du cog : \n {cog}')
                thebot.unload_extension(f'cogs.{filename[:-3]}')
                thebot.load_extension(f'cogs.{filename[:-3]}')


@thebot.command()
async def module(ctx, mode=None, extension=None):
    if mode == "load":
        if ctx.message.author.id in admins:
            if extension is None:
                await ctx.send("Vous n'avez pas demandé de module")
            try:
                thebot.load_extension(f'cogs.{extension}')
                await ctx.send("Le module a été chargé.")
            except:
                await ctx.send("Le module n'a pas été chargé")

        else:
            await ctx.send("Vous n'avez pas les droits d'administration.")

    elif mode == "unload":
        if ctx.message.author.id in admins:
            if extension is None:
                await ctx.send("Vous n'avez pas demandé de module")
            try:
                thebot.unload_extension(f'cogs.{extension}')
                await ctx.send("Le module a été déchargé.")
            except:
                await ctx.send("Le module n'a pas été déchargé")
        else:
            await ctx.send("Vous n'avez pas les droits d'administration.")


    elif mode == "reload":
        if ctx.message.author.id in admins:
            if extension is None:
                await ctx.send("Vous n'avez pas demandé de module")
            try:
                thebot.unload_extension(f'cogs.{extension}')
                thebot.load_extension(f'cogs.{extension}')
                await ctx.send("Le module a été rechargé.")
            except:
                await ctx.send("Le module n'a pas été rechargé")
        else:
            await ctx.send("Vous n'avez pas les droits d'administration.")

    elif mode is None:
        await ctx.send("Usage : +module Mode(load/unload/reload) NomDuModule")


@thebot.command()
async def ping(ctx):
    await ctx.send(f'Mon ping est {round(thebot.latency * 1000, 3)} !')

starter()

thebot.run(token, reconnect=True)