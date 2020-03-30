import discord
from discord.ext import commands


class Mods(commands.Cog):
   
    def __init__(self, client):
        self.client = client

    
    ##*clearing messgaes
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, amount=1):
        clear = await ctx.channel.purge(limit=amount + 1)
        await ctx.send(f'We are doing some kind of cover up ay?', delete_after = 5)

    #*Kick user
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member=None, *,Reason=None):

        if(member == None):
            await ctx.send('You need to give me someone to work with')

        elif(member == ctx.message.author):
            await ctx.send('Please don\'t tell me you are seriuos')
        
        elif(member.top_role >= ctx.message.author.top_role):
            await ctx.send('Are you really trying to kick someone higher or equal to you??')
        
        elif(member.top_role > member.guild.me.top_role):
            await ctx.send('I need to have a higher role than him')

        else:
            await member.send(f'You got kicked from {ctx.guild.name} Reason: {Reason}')
            await member.kick(reason=Reason)
            await ctx.send(f'{member.mention} got kicked from the server for: {Reason}')
  

    #*Ban user
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member=None, *,Reason=None):
        
        if(member == None):
            await ctx.send('You need to give me someone to work with')

        elif(member == ctx.message.author):
            await ctx.send('Please don\'t tell me you are seriuos')
        
        elif(member.top_role >= ctx.message.author.top_role):
            await ctx.send('Are you really trying to ban someone higher or equal to you??')
        
        elif(member.top_role > member.guild.me.top_role):
            await ctx.send('I need to have a higher role than him')
            
        else:
            await ctx.message.delete()
            await member.send(f'You got banned from {ctx.guild.name} Reason: {Reason}')
            await member.ban(reason=Reason)
            await ctx.send(f'{member.mention} got banned from the server for: {Reason}')


    #*unban user
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
            print(ctx.guild.bans)



        
            # banned_users = await ctx.guild.bans()
            # member_name, member_discriminator = member.split('#')

            # for ban_entry in banned_users:
            #     user = ban_entry.user

            #     if(user.name, user.discriminator) == (member_name, member_discriminator):
            #         await ctx.guild.unban(user)
            #         await ctx.send(f'**{user}** got unnbaned.')
            #         return
        

def setup(client):
    client.add_cog(Mods(client))