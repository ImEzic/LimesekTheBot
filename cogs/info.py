import discord
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client


    #*pings bot 
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'🏓 Pong! `{round(self.client.latency * 1000)}ms`')

    #*investigate user
    @commands.command()
    async def investigate(self, ctx, member: discord.Member = None):
        member = ctx.author if member == None else member

        roles = [role for role in member.roles]
        
        embed = discord.Embed(colour = member.color, timestamp = ctx.message.created_at)

        embed.set_author(name = f'User record:   {member}')
        embed.set_thumbnail(url = member.avatar.url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar.url)

        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name='Name:', value=member.display_name, inline=False)
        
        embed.add_field(name='Born:', value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
        embed.add_field(name='Joined at:', value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"), inline=False)
        
        embed.add_field(name=f'Roles [{len(roles)}]', value=' '.join([role.mention for role in roles]))
        embed.add_field(name='Top role:', value=member.top_role.mention)

        embed.add_field(name='Bot?', value=member.bot, inline=False)

        await ctx.send(embed=embed)



    @investigate.error
    async def investigate_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Okay... *shakes his head*... Please tell me what that is, because that's not a person for sure")
            await ctx.send("*Sighs*.. just type `investigate [@someguyyouwanttostalk or just leave it blank and see what happens]`")

    
    #*Help command
    @commands.command()
    async def help(self, ctx):
        
        embed = discord.Embed(title ='Widzę, że potrzebujesz pomocy. Nic w tym złego.', colour = discord.Color(0xffc200))
        
        embed.add_field(name='Prefixes', value='`Lm`, `Lim`, `lm`,`lim`', inline=False)
        embed.add_field(name='Info', value='`ping`, `investigate`, `help`,`vote`', inline=False)
        embed.add_field(name='Fun', value='`coinflip`, `say`, `google`, `useless`, `size`, `roast`, `8ball`', inline=False)
        embed.add_field(name='Moderation', value='`clear`, `kick`, `unban`, `ban`', inline=False)

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Info(client))
