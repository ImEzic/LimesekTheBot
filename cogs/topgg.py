import discord
from discord.ext import commands
import os
import requests

class TopGG(commands.Cog):
    

    def __init__(self, client):
        self.client = client
        print("topgggggggg")
    
    
        headers = {  
        "content-type": "application/json",
        "authorization": os.environ.get("TOPGG_TOKEN"),
        "user-agent": "Elon Musk/1.1 Python/3.8 requests/2.23.0"
        }

        payload = {"server_count": len(self.client.guilds)} # The amount you want to post (dont falsify this)
        req = requests.post("https://top.gg/api/bots/688397092707631125/stats", json=payload, headers=self.headers)
        print(req)
        if 199 < req.status_code < 300:
            print("Successfully posted '" + str(payload) + "' to TopGG.")
        else:
            print(f"Failed to post guild count to TopGG, response code {req.status_code}")

def setup(client):
    client.add_cog(TopGG(client))