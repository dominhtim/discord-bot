import os
import random
import discord
import asyncio

from discord.ext import commands
from dotenv import load_dotenv
from discord import FFmpegPCMAudio
from discord.utils import get

load_dotenv('.env')
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='.')


@bot.command(name='choose')
async def choose(ctx, *, choices):
    choices_array = choices.split(';')
    response = random.choice(choices_array)
    embed = discord.Embed(title=":thinking:", description=response)
    await ctx.send(embed=embed)


@bot.command(name='hentai')
async def hentai(ctx):
    embed = discord.Embed(title="Hentai", description="Kirito")
    embed.set_image(
        url='https://www.anime-planet.com/images/characters/kirito-30045.jpg')
    await ctx.send(embed=embed)


@bot.command(name='easy')
async def easy(ctx):
    response = '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'\
               '░░░░█▀▀▀░█▀▀█░█▀▀▀░█░░█░█░░░░\n'\
               '░░░░█▀▀▀░█▀▀█░▀▀▀█░▀██▀░▀░░░░\n'\
               '░░░░▀▀▀▀░▀░░▀░▀▀▀▀░░▀▀░░▀░░░░\n'\
               '░░░░░░░░░░░░░░░░░░░░░░░░░░░░░\n'
    await ctx.send(response)


@bot.command(name='bread')
async def bread(ctx):
    embed = discord.Embed(title="Bread", description="Bread")
    embed.set_image(
        url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fiheartrecipes.com%2Fwp-content%2Fuploads%2F2015%2F03%2FIMG_95911.jpg&f=1&nofb=1')
    await ctx.send(embed=embed)


@bot.command(name='sion')
async def sion(ctx):
    embed = discord.Embed(title="Sion", description="Best Champion in League")
    embed.set_image(url='https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fvignette.wikia.nocookie.net%2Fleagueoflegends%2Fimages%2Ff%2Ffc%2FSion_OriginalCentered.jpg%2Frevision%2Flatest%3Fcb%3D20180414203549&f=1&nofb=1')
    await ctx.send(embed=embed)


@bot.command(name='mike')
async def mike(ctx):
    response = 'fk u mike'
    await ctx.send(response)


@bot.command(name='cao')
async def cao(ctx):
    response = 'i miss you'
    await ctx.send(response)


@bot.command(name='joe')
async def joe(ctx):
    response = 'the spaghettisburg address'
    await ctx.send(response)


@bot.command(name='lev')
async def lev(ctx):
    response = 'no one likes you'
    await ctx.send(response)


@bot.command(name='ryan')
async def ryan(ctx):
    response = 'you\'re a nerd'
    await ctx.send(response)


@bot.command(name='andrew')
async def andrew(ctx):
    response = 'i did nothing wrong. joe was wrong.'
    await ctx.send(response)


@bot.command(name='rahul')
async def rahul(ctx):
    response = 'What the fuck did you just fucking say about me, you little bitch? I\'ll have you know I graduated top of my class in the Navy Seals, and I\'ve been involved in numerous secret raids on Al-Quaeda, and I have over 300 confirmed kills.'
    await ctx.send(response)


@bot.command(name='plspenis')
async def plspenis(ctx):
    author = ctx.message.author
    user_name = author.name
    length = random.randint(0, 10)
    penis = "8"
    for i in range(length):
        penis += "="
    penis += "D"
    embed = discord.Embed(title="{}'s Penis".format(
        user_name), description=penis)
    await ctx.send(embed=embed)


@bot.command(name='voice')
async def voice(ctx, voice_index: int):
    channel = ctx.message.author.voice.channel
    if not channel:
        await ctx.send("You are not connected to a voice channel")
        return
    voice = get(bot.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    if voice.is_playing():
        return
    source = FFmpegPCMAudio(voice_clip(voice_index))
    voice.play(source)
    while voice.is_playing():
        await asyncio.sleep(1)
    voice.stop()
    await voice.disconnect()


def voice_clip(voice_index):
    voice_map = {0: "voice/WDYW.mp3",
                 1: "voice/MONEY_MONEY.mp3",
                 2: "voice/soy.mp3",
                 3: "voice/Dance_the_Shape_Away.mp3",
                 4: "voice/video-1460446568.mp3"}
    return voice_map[voice_index]


bot.run(TOKEN)
