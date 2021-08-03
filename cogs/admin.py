import asyncio

import discord
from discord.ext import commands
from main import thebot
import random


class admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(
            f'Connecté à Discord : depuis votre token , je suis connecté en tant que {self.client.user.name} - {self.client.user.id}.')
        print(f'Le tag discord : {self.client.user}.')
        while True:
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(
                f"Sympatic | Le bot mini-jeux !"))
            await asyncio.sleep(5)
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(
                f"Mon préfix : sym!"))
            await asyncio.sleep(5)
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(
                f"Je suis utilisé sur {len(thebot.guilds)} serveurs."))
            await asyncio.sleep(5)
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(
                f"Ce bot a été codé par Rixy !"))
            await asyncio.sleep(5)
            await self.client.change_presence(status=discord.Status.online, activity=discord.Game(
                f"Bonne journée ! :-)"))
            await asyncio.sleep(5)
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        print(str(error))
        if "is not found" in str(error):
            await ctx.send(":video_game: Commande introuvable ! Avez-vous fait une faute de frappe ? :video_game:")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel.type is discord.ChannelType.private:
            if not message.author.id == thebot.user.id:
                await message.channel.send(":video_game: Ce bot ne peut pas être utilisé dans les messages privés ! Utilise moi sur des serveurs ou invite moi ! :video_game:")


def setup(client):
    client.add_cog(admin(client))
