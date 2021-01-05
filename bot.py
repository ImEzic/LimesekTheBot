import discord
import os
from discord.ext import commands
import requests
import time

__version__ = '1.0.0'

client = commands.Bot(command_prefix = commands.when_mentioned_or('elon ', 'bro ', 'Elon ', 'Bro '))
client.remove_command('help')


#*bot status
@client.event
async def on_ready():
    
    #*Bot Info
    print('Logged in as')
    print(f'Bot-Name: {client.user.name}')
    print(f'Bot-ID: {client.user.id}')
    print(f'Discord Version: {discord.__version__}')
    print(f'Bot Version: {__version__}')
    client.AppInfo = await client.application_info()
    print(f'Owner: {client.AppInfo.owner}')
    print('------')
    
    
    #*Loading cogs
    try:
        for filename in os.listdir('./cogs'):
            if filename.endswith('.py'):
                client.load_extension(f'cogs.{filename[:-3]}')
    except Exception:
            print(f'Couldn\'t load cog {filename}')
    
    #* Bot Status
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Making Pancakes'))
    
    
#*TopGG Server count
@commands.command()
@commands.is_owner()
async def topgg(ctx):
    headers = {  
        "content-type": "application/json",
        "authorization": os.environ.get("TOPGG_TOKEN"),
        "user-agent": "Discord-Bot-That-Does-Stuff/1.0.0 Python/3.8.2 requests/2.23.0"
    }
    while True:
        payload = {"server_count": len(client.guilds)}
        req = requests.post("https://top.gg/api/bots/{}/stats".format(str(client.user.id)), json=payload, headers=headers)
        if 199 < req.status_code < 300:
            print("Successfully posted '" + str(payload) + "' to TopGG.")
        else:
            print("Failed to post guild count to TopGG, response code {}".format(req.status_code))
            break
        time.sleep(300) # change that to 3600


@client.event
async def on_guild_join(guild):
    firstChannel = guild.text_channels[0]
    await firstChannel.send("Hi there, I'm Elon! Thanks for inviting me here. Type `elon help` or `bro help` to get a list of commands or just mention me in chat."
                            " If you need help, or find a bug: Join our support server at https://discord.gg/PYU6uhB")


client.run(os.environ.get("BOT_TOKEN"))