import dbl
import discord
from discord.ext import commands
import os

class TopGG(commands.Cog):
    

    def __init__(self, client):
        self.client = client
        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY4ODM5NzA5MjcwNzYzMTEyNSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTg3ODQzNzgyfQ.gpLYaqZicN4mozzdygrUeEV77WeSZXZR3_XqzhNHZKk"
        self.dblpy = dbl.DBLClient(self.client, self.token, autopost=True)

    async def on_guild_post(self):
        print("Server count posted successfully")

def setup(client):
    client.add_cog(TopGG(client))
