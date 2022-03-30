from types import MemberDescriptorType
import discord
from discord.ext import commands
from discord.utils import get


class acceptingRules(commands.Cog):
   
    def __init__(self, client):
        self.client = client
           

    @commands.command()
    @commands.is_owner()
    async def regu(self, ctx):
        message ="1. szydzimy z solara\n2. bobrowski do domu\n3. krzysiu król"
        r_message = await ctx.send(message)
        await r_message.add_reaction("🔑")

    @commands.command()
    @commands.is_owner()
    async def addreact(self, ctx):
        message = ctx.get_message(939632391604031538)
        



    #*adds role after accepting the rules and gives access to the server
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 939646486101241908:
            member = payload.member
            guild = member.guild
            emoji = payload.emoji.name
            if emoji == "🔑":
                role = discord.utils.get(guild.roles, name="Zbłąkana Dusza")
            await member.add_roles(role)

    #*removes role after accepting the rules and gives access to the server
    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 939646486101241908:
            member = payload.member
            guild = await(self.client.fetch_guild(payload.guild_id))
            emoji = payload.emoji.name
            
            if emoji == "🔑":
                role = discord.utils.get(guild.roles, name="Zbłąkana Dusza")
                member = await(guild.fetch_member(payload.user_id))
            await member.remove_roles(role)
        
            
        
async def setup(client):
    await client.add_cog(acceptingRules(client))

        
