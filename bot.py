from logging import exception
import discord
import os
from discord.ext import commands

__version__ = '2.0.0'

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
    except Exception as e:
        print(f"Couldn't load cog {filename[:-3]}: {e}")
    
    #* Bot Status
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Making Pancakes'))
    

@client.event
async def on_guild_join(guild):
    firstChannel = guild.text_channels[0]
    await firstChannel.send("Hi there, I'm Elon! Thanks for inviting me here. Type `elon help` or `bro help` to get a list of commands or just mention me in chat."
                            " If you need help or find a bug: Join our support server at https://discord.gg/PYU6uhB")


client.run(os.environ.get("BOT_TOKEN"))