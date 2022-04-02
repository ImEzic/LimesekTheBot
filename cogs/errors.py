import discord
from discord.ext import commands

class Errors(commands.Cog):

    def __init__(self, client):
        self.client = client

    #*Error if user doesn't have a rank to use specific command
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        
        if isinstance(error, commands.MissingRole):
            await ctx.send(f"{ctx.author.mention} You don\'t have permmision to do that silllly")
        
        elif isinstance(error, commands.CommandNotFound):
           await ctx.send("You clearly have not got a single clue what are you doing here, don't you? Just type `lm help` and stop the spam")
        
        elif isinstance(error, commands.MissingRequiredArgument):
            raise error
        
        elif isinstance(error, commands.BadArgument):
            raise error
        
        elif isinstance(error, commands.errors.MemberNotFound):
            raise error
        
        elif isinstance(error, commands.NotOwner):
            await ctx.message.delete()
            await ctx.send("Ey this is for my father only")
        else:
            print(ctx.guild.name)
            raise error

defsetup( client):
    client.add_cog(Errors(client))
