import os
import random
import discord
import asyncio
import logging
import sqlite3
from datetime import datetime

from discord.ext import commands
from discord import FFmpegPCMAudio
from discord.utils import get

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix='.', intents=intents)

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Running bot')

connection = sqlite3.connect('/data/celebrations.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS celebrations (
                    name TEXT NOT NULL,
                    date DATE NOT NULL,
                    celebrated BOOLEAN NOT NULL
                  )''')
connection.commit()

@bot.command(name='celebration')
async def add_celebration(ctx, *, name):
    current_date = datetime.now().date()
    # sql injection isn't real
    cursor.execute('''
        INSERT INTO celebrations (name, date, celebrated)
        VALUES (?, ?, ?)
        ''', (name, current_date, False))
    connection.commit()
    response = f"added {name} to celebrations"
    await ctx.send(response)


@bot.command(name='celebrations')
async def print_uncelebrated(ctx):
    cursor.execute(''' SELECT name, date FROM celebrations WHERE celebrated = 0 ORDER BY date ''')
    celebrations = ""
    for name, date in cursor.fetchall():
        celebrations += f"{date}: {name}\n"
    await ctx.send(celebrations)


@bot.command(name='celebrate')
async def celebrate(ctx, *, name):
    cursor.execute(''' UPDATE celebrations SET celebrated = 1 WHERE name = ? ''', (name,))
    connection.commit()
    if cursor.rowcount == 0:
        response = f"{name} isn't in the queue"
    else:
        response = f"🎉 {name} 🎉"
    await ctx.send(response)


@bot.command(name='pinglev')
async def pinglev(ctx):
    async for m in ctx.guild.fetch_members(limit=100):
        if "Lev" in m.name:
            channel = await m.create_dm()
            msg = await channel.send("Message Content Hidden")
            await asyncio.sleep(2)
            await msg.delete()
            await asyncio.sleep(2)


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
    file_list = os.listdir("voice")
    file_list = ["voice/" + file for file in file_list]
    return file_list[voice_index]


bot.run(TOKEN)
