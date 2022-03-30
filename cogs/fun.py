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
    
    @say.error
    async def say_error(self, ctx, error):
        await ctx.send("`say [message]`")
    
    
    #*on_message commands
    @commands.Cog.listener()
    async def on_message(self, message):
        if isinstance(message.channel, discord.DMChannel):
            # await message.author.send(f'pfff "{message.content}"')
            # await message.author.send("Yeah add me to the server just to talk to me in pm. Bruhh. Do you even think? You aren't even my type tbf. Let's just talk on the server")
            return

        if message.author == self.client.user:
            return

        if "piwo" in message.content.lower():
            await message.channel.send('Po co komu piwo jak jest wódka')

        if '@!939227760075886652' in message.content.lower():
            await message.channel.send('Kto mnie wołał??')
        
        if message.content.lower().replace('?', '') in ['Co tam','co tam','Jak się masz','jak sie masz','jak tam']:
            wittyResponse = ['Mój prawnik powiedział, że nie muszę odpowiadać na to pytanie.',
                             'Co ja bym dał teraz za masaż.',
                             'Powiedział bym, że jestem sex bombą, ale tego nie zrobie',
                             'Jestem tak gorący, że pękają przy mnie termometry',
                             'Czy jest już piątek?',
                             'Nie jest tak źle, ale dobrze też nie jest.']
            await message.channel.send(random.choice(wittyResponse))
        

    #*8ball
    @commands.command(name="8ball")
    async def _8ball(self, ctx , *,message):
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
        if "?" not in message:
            await ctx.send("What are you allergic to question marks???")
            await ctx.send("`8ball [your question and question mark at the end dummy]`")
        if len(message) < 2:
            await ctx.send("I'm going to pretend I didn't see that")
        else:
            await ctx.send(random.choice(magicResponse))

    @_8ball.error
    async def _8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Yeah, alright that's far from correct")
            await ctx.send("`8ball [your question]`")


    #*Let me google that for you
    @commands.command()
    async def google(self, ctx, *,search):
        await ctx.send(f"https://lmgtfy.com/?q={search.replace(' ','+')}")
    
    @google.error
    async def google_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Yes expect output with no input ")
            await ctx.send("`google [something to google perhaps???]`")

    

    #*The Usless Web
    @commands.command()
    async def useless(self, ctx):
        usless=["http://heeeeeeeey.com/",
		        "http://corndog.io/",
                "https://alwaysjudgeabookbyitscover.com",
                "http://thatsthefinger.com/",
                "http://cant-not-tweet-this.com/",
                "http://weirdorconfusing.com/",
                "http://eelslap.com/",
                "http://www.staggeringbeauty.com/",
                "http://burymewithmymoney.com/",
                "https://smashthewalls.com/",
                "https://jacksonpollock.org/",
                "http://endless.horse/",
                "http://www.trypap.com/",
                "http://www.republiquedesmangues.fr/",
                "http://www.movenowthinklater.com/",
                "http://www.partridgegetslucky.com/",
                "http://www.rrrgggbbb.com/",
                "http://beesbeesbees.com/",
                "http://www.koalastothemax.com/",
                "http://www.everydayim.com/",
                "http://randomcolour.com/",
                "http://cat-bounce.com/",
                "http://chrismckenzie.com/",
                "https://thezen.zone/",
                "http://hasthelargehadroncolliderdestroyedtheworldyet.com/",
                "http://ninjaflex.com/",
                "http://ihasabucket.com/",
                "http://corndogoncorndog.com/",
                "http://www.hackertyper.com/",
                "https://pointerpointer.com",
                "http://imaninja.com/",
                "http://drawing.garden/",
                "http://www.ismycomputeron.com/",
                "http://www.nullingthevoid.com/",
                "http://www.muchbetterthanthis.com/",
                "http://www.yesnoif.com/",
                "http://lacquerlacquer.com",
                "http://potatoortomato.com/",
                "http://iamawesome.com/",
                "https://strobe.cool/",
                "http://www.pleaselike.com/",
                "http://crouton.net/",
                "http://corgiorgy.com/",
                "http://www.wutdafuk.com/",
                "http://unicodesnowmanforyou.com/",
                "http://chillestmonkey.com/",
                "http://scroll-o-meter.club/",
                "http://www.crossdivisions.com/",
                "http://tencents.info/",
                "http://www.patience-is-a-virtue.org/",
                "http://pixelsfighting.com/",
                "http://isitwhite.com/",
                "https://existentialcrisis.com/",
                "http://onemillionlols.com/",
                "http://www.omfgdogs.com/",
                "http://oct82.com/",
                "http://chihuahuaspin.com/",
                "http://www.blankwindows.com/",
                "http://dogs.are.the.most.moe/",
                "http://tunnelsnakes.com/",
                "http://www.trashloop.com/",
                "http://www.ascii-middle-finger.com/",
                "http://spaceis.cool/",
                "http://www.donothingfor2minutes.com/",
                "http://buildshruggie.com/",
                "http://buzzybuzz.biz/",
                "http://yeahlemons.com/",
                "http://wowenwilsonquiz.com",
                "https://thepigeon.org/",
                "http://notdayoftheweek.com/",
                "http://www.amialright.com/",
                "http://nooooooooooooooo.com/",
                "https://greatbignothing.com/",
                "https://zoomquilt.org/",
                "https://dadlaughbutton.com/",
                "https://www.bouncingdvdlogo.com/",
                "https://remoji.com/",
                "http://papertoilet.com/"]
        await ctx.send(random.choice(usless))
        

    #*Gives size of member's little guy
    @commands.command()
    async def size(self, ctx, member: discord.Member = None):
        member = ctx.author if member == None else member
        await ctx.send(f'{member.mention}\'s friend is this size: 8{random.randint(3,15)*"="}D')
    
    @size.error
    async def size_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send("Okay... *shakes his head*... Please tell me what that is, because that's not a person for sure")
            await ctx.send("*Sighs*.. just type that`size [@bigman]`")
    
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
        "You always bring me so much joy as soon as you leave the room.",
        "I was hoping for a battle of wits but it would be wrong to attack someone who’s totally unarmed.",
        "I’d tell you how I really feel, but I wasn’t born with enough middle fingers to express myself in this case.",
        "Stupidity’s not a crime, so feel free to go.",
        "I’d tell you to go fuck yourself, but that would be cruel and unusual punishment."]
        await ctx.send(random.choice(roasts))

    @roast.error
    async def roasts_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send("Who? Is the questions! WHO?")
            await ctx.send("`roast [@theguywhoreallypissesyouoff]`")


def setup(client):
    await client.add_cog(Fun(client))
