import discord
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import colorsys
import random
import platform
from discord import Game, Embed, Color, Status, ChannelType
import os
import functools
import time
import datetime
import requests
import json
import aiohttp


async def status_task():
    while True:
        await client.change_presence(game=discord.Game(name='Destruction of Gotham City', type=3))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='Death of Batman', type=2))
        await asyncio.sleep(5)
      
Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)
client = commands.Bot(description="The Laughing Clown BOT", command_prefix=commands.when_mentioned_or("%"), pm_help = True)
client.remove_command('help')



@client.event
async def on_ready():
    print('Logged in as '+client.user.name+' (ID:'+client.user.id+') | Connected to '+str(len(client.servers))+' servers | Connected to '+str(len(set(client.get_all_members())))+' users')
    print('-----')
    print('-----')
    print("Created by I'm Joker")
    client.loop.create_task(status_task())


@client.command(pass_context = True)
async def quote(ctx):
    choices = ["**Smile, because it confuses people. Smile, because it's easier than explaining what is killing you inside. - THE JOKER**", "**As you know, madness is like gravity...all it takes is a little push. - THE JOKER**", "**If you’re good at something, never do it for free. - THE JOKER**", "**Nobody panics when things go “according to plan”. Even if the plan is horrifying! - THE JOKER**", "**Introduce a little anarchy. Upset the established order, and everything becomes chaos. I'm an agent of chaos... - THE JOKER**", "**Do I really look like a guy with a plan? You know what I am? I'm a dog chasing cars. I wouldn't know what to do with one if I caught it! You know, I just... *do* things. - THE JOKER**", "**What doesn't kill you, simply makes you stranger! - THE JOKER**", "**Why so serious? >:) - THE JOKER**", "**They Laugh At me Because I'm Different. I laugh At Them Because The're all the same - THE JOKER**", "**Their morals, their code; it's a bad joke. Dropped at the first sign of trouble. They're only as good as the world allows them to be. You'll see- I'll show you. When the chips are down these, uh, civilized people? They'll eat each other. See I'm not a monster, I'm just ahead of the curve. - THE JOKER**", "**The only sensible way to live in this world is without rules. - THE JOKER**"]
    embed = discord.Embed(title = " ", description = "**RIP Heath Ledger.... You've gave us a memorable gift like JOKER... We can't forget you...**", color=0XFF69B4)
    embed.add_field(name="Here's a quote of JOKER for you....", value = random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/531162741281521665/Heath_Ledger.png')
    embed.set_footer(text=f'Requested by {ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context = True)
async def botinfo(ctx):
    embed=discord.Embed(title="Details of this BOT...", description="Here are the details of this BOT below", color=0XFF69B4)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_author(name="This is Official BOT of REFORMED server")
    embed.add_field(name="__**Creator**__", value="__**@I'm Joker#7475**__", inline = True)
    embed.add_field(name="__**Special Thanks To**__", value="__**@marcos.#0290**__")
    embed.add_field(name="**Currently connected servers**", value=str(len(client.servers)), inline = True)
    embed.add_field(name="**Currently connected users**", value=str(len(set(client.get_all_members()))), inline = True)
    embed.add_field(name="If you have any queries about this BOT, DM me...", value="**@I'm Joker#7475**")
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)



@client.command(pass_context = True)
async def fams(ctx):
    choices = ['https://media.giphy.com/media/zDAqUralC0HU4/giphy.gif', 'https://media.giphy.com/media/pz1s2IpdQh86k/giphy.gif', 'https://media.giphy.com/media/1LnQIODGufGec/giphy.gif', 'https://media.giphy.com/media/yROJ5dn5IhR5u/giphy.gif', 'https://media.giphy.com/media/SjWEmbTtlOwcU/giphy.gif', 'https://media.giphy.com/media/396CPbx4g1o9W/giphy.gif', 'https://media.giphy.com/media/mXz3v0UdjrNTO/giphy.gif', 'https://media.giphy.com/media/XAr3mee7JuXYc/giphy.gif', 'https://media.giphy.com/media/12I9y6on09avza/giphy.gif', 'https://media.giphy.com/media/zBdfuQVMClAis/giphy.gif']
    embed = discord.Embed(title = "Hello {}, Here's your GIF....".format(ctx.message.author.name), description = " ", color=0XFF69B4)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.set_image(url=random.choice(choices))
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def askquestion(ctx):
    channel = client.get_channel('531837376562069514')
    channel2 = client.get_channel('525391238472663071')
    channel3 = '525391238472663071'
    role = '<@&516303012671520769>'
    embed = discord.Embed(title = "Here's a funny question for you... ", description = "**What's the first game you played in a PC?** \n Post your answer in "+str(channel)+" channel.Thank you for your valuable time. \n Sorry for ping...", color=0XFF69B4)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.timestamp = datetime.datetime.utcnow()
    embed.set_footer(text=f'Question by {ctx.message.author}', icon_url=f'{ctx.message.author.avatar_url}')
    await client.send_message(channel, role, embed=embed)


@client.command(pass_context = True)
async def avatar(ctx, user: discord.Member=None):
    if user is None:
        embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=0XFF69B4)
        embed.add_field(name='User: {}'.format(ctx.message.author.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png') 
        embed.set_image(url = ctx.message.author.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f'{ctx.message.author.avatar_url}')
        embed.timestamp = datetime.datetime.utcnow()
        await client.say(embed=embed)
    else:
        embed = discord.Embed(title=f'Avatar', description="Here's your avatar that you've requested...\n Don't misuse this cmd...", color=0XFF69B4)
        embed.add_field(name='User: {}'.format(user.name), value='Avatar:', inline=True)
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png') 
        embed.set_footer(text=f"Requested by {ctx.message.author.name}", icon_url=f"{ctx.message.author.avatar_url}")
        embed.timestamp = datetime.datetime.utcnow()
        embed.set_image(url = user.avatar_url)
        await client.say(embed=embed)

@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def poll(ctx, question, *options:str):
    if len(options) <=1:
        await client.say('Joker needs more than one option to conduct poll!!')
        return
    if len(options) > 10:
        await client.say("Joker Can't accept more than 10 options to conduct poll!")
        return

    if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
        reactions = ['👍', '👎']

    else:
        reactions = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '\U0001f51f']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
            embed = discord.Embed(title=question, description=''.join(description), color=0XFF69B4)
            react_message = await client.say(embed=embed)
        for reaction in reactions[:len(options)]:
            await client.add_reaction(react_message, reaction)
            embed.set_footer(text='poll ID: {}'.format(react_message.id))
            await client.edit_message(react_message, embed=embed)


@client.event
async def on_member_join(member):
    channel = client.get_channel('515997744842932229')
    text_channel = client.get_channel('516137272048091176')
    msg = "**Welcome to {}... Don't forget to read rules at {}... and don't break any of them... We hope you a good stay here...**".format(member.server.name, text_channel.mention)
    embed=discord.Embed(title=f"Welcome {member.name} to {member.server.name}", description=f"**Hope you'll be active here... Read rules at {text_channel.mention} channel and don't break any of them...**", color=0XFF69B4)
    embed.set_thumbnail(url='https://media.giphy.com/media/OF0yOAufcWLfi/giphy.gif')
    embed.add_field(name="__**Thanks for joining our server**__", value="We hope you a good stay here....")
    embed.add_field(name="__**Time of joining**__", value=member.joined_at, inline=True)
    embed.add_field(name="__**Joining position**__", value='{}'.format(str(member.server.member_count)), inline=True)
    embed.set_footer(text="This bot is created by I'm Joker", icon_url='https://images-ext-1.discordapp.net/external/Dk4VE5l-ZiG1BjZpdw8sdnh7BKxg4wDx7wk52zwT63A/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/472128507150073871/7c6f4d51bb2f6a331f5fd0d9c5df0e5f.webp?width=536&height=536')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(member, msg)
    await client.send_message(channel, embed=embed)

@client.event
async def on_member_remove(member):
    channel = client.get_channel('515997993204187177')
    embed=discord.Embed(title=f"Good bye {member.name}... Hope you'll come back again to {member.server.name}", description="Thank you for being with us all these times...", color=0XFF69B4)
    embed.set_thumbnail(url='https://media.giphy.com/media/UQaRUOLveyjNC/giphy.gif')
    embed.add_field(name="__**Members Remaining**__", value='{}'.format(str(member.server.member_count)), inline=True)
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(channel, embed=embed)


@client.command(pass_context = True)
async def marvel(ctx):
    choices = ['https://media.giphy.com/media/F9hQLAVhWnL56/giphy.gif', 'https://media.giphy.com/media/l4FGrYKtP0pBGpBAY/giphy.gif', 'https://media.giphy.com/media/JzujPK0id34qI/giphy.gif', 'https://media.giphy.com/media/M9TuBZs3LIQz6/giphy.gif', 'https://media.giphy.com/media/3GnKKEw2v7bXi/giphy.gif', 'https://media.giphy.com/media/GR1WWKadM9m0g/giphy.gif', 'https://media.giphy.com/media/iBpq5SbrYiSTTSHO7z/giphy.gif', 'https://media.giphy.com/media/dJirXKRo0j1l0j9V9Q/giphy.gif', 'https://media.giphy.com/media/ZvkFmclQO1ImmRNm0K/giphy.gif', 'https://media.giphy.com/media/82Mksc7tnX3qp4FVNN/giphy.gif', 'https://media.giphy.com/media/mTQhl6cWXDJBu/giphy.gif']
    embed=discord.Embed(title="Hello {}... Here's your GIF...".format(ctx.message.author.name), description="This BOT is made by I'm Joker", color=0XFF69B4)
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name} ', icon_url=f'{ctx.message.author.avatar_url}')
    embed.set_image(url=random.choice(choices))
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)

