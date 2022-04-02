from logging import exception
import discord
import os
from discord.ext import commands
from discord.utils import get

__version__ = '3.1.0'

intents = discord.Intents.default()
intents.message_content = True


client = commands.Bot(command_prefix = commands.when_mentioned_or('lim ', 'lm ', 'Lim ', 'Lm '), intents=intents)
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
    
    async def load_extensions():
        try:
            for filename in os.listdir('./cogs'):
                if filename.endswith('.py'):
                    await client.load_extension(f'cogs.{filename[:-3]}')
        except Exception as e:
            print(f"Couldn't load cog {filename[:-3]}: {e}")
    
    #* Bot Status
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Bobrowski do domu'))
    
async def main():
    async with client:
        await load_extensions()
        await client.start(os.environ.get("BOT_TOKEN"))

asyncio.run(main())
