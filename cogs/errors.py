import discord
from discord.ext import commands


class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    #*Error if user doesn't have a rank to use specific command
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #dont have a role to run commnd
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"{ctx.author.mention} You don\'t have permmision to do that silllly")
        
        elif isinstance(error, commands.CommandNotFound):
            pass
        
        elif isinstance(error, commands.MissingRequiredArgument):
            pass
        
        elif isinstance(error, commands.BadArgument):
            pass
        elif isinstance(error, commands.NotOwner):
            await ctx.message.delete()
        else:
            raise error

def setup(client):
    client.add_cog(Errors(client))