@client.command(pass_context = True)
async def dc(ctx):
    choices = ['https://media.giphy.com/media/uDPSXySAEDv56/giphy.gif', 'https://media.giphy.com/media/26vIg1DlkNdJr65q0/giphy.gif', 'https://media.giphy.com/media/jcIRoyJKQG3za/giphy.gif', 'https://media.giphy.com/media/26xBLVi4RuhYmV6zm/giphy.gif', 'https://media.giphy.com/media/xUOwGfcrlRjKjs2sSI/giphy.gif', 'https://media.giphy.com/media/l41Yq5KYEmbxFaeVq/giphy.gif', 'https://media.giphy.com/media/3o7abJW5ZuiByDelji/giphy.gif', 'https://media.giphy.com/media/xU67CtAMi8f5K/giphy.gif', 'https://media.giphy.com/media/VXQuKHDhTIBWM/giphy.gif']
    embed=discord.Embed(title="Hello kryptonian... Here's your GIF...", color=0XFF69B4)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)



@client.command(pass_context = True)
async def joker(ctx):
    choices = ['https://media.giphy.com/media/KZd26L2o8QXtK/giphy.gif', 'https://media.giphy.com/media/aazZrFTMrDKLK/giphy.gif', 'https://media.giphy.com/media/F0A48Q2wFjE7S/giphy.gif', 'https://media.giphy.com/media/7waKDy5RbDYVG/giphy.gif', 'https://media.giphy.com/media/13m24iFmhomZi0/giphy.gif', 'https://media.giphy.com/media/zCP1GdPjxtCTe/giphy.gif', 'https://media.giphy.com/media/tN2OR1R1BLKV2/giphy.gif', 'https://media.giphy.com/media/X9Z0O2bpi8GMU/giphy.gif', 'https://media.giphy.com/media/YPIrsRqqO7oB2/giphy.gif', 'https://media.giphy.com/media/FSp1Wqx2TPYSA/giphy.gif', 'https://media.giphy.com/media/8UwEdwAF5XWQE/giphy.gif']
    embed=discord.Embed(title="Hello Joker fan... Here's a GIF for you...", description="Tribute to the legendary **Heath Ledger**", color=0XFF69B4)
    embed.set_image(url=random.choice(choices))
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/531162741281521665/Heath_Ledger.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(ctx.message.channel, embed=embed)


