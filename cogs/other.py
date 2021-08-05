import asyncio

import discord, color_table
import random
from discord.ext import commands
from main import thebot

class Other(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        color_list = [c for c in color_table.colors.values()]
        embed = discord.Embed(title="Liste des commandes", color=random.choice(color_list))
        embed.add_field(name=":game_die: Ultra Mini Games", value="`dice`: Faire tomber un dé !\n`doublemoney`(demande un argument: nombre de money à doubler): doublez potentiellement l'argent que vous voulez doubler !")
        embed.add_field(name=":arrow_up: Rank", value="`rank`: Voir votre rank !\n`delete_account`: **ACTION IRRÉVERSIBLE** Supprimer votre compte.\n`buygame`(demande un argument: id du jeu): Acheter un jeu !")
        embed.add_field(name=":video_game: Mini-jeux", value="`animal_catch`(ID n°1): Jeu où tu dois essayer d'attraper un animal pour en gagner un.")
        embed.add_field(name=":zzz: Autres", value="`help`: Tu es dessus...!\n`inviteme`: M'inviter sur ton serveur !\n`important`: message important du développeur à l'intention de ses utilisateurs.")
        embed.set_footer(text=f'Sympatic v1.00.3 - En réponse à {ctx.message.author.name} - Créé par Rixy - Destruction du message dans 5 secondes !',
                        icon_url=thebot.user.avatar.url)
        message = await ctx.send(embed=embed)
        await asyncio.sleep(5)
        await message.delete()

    @commands.command()
    async def inviteme(self, ctx):
        await ctx.send("Lien envoyé dans tes messages privés !")
        color_list = [c for c in color_table.colors.values()]
        embed = discord.Embed(title="M'inviter sur ton serveur", color=random.choice(color_list))
        embed.add_field(name="Alors comme ça, on veut m'inviter ?", value="Voici mon lien d'invitation ! \nhttps://discord.com/oauth2/authorize?client_id=872021788945698817&permissions=51539626048&scope=bot")
        await ctx.author.send(embed=embed)
    @commands.command()
    async def important(self, ctx):
        await ctx.send("Ceci est un message assez important du développeur. Le bot utilise la version alpha de Discord.py, librarie servant à faire fonctionner ce bot. Il ce pourrait qu'il y ait des bugs qui ne soient pas en rapport avec mon code, mais avec Discord.py. Merci ! -Rixy")



def setup(client):
    client.add_cog(Other(client))