import os
import dbl
import discord
from discord.ext import commands


class TopGG(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.token = os.environ.get("TOPGG_TOKEN") 
        self.dblpy = dbl.DBLClient(self.client, self.token, autopost=True) # Autopost will post your guild count every 30 minutes

    async def on_guild_post(self):
        print("Server count posted successfully")

def setup(client):
    client.add_cog(TopGG(client))