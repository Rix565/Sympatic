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
        embed.add_field(name=":video_game: Ultra Mini Games", value="`dice`: Faire tomber un dé !\n`doublemoney`(demande un argument: nombre de money à doubler): doublez potentiellement l'argent que vous voulez doubler !")
        embed.add_field(name=":arrow_up: Rank", value="`rank`: Voir votre rank !")
        embed.add_field(name=":zzz: Autres", value="`help`: Tu es dessus...!\n`inviteme`: M'inviter sur ton serveur !\n`important`: message important du développeur à l'intention de ses utilisateurs.")
        embed.set_footer(text=f'Sympatic v1.00.1 - En réponse à {ctx.message.author.name} - Créé par Rixy',
                        icon_url=thebot.user.avatar_url)
        await ctx.send(embed=embed)

    @commands.command()
    async def inviteme(self, ctx):
        await ctx.send("Lien envoyé dans tes messages privés !")
        color_list = [c for c in color_table.colors.values()]
        embed = discord.Embed(title="M'inviter sur ton serveur", color=random.choice(color_list))
        embed.add_field(name="Alors comme ça, on veut m'inviter ?", value="Voici mon lien d'invitation ! \nhttps://discord.com/oauth2/authorize?client_id=872021788945698817&permissions=51539626048&scope=bot")
        await ctx.author.send(embed=embed)
    @commands.command()
    async def important(self, ctx):
        await ctx.send("Ceci est un message assez important du développeur. Parce que la version 2.0 de Discord.py, la librarie que j'utilise pour créer ce bot, arrive à grand pas, le bot aura sûrement besoin la réadaptation de son code. Quand cette nouvelle version sortira, le bot ne se rallumera pas avant un petit moment le temps que j'adapte son code.")


def setup(client):
    client.add_cog(Other(client))