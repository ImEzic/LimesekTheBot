import discord
from discord.ext import commands


class Info(commands.Cog):

    def __init__(self, client):
        self.client = client


    #*Info about the bot
    @commands.command()
    async def who(self, ctx):
        embed = discord.Embed(title="Elon duck you!", description="Your brother Elon here if you need something just **elon** or **bro** me"
                                                                  "and I will help you if I will want to, but do I want to", color=0xffc200)
        
        embed.add_field(name="Author", value="Ezic")
        embed.add_field(name="Server count", value= len(self.client.guilds))
        embed.add_field(name="Invite", value="[Invite link](https://discordapp.com/api/oauth2/authorize?client_id=688397092707631125&permissions=8&scope=bot)")
        await ctx.send(embed=embed)

    #*Server list the bot is in
    @commands.command(hidden=True, aliases=['guilds'])
    @commands.is_owner()
    async def servers(self, ctx):
        msg = '```js\n'
        msg += '{!s:19s} | {!s:10s} | {!s:25s} | {}\n'.format('ID', 'Member', 'Name', 'Owner')
        for guild in self.client.guilds:
            msg += '{!s:19s} | {!s:11s}| {!s:25s} | {}\n'.format(guild.id, guild.member_count, guild.name, guild.owner)
        msg += '```'
        await ctx.send(f'Elon is in **{len(self.client.guilds)}** servers')
        await ctx.send(msg)



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
        embed.set_thumbnail(url = member.avatar_url)
        embed.set_footer(text=f'Requested by {ctx.author}', icon_url=ctx.author.avatar_url)

        embed.add_field(name='ID:', value=member.id)
        embed.add_field(name='Name:', value=member.display_name, inline=False)
        
        embed.add_field(name='Born:', value=member.created_at.strftime("%a, %d %B %Y, %I:%M %p UTC"))
        embed.add_field(name='Joined at:', value=member.joined_at.strftime("%a, %d %B %Y, %I:%M %p UTC"), inline=False)
        
        embed.add_field(name=f'Roles [{len(roles)}]', value=' '.join([role.mention for role in roles]))
        embed.add_field(name='Top role:', value=member.top_role.mention)

        embed.add_field(name='Bot?', value=member.bot, inline=False)

        await ctx.send(embed=embed)


    #*Help command
    @commands.command()
    async def help(self, ctx):
        
        embed = discord.Embed(title ='**Elon Musk** is happy to help You *wink*', colour = discord.Color(0xffc200))
        
        embed.add_field(name='Info', value='`who`, `ping`, `investigate`, `help`', inline=False)
        embed.add_field(name='Fun', value='`coinflip`, `say`, `google`, `useless`, `size`, `roast`, `8ball`', inline=False)
        embed.add_field(name='Moderation', value='`clear`, `kick`, `unban`, `ban`', inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))