@client.command(pass_context = True)
async def meme(ctx):
    async with aiohttp.ClientSession() as session:
        async with session.get("https://api.reddit.com/r/me_irl/random") as r:
            data = await r.json()
            embed = discord.Embed(title='Meme',color=0XFF69B4)
            embed.set_image(url=data[0]["data"]["children"][0]["data"]["url"])
            embed.set_footer(text=f'Requested by: {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
            embed.timestamp = datetime.datetime.utcnow()
            await client.say(embed=embed)

@client.command(pass_context = True)
async def serverinvite(ctx):
    link = "**Thanks for joining in our server.... Invite your friends and tell them join the party too** \n https://discord.gg/gER47Jw"
    await client.send_message(ctx.message.channel, link)
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True)
async def announcement(ctx, matter):
    await client.send_message(ctx.message.channel, matter)
    
@client.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def clear(ctx, number):
 
    if ctx.message.author.server_permissions.manage_messages:
         mgs = [] #Empty list to put all the messages in the log
         number = int(number) #Converting the amount of messages to delete to an integer
    async for x in client.logs_from(ctx.message.channel, limit = number+1):
        mgs.append(x)            
       
    try:
        await client.delete_messages(mgs)          
        x = await client.say('`Joker has deleted '+str(number)+' messages for you...`')
        await asyncio.sleep(5)
        return await client.delete_message(x)
     
    except discord.Forbidden:
        await client.say(embed=Forbidden)
        return
    except discord.HTTPException:
        await client.say('clear failed.')
        return         
   
 
    await client.delete_messages(mgs)
    
