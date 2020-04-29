import dbl
import discord
from discord.ext import commands
import os

class TopGG(commands.Cog):
    """Handles interactions with the top.gg API"""

    def __init__(self, client):
        self.client = client
        self.token = os.environ.get("TOPGG_TOKEN")
        self.dblpy = dbl.DBLClient(self.client, self.token, autopost=True)

    async def on_guild_post(self):
        print("Server count posted successfully")

def setup(client):
    client.add_cog(TopGG(client))