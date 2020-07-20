import discord
from discord.ext import commands
import os
import requests

class TopGG(commands.Cog):
    

    def __init__(self, client):
        self.client = client
        

    # The headers, this doesn't need to be set every time you push the data, only once. 
    #
    # Do be sure to change BOT_NAME in 'user-agent' and put your token in 'DBL_TOKEN_HERE', if this is an
    # open source project I would reccommend putting this in a seperate json file, and getting it from there.
    headers = {  
    "content-type": "application/json",
    "authorization": os.environ.get("TOPGG_TOKEN")
    "user-agent": "Elon_Musk/1.1 Python/3.8 requests/2.23.0"
    }

    payload = {"server_count": len(client.guilds)} # The amount you want to post (dont falsify this)
    req = requests.post("https://top.gg/api/bots/688397092707631125/stats", json=payload, headers=self.headers)
    if 199 < req.status_code < 300:
    print("Successfully posted '" + str(payload) + "' to TopGG.")
    else:
    print("Failed to post guild count to TopGG, response code {}".format(req.status_code)

def setup(client):
    client.add_cog(TopGG(client))
    




