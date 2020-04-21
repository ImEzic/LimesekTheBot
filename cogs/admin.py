import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    
    #*reloads specified cog
    @commands.command(hidden=True, aliases=["rl"])
    @commands.is_owner()
    async def reload(self, ctx, extension):
        await ctx.message.delete()
	await ctx.send("not true")
        self.client.unload_extension(f'cogs.{extension}')
        self.client.load_extension(f'cogs.{extension}')


    #*unloads specific cog
    @commands.command(hidden=True)
    @commands.is_owner()
    async def unload(self, ctx, extension):
        self.client.unload_extension(f'cogs.{extension}')


    #*load extension
    @commands.command(hidden = True)
    @commands.is_owner()
    async def load(self, ctx, extension):
        self.client.load_extension(f'cogs.{extension}')


def setup(client):
    client.add_cog(Admin(client))