@client.command(pass_context=True)
async def movie(ctx, *, name:str=None):
    await client.send_typing(ctx.message.channel)
    if name is None:
        embed=discord.Embed(description = "Please specify a movie, *eg. %movie Bohemian Rhapsody*", color = 0x3333cc)
        await client.say(embed=embed)
    key = "4210fd67"
    url = "http://www.omdbapi.com/?t={}&apikey={}".format(name, key)
    response = requests.get(url)
    x = json.loads(response.text)
    embed=discord.Embed(title = "**{}**".format(name).upper(), description = "Here is your movie {}".format(ctx.message.author.name), color = 0x3333cc)
    if x["Poster"] != "N/A":
     embed.set_thumbnail(url = x["Poster"])
    embed.add_field(name = "__Title__", value = x["Title"])
    embed.add_field(name = "__Released__", value = x["Released"])
    embed.add_field(name = "__Runtime__", value = x["Runtime"])
    embed.add_field(name = "__Genre__", value = x["Genre"])
    embed.add_field(name = "__Director__", value = x["Director"])
    embed.add_field(name = "__Writer__", value = x["Writer"])
    embed.add_field(name = "__Actors__", value = x["Actors"])
    embed.add_field(name = "__Plot__", value = x["Plot"])
    embed.add_field(name = "__Language__", value = x["Language"])
    embed.add_field(name = "__Imdb Rating__", value = x["imdbRating"]+"/10")
    embed.add_field(name = "__Type__", value = x["Type"])
    embed.set_footer(text = "Information from the OMDB API")
    await client.say(embed=embed)

@client.command(pass_context = True)
async def help(ctx):
    author = ctx.message.author
    embed=discord.Embed(title="__Command Prefix__: %", description='', color=0XFF69B4)
    embed.add_field(name="__**Summary**__", value="**This is the official BOT of REFORMED server. You can't find this BOT anywhere than here. This BOT is made in memory of JOKER \n And this BOT can't be distributed to anyone \n \n \n**", inline=True)
    embed.add_field(name="__**Commands**__", value="__**Fun Commands**__ \n `quote` - Quote of Joker \n `fams` - Random DragonBall Z GIF \n `marvel` - Random Marvel GIF \n `dc` - Random DC GIF \n `joker` - Random Joker GIF (Tribute to Heath Ledger) \n`meme` - Random funny meme \n `movie <movie name>` - Gives info of the particular movie you have searched \n \n __**Bot and server releated commands**__ \n `botinfo` - Information about this BOT \n `serverinvite` - Server invitation link \n \n __**Misc Commands**__ \n `avatar` - Avatar of the user \n `avatar <user>` - Avatar of mentioned user \n \n __**Admin Commands**__ \n `poll` - Polling (Administrator) \n `askquestion` - Asking of funny question (Administrator) \n `announce <matter>` - To announce the entered matter (Administrator) \n \n **More Feautures coming soon...** \n \n __**BOT will be offline someties... That means we are updating BOT**__ \n **Thank you for using this BOT**")
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/516953091656908810/519072295080296469/Joker.png')
    embed.set_footer(text=f'Requested by {ctx.message.author.name}', icon_url=f'{ctx.message.author.avatar_url}')
    embed.timestamp = datetime.datetime.utcnow()
    await client.send_message(author, embed=embed)
    
    
@client.command(pass_context = True)
@commands.has_permissions(administrator=True) 
async def announce(ctx, channel: discord.Channel=None, *, msg: str):
    if channel is None:
        await client.say(" ```Proper usage is\n\nannounce<channel><matter>```")
    else:
        await client.send_message(channel, msg)
  
        
@client.event
async def on_message(message):
    if message.content == "Hii":
        await client.send_message(message.channel, "Hello, How was your day? {}".format(message.author.mention))

                                  
                                  
client.run(os.getenv('Token'))
