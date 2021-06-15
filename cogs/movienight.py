import discord
from discord.ext import commands


class Movienight(commands.Cog):
   
    def __init__(self, client):
        self.client = client
           
    @commands.command()
    async def vote(self,ctx,title1,*,title2):
        embed = discord.Embed(title="Let the voting begin", description="React with a number of the position that you are choosing", color=0xffc200)
        numbers=["1️⃣","2️⃣","3️⃣","4️⃣","5️⃣","6️⃣","7️⃣","8️⃣","9️⃣","🔟"]
        
        a=[title1,title2]
        b=[]
        for i in a:
            b+=i.split('" "')
        global titles
        titles = [sub.replace('"', '') for sub in b]
        
        for c in range(0,len(titles)):
            embed.add_field(name=f"{numbers[c]} {titles[c]}", value=f"{(len(max(titles, key=len))//2)*'='}", inline=True)
        message = await ctx.send(embed=embed)
        for c in range(0,len(titles)):
            await message.add_reaction(numbers[c])
            
    @vote.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('You need at least two arguments: `vote "argument1" "argument2"`')
        if isinstance(error, commands.errors.CommandInvokeError):
            await ctx.send(f'Maximum amount of arguments is 10 `you have: {len(titles)}`')    
        
def setup(client):
    client.add_cog(Movienight(client))

        