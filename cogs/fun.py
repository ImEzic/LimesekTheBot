import discord
import random
from discord.ext import commands


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client


    #*coin flip
    @commands.command()
    async def coinflip(self, ctx):
        coin = ['**Heads**','**Tails**']
        await ctx.send(random.choice(coin))


    #*Bot says what user will give him
    @commands.command()
    async def say(self, ctx, *,text):
        await ctx.send(f"{text} \n\u200b{(len(text) + 5)*' '}-{ctx.message.author}")
    
    
    #*on_message commands
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            await message.author.send(':x: Sorry, but I don\'t accept commands through direct messages! Please use the `#bots` channel of your corresponding server!')
            return

        if message.author == self.client.user:
            return

        if "caban" in message.content.lower():
            await message.channel.send('Caban?! Omg jesus not her againnn')

        if '@!688397092707631125' in message.content.lower():
            await message.channel.send('Type `elon help` or `bro help` to see the list of commands brother')
        
        if message.content.lower().replace('?', '') in ['how are you', 'what\'s up']:
            wittyResponse = ['My lawyer says I don’t have to answer that question.',
                             'I could really go for a massage.',
                             'I\'d say I\'m a [insert number here] out of 10.',
                             'If I were any better, I\'d be illegal.',
                             'I dunno. Is it Friday yet?',
                             'I\'m just how I like my steak Medium well.']
            await message.channel.send(random.choice(wittyResponse))
        

    #*8ball
    @commands.command()
    async def 8ball(self, ctx, message):
        magicResponse = ['It is certain.',
                        'It is decidedly so.',
                        'Without a doubt.',
                        'Yes - definitely.',
                        'You may rely on it.',
                        'As I see it, yes.',
                        'Most likely.',
                        'Outlook good.',
                        'Yes.',
                        'Signs point to yes.',
                        'Reply hazy, try again.',
                        'Ask again later.',
                        'Better not tell you now.',
                        'Cannot predict now.',
                        'Concentrate and ask again.',
                        'Don\'t count on it.',
                        'My reply is no.',
                        'My sources say no.',
                        'Outlook not so good.',
                        'Very doubtful.']
        await ctx.send(random.choice(magicResponse))

    #*Let me google that for you
    @commands.command()
    async def google(self, ctx, *,search):

        await ctx.send(f"https://lmgtfy.com/?q={search.replace(' ','+')}")
    

    #*The Usless Web
    @commands.command()
    async def useless(self, ctx):
        await ctx.send("https://theuselessweb.com/")
        

    #*Gives size of member's little guy
    @commands.command()
    async def size(self, ctx, member: discord.Member = None):
        member = ctx.author if member == None else member
        await ctx.send(f'{member.mention}\'s friend is this size: 8{random.randint(3,15)*"="}D')


    #*roasts
    @commands.command()
    async def roast(self, ctx, member: discord.Member):
        roasts = ["You have your entire life to be a jerk. Why not take today off?",
        "Your ass must be pretty jealous of all the shit that comes out of your mouth.",
        "Remember when I asked for your opinion? Me neither.",
        "If you’re waiting for me to care, I hope you brought something to eat, ‘cause it’s gonna be a really long time.",
        "Some day you’ll go far—and I really hope you stay there.",
        "I’m trying my absolute hardest to see things from your perspective, but I just can’t get my head that far up my ass.",
        "Sometimes it’s better to keep your mouth shut and give the impression that you’re stupid than open it and remove all doubt.",
        "I’m not a proctologist, but I know an asshole when I see one.",
        "You only annoy me when you’re breathing, really.",
        "Do yourself a favor and ignore anyone who tells you to be yourself. Bad idea in your case.",
        "I don’t know what your problem is, but I’m guessing it’s hard to pronounce.",
        "Do your parents even realize they’re living proof that two wrongs don’t make a right?",
        "Remember that time I said I thought you were cool? I lied.",
        "Everyone’s entitled to act stupid once in awhile, but you really abuse the privilege.",
        "I can’t help imagining how much awesomer the world would be if your dad had just pulled out.",
        "Do you ever wonder what life would be like if you’d gotten enough oxygen at birth?",
        "Please, save your breath. You’ll probably need it to blow up your next date.",
        "Can you die of constipation? I ask because I’m worried about how full of shit you are.",
        "Good story, but in what chapter do you shut the fuck up?",
        "Don’t hate me because I’m beautiful. Hate me because your boyfriend thinks so.",
        "Were you born on the highway? That is where most accidents happen.",
        "Please, keep talking. I only yawn when I’m super fascinated.",
        "If I wanted to hear from an asshole, I’d fart.",
        "Jesus might love you, but everyone else definitely thinks you’re an idiot.",
        "Sorry, I didn’t get that. I don’t speak bullshit.",
        "The only way you’ll ever get laid is if you crawl up a chicken’s ass and wait.",
        "If ignorance is bliss, you must be the happiest person on the planet.",
        "Are you always such an idiot, or do you just show off when I’m around?",
        "There are some remarkably dumb people in this world. Thanks for helping me understand that.",
        "I could eat a bowl of alphabet soup and shit out a smarter statement than whatever you just said.",
        "I was pro life. Then I met you.",
        "You’re about as useful as a screen door on a submarine.",
        "Whenever we hang out, I remember that God really does have a sense of humor.",
        "It’s kind of hilarious watching you try to fit your entire vocabulary into one sentence.",
        "Please just tell me you don’t plan to home-school your kids.",
        "You always bring me so much joy—as soon as you leave the room.",
        "I was hoping for a battle of wits but it would be wrong to attack someone who’s totally unarmed.",
        "I’d tell you how I really feel, but I wasn’t born with enough middle fingers to express myself in this case.",
        "Stupidity’s not a crime, so feel free to go.",
        "I’d tell you to go fuck yourself, but that would be cruel and unusual punishment."]
        await ctx.send(random.choice(roasts))


def setup(client):
    client.add_cog(Fun(client))