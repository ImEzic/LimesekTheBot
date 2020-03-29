import discord
from discord.ext import commands


class Mods(commands.Cog):
   
    def __init__(self, client):
        self.client = client

    # ##*giving user rank on join
    # @commands.Cog.listener()
    # async def on_member_join(self, member):
    #     role = discord.utils.get(member.guild.roles, name='Passengers of Oceanic Flight 815')
    #     await member.add_roles(role)


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

            if(member == None or member == discord.Message.author):
                await ctx.send('What\'s his name boss')
            
            elif(member.top_role > ctx.message.author.top_role):
                await ctx.send('Are you really trying to kick someone higher or equal to you??')
            
            elif(member.top_role > discord.Guild.me):
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
        
        try:    #check if user wants to ban himself or no user specified
            if(member == None or member == discord.Message.author):
                await ctx.send('You can\'t ban yourself')
            else:
                
                await ctx.message.delete()
                await member.send(f'You got banned from {ctx.guild.name} Reason: {Reason}')
                await member.ban(reason=Reason)
                await ctx.send(f'{member.mention} got banned from the server for: {Reason}')

               
        except discord.Forbidden:   #user cannot ban someone with the same permmision 
            await ctx.message.delete()
            await ctx.send(f"You can't kick someone equal to you {ctx.author.mention}")


    #*unban user
    @commands.command()
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, *, member):
        try:
            banned_users = await ctx.guild.bans()
            member_name, member_discriminator = member.split('#')

            for ban_entry in banned_users:
                user = ban_entry.user

                if(user.name, user.discriminator) == (member_name, member_discriminator):
                    await ctx.guild.unban(user)
                    await ctx.send(f'{user.mention} got unnbaned. His sentence is over!')
                    return
        except commands.errors.CommandInvokeError:
            await ctx.send('This user is not banned')


def setup(client):
    client.add_cog(Mods(client))