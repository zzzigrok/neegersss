import discord
import os
from discord.ext import commands
import colorama
import requests
import discord
import requests
import json
import discord
from discord import member
from discord.ext import commands




from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from os import system


from colorama import Fore, Style, init

import random
from discord import Permissions
from colorama import Fore, Style
import asyncio
import discord
import time
import random
import asyncio
import datetime
import os
from discord.ext import commands
import random
import asyncio
import itertools
import sys
import traceback
from async_timeout import timeout
from functools import partial

import json
import inspect
import aiohttp
import datetime
import threading
from discord import Permissions
from discord import client
from discord.ext import commands
from discord.utils import get
from threading import Thread
import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import keep_alive
from random import choice
from time import sleep
import discord, random, aiohttp, asyncio
from colorama import Fore, init
import discord
import time
import random
import asyncio
import asyncio
from typing import Optional, Set
import datetime
import functools
import io
import json
import os
import random
import re
import string
import urllib.parse
import urllib.request
import time
import requests
import webbrowser
import os
import sys
import threading
from pyrandmeme import *
import time
import datetime
import subprocess
from urllib import parse, request
from itertools import cycle
from bs4 import BeautifulSoup as bs4

import aiohttp
import colorama
import discord

import requests

from colorama import Fore
from discord.ext import commands
from discord.utils import get
import os
import threading
import time
from discord import client
from discord.ext import commands
from discord.utils import get
from threading import Thread
from time import sleep
from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Button, Style
from tkinter import *

import re
import os
import discord
from discord.ext import commands
import random
from discord import Permissions
from colorama import Fore, Style
import asyncio

import discord
from discord import *
from discord.ext import commands
import asyncio
import time
from random import randint
import random
import string
import os
import requests
import datetime
from asyncio import sleep
import discord
import json
import discord
#импорты
bot = commands.Bot(command_prefix = '+')
bot.remove_command('help')
   

@bot.group(invoke_without_command= True)
@commands.cooldown(1, 3, commands.BucketType.user)    
async def help(ctx):
    # insert your help command embed or message here
    embed= discord.Embed(title="Хелп", description="Хелп команды", color=discord.Color.red())
    embed.add_field(name="пожалуйста напиши модуль.", value="пример: help modules")
    embed.set_image(url = 'https://media.discordapp.net/attachments/943933147375083654/945285528973086740/1581155354_vsthemes_ru-12.jpg?width=1182&height=655')
    embed.set_footer(text=f'От LunarBot',icon_url= f"https://media.discordapp.net/attachments/944926251280367616/945358689605398558/unknown-21.png")
    await ctx.send(embed=embed)

@help.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
async def modules(ctx):
    embed = discord.Embed(
        title = 'команда поддержки',
        description = 'Команда help moderation выполняет команды модерации.\nКоманда help fun выполняет команды веселья.',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    embed.set_image(url = 'https://media.discordapp.net/attachments/943933147375083654/945285528973086740/1581155354_vsthemes_ru-12.jpg?width=1182&height=655')
    embed.set_footer(text=f'От LunarBot',icon_url= f"https://media.discordapp.net/attachments/944926251280367616/945358689605398558/unknown-21.png")  
    await ctx.send(embed=embed)

    
@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
async def ban(ctx, member: discord.Member):
   await ctx.guild.ban(member, reason = None)



@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
async def kick(ctx, member: discord.Member):
   await ctx.guild.kick(member, reason = None)


@bot.command(aliases = ['мьют', 'мут'])
@commands.cooldown(1, 3, commands.BucketType.user)    
@commands.has_permissions(administrator=True)
@commands.has_permissions(manage_messages = True)
@commands.has_permissions(manage_channels = True)
async def mute(ctx, member: discord.Member = None, amout: str = None, *, reason = None):
    times_start = datetime.datetime.today()
    emb_user = discord.Embed(title = '**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
    emb_user.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
    emb_user.add_field(name = '**Причина:**', value = reason, inline = False)
    emb_user.add_field(name = '**Длительность:**', value = amout, inline = False)
    emb_user.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)
    emb_user.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
 
    emb_user_stop = discord.Embed(title = '**PlanetBot - Unmute**', colour = discord.Colour.from_rgb(255, 0, 0))
    emb_user_stop.add_field(name = '**Снял:**', value = ctx.author.mention, inline = False)
    emb_user_stop.add_field(name = '**Сервер:**', value = ctx.guild.name, inline = False)
    emb_user_stop.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
    guild = ctx.guild
    await guild.create_role(name="PlanetBot Muted")
    mute_role = discord.utils.get(ctx.guild.roles, name="PlanetBot Muted")


    
        

 
    if member is None:
        emb = discord.Embed(title = 'Planet Bot error mute', description = f'{ctx.author.mention}, Укажите пользователя!', colour = discord.Colour.from_rgb(255, 0, 0))
        emb.add_field(name = 'Пример:', value = f'{ctx.prefix}мьют [@участник] <время(с, м)> [причина]', inline = False)
        emb.add_field(name = 'Пример 1:', value = f'{ctx.prefix}мьют @test 40м пример')
        emb.add_field(name = 'Время:', value = f'с - секунды\nм - минуты\n')
 
        await ctx.send(embed = emb)
    else:
        end_time = amout[-1:]
        time = int(amout[:-1])
        if time <= 0:
            emb = discord.Embed(title = 'Planet Bot error mute', description = f'{ctx.author.mention}, Время не может быть меньше 1!', colour = discord.Colour.from_rgb(255, 0, 0))
            emb.add_field(name = 'Пример:', value = f'{ctx.prefix}мьют [@участник] <время> [причина]', inline = False)
            emb.add_field(name = 'Пример 1:', value = f'{ctx.prefix}мьют @Xpeawey 1ч пример')
            emb.add_field(name = 'Время:', value = f'с - секунды\nм - минуты\nч - часы\nд - дни')
 
            await ctx.send(embed = emb)
        else:
            if end_time == 'с':
                if reason is None:
                    emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                    emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
                    emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
                    emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
                    emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
                    emb.add_field(name = 'Длительность:', value = '{} секунд'.format(time))
                    emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                    await member.add_roles(mute_role)
                    await ctx.send(embed = emb)
                    await member.send(embed = emb_user)
                    await asyncio.sleep(time)
                    await member.remove_roles(mute_role)
                    await member.send(embed = emb_user_stop)
                else:
                    emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                    emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
                    emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
                    emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
                    emb.add_field(name = 'Причина:', value = reason, inline = False)
                    emb.add_field(name = 'Длительность:', value = '{} секунд'.format(time))
                    emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                    await member.add_roles(mute_role)
                    await ctx.send(embed = emb)
                    await member.send(embed = emb_user)
                    await asyncio.sleep(time)
                    await member.remove_roles(mute_role)
                    await member.send(embed = emb_user_stop)
            elif end_time == 'м':
                if reason is None:
                    emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                    emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
                    emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
                    emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
                    emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
                    emb.add_field(name = 'Длительность:', value = '{} минут'.format(time))
                    emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                    await member.add_roles(mute_role)
                    await ctx.send(embed = emb)
                    await member.send(embed = emb_user)
                    await asyncio.sleep(time *60)
                    await member.remove_roles(mute_role)
                    await member.send(embed = emb_user_stop)
                else:
                    emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                    emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
                    emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
                    emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
                    emb.add_field(name = 'Причина:', value = reason, inline = False)
                    emb.add_field(name = 'Длительность:', value = '{} минут'.format(time))
                    emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                    await member.add_roles(mute_role)
                    await ctx.send(embed = emb)
                    await member.send(embed = emb_user)
                    await asyncio.sleep(time *60)
                    await member.remove_roles(mute_role)
                    await member.send(embed = emb_user_stop)
            elif end_time == 'ч':
                if reason is None:
                    if time == '1':
 
                        emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                        emb.add_field(name = 'Выдал:', value = ctx.author.mention, inline = False)
                        emb.add_field(name = 'Нарушитель:', value = member.mention, inline = False)
                        emb.add_field(name = 'ID нарушителя:', value = member.id, inline = False)
                        emb.add_field(name = 'Причина:', value = 'Не указано', inline = False)
                        emb.add_field(name = 'Длительность:', value = '{} час'.format(time))
                        emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                        await member.add_roles(mute_role)
                        await ctx.send(embed = emb)
                        await member.send(embed = emb_user)
                        await asyncio.sleep(time *60 *60)
                        await member.remove_roles(mute_role)
                        await member.send(embed = emb_user_stop)
                    elif time == '4' or time == '3' or time == '2':
                        emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                        emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
                        emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
                        emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
                        emb.add_field(name = '**Причина:**', value = 'Не указано', inline = False)
                        emb.add_field(name = '**Длительность:**', value = '{} часов'.format(time))
                        emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                        await member.add_roles(mute_role)
                        await ctx.send(embed = emb)
                        await member.send(embed = emb_user)
                        await asyncio.sleep(time *60 *60)
                        await member.remove_roles(mute_role)
                        await member.send(embed = emb_user_stop)
                    elif time >= '5':
                        emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                        emb.add_field(name = '**Выдал:', value = ctx.author.mention, inline = False)
                        emb.add_field(name = '**Нарушитель:', value = member.mention, inline = False)
                        emb.add_field(name = '**ID нарушителя:', value = member.id, inline = False)
                        emb.add_field(name = '**Причина:', value = 'Не указано', inline = False)
                        emb.add_field(name = '**Длительность:', value = '{} часов'.format(time))
                        emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                        await member.add_roles(mute_role)
                        await ctx.send(embed = emb)
                        await member.send(embed = emb_user)
                        await asyncio.sleep(time *60 *60)
                        await member.remove_roles(mute_role)
                        await member.send(embed = emb_user_stop)
                else:
                    if time == '1':
                        emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                        emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
                        emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
                        emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
                        emb.add_field(name = '**Причина:**', value = reason, inline = False)
                        emb.add_field(name = '**Длительность:**', value = '{} час'.format(time))
                        emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                        await member.add_roles(mute_role)
                        await ctx.send(embed = emb)
                        await member.send(embed = emb_user)
                        await asyncio.sleep(time *60 *60)
                        await member.remove_roles(mute_role)
                        await member.send(embed = emb_user_stop)
                    elif time == '4' or time == '3' or time == '2':
                        emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                        emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
                        emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
                        emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
                        emb.add_field(name = '**Причина:**', value = reason, inline = False)
                        emb.add_field(name = '**Длительность:**', value = '{} часа'.format(time))
                        emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
                        await member.add_roles(mute_role)
                        await ctx.send(embed = emb)
                        await member.send(embed = emb_user)
                        await asyncio.sleep(time *60 *60)
                        await member.remove_roles(mute_role)
                        await member.send(embed = emb_user_stop)
                    elif time >= '5':
                        emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                        emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
                        emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
                        emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
                        emb.add_field(name = '**Причина:**', value = reason, inline = False)
                        emb.add_field(name = '**Длительность:**', value = '{} часов'.format(time))
                        emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
 
                        await member.add_roles(mute_role)
                        await ctx.send(embed = emb)
                        await member.send(embed = emb_user)
                        await asyncio.sleep(time *60 *60)
                        await member.remove_roles(mute_role)
                        await member.send(embed = emb_user_stop)
            elif time == 'д':
                if reason is None:
                    emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                    emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
                    emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
                    emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
                    emb.add_field(name = '**Причина:**', value = 'Не указано', inline = False)
                    emb.add_field(name = '**Длительность:**', value = '{} день(ей)'.format(time))
                    emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
 
                    await member.send(embed = emb_user)
                    await member.add_roles(mute_role)
                    await ctx.send(embed = emb)
                    await member.send(embed = emb_user)
                    await asyncio.sleep(time *60 *60 *24)
                    await member.remove_roles(mute_role)
                    await member.send(embed = emb_user_stop)
                else:
                    emb = discord.Embed(title = f'**Planet Bot mute**', colour = discord.Colour.from_rgb(255, 0, 0))
                    emb.add_field(name = '**Выдал:**', value = ctx.author.mention, inline = False)
                    emb.add_field(name = '**Нарушитель:**', value = member.mention, inline = False)
                    emb.add_field(name = '**ID нарушителя:**', value = member.id, inline = False)
                    emb.add_field(name = '**Причина:**', value = reason, inline = False)
                    emb.add_field(name = '**Длительность:**', value = '{} день(ей)'.format(time), inline = False)
                    emb.set_footer(text = f'Дата: {times_start.strftime("%Y-%m-%d, %H:%M:%S")}')
 
                    await member.add_roles(mute_role)
                    await ctx.send(embed = emb)
                    await member.send(embed = emb_user)
                    await asyncio.sleep(time *60 *60 *24)
                    await member.remove_roles(mute_role)
                    await member.send(embed = emb_user_stop)




@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
@commands.has_permissions(manage_channels = True)
async def lock(ctx):
          overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
          overwrite.send_messages = False
          await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
          await ctx.send(ctx.channel.mention + "был заблакирован 🔒")
          await ctx.message.add_reaction('🔒')


@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
@commands.has_permissions(manage_channels = True)
async def unlock(ctx):
          overwrite = ctx.channel.overwrites_for(ctx.guild.default_role)
          overwrite.send_messages = True
          await ctx.channel.set_permissions(ctx.guild.default_role, overwrite=overwrite)
          await ctx.send(ctx.channel.mention + "был разблокирован 🔓")
          await ctx.message.add_reaction('🔓')




@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
async def support(ctx):
  embed = discord.Embed(
  title = 'Planet Bot',
  description = 'Наш сервер поддержки https://discord.gg/uukbbEZw3h',
  colour = discord.Colour.from_rgb(255, 0, 0)
  )
  embed.set_image(url = 'https://media.discordapp.net/attachments/943933147375083654/945285528973086740/1581155354_vsthemes_ru-12.jpg?width=1182&height=655')
  embed.set_footer(text=f'От PlanetBot',icon_url= f"https://media.discordapp.net/attachments/944926251280367616/945358689605398558/unknown-21.png")
  await ctx.send(embed=embed)


@help.command()
async def fun(ctx):
    embed=discord.Embed(title="PlanetBot", url="", description="", color=discord.Color.red())
    embed.add_field(name="8ball", value="магический шар предсказаний", inline=True)
    embed.add_field(name="slot", value="слот машина", inline=True)    
    embed.set_image(url = 'https://media.discordapp.net/attachments/943933147375083654/945285528973086740/1581155354_vsthemes_ru-12.jpg?width=1182&height=655')
    embed.set_footer(text=f'От PlanetBot',icon_url= f"https://media.discordapp.net/attachments/944926251280367616/945358689605398558/unknown-21.png")
    await ctx.send(embed=embed)
    
    
@help.command()
async def moderation(ctx):
    embed=discord.Embed(title="PlanetBot", url="", description="", color=discord.Color.red())
    embed.add_field(name="lock", value="заблокировать канал", inline=True)
    embed.add_field(name="unlock", value="разблокировать канал", inline=True)    
    embed.add_field(name="mute", value="мьют", inline=True)
    embed.add_field(name="ban", value="бан участника", inline=True)  
    embed.set_image(url = 'https://media.discordapp.net/attachments/943933147375083654/945285528973086740/1581155354_vsthemes_ru-12.jpg?width=1182&height=655')
    embed.set_footer(text=f'От PlanetBot',icon_url= f"https://media.discordapp.net/attachments/944926251280367616/945358689605398558/unknown-21.png")  
    await ctx.send(embed=embed)
 
 
@bot.event
async def on_guild_join(guild):
    text_channels = guild.text_channels
    if text_channels:
        channel = text_channels[0]

    embed = discord.Embed(
        title = 'Lunar Bot',
        description = '**Привет! | я бот Planet. Наш создатель !     Billy / FZL#0396. Сообщайте нам о багах недоработках и т.д, наши команды +help | И наш сервер с поддежркой тут: https://discord.gg/Gas7Exekk5**',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await channel.send(embed=embed)


@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
async def send(ctx, message):
    embed = discord.Embed(
        title = f'{message}',
        description = '',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    await ctx.send(embed=embed)
    
@bot.command(aliases=['8ball'])
@commands.cooldown(1, 3, commands.BucketType.user)    
async def _8ball(ctx, *, question):
  responses = ["Несомненно",
        "Совершенно верно",
        "Без сомнения",
        "Определенно да",
        "Сконцентрируйся и спроси еще раз",
        "Не рассчитывай на это",
        "Нет",
        "Скорее всего нет",
        "Точно нет!"]
  await ctx.send(f'{random.choice(responses)}')


@bot.command(aliases=['slots', "slotmachine"])
@commands.cooldown(1, 3, commands.BucketType.user)    
async def slot(ctx):
    await ctx.message.delete()
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} Молодец! у тебя совпали все фигуры!"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} выполо 2 фигуры ты выйграл!"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} Ты проиграл!"}))

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
async def server_info(ctx):
  members = ctx.guild.members
  allchannels = len(ctx.guild.channels)
  allroles = len(ctx.guild.roles)
  allmembers = len(ctx.guild.members)
  allvoice = len(ctx.guild.voice_channels)
  alltext = len(ctx.guild.text_channels)
  embed = discord.Embed(
    title = f'{ctx.guild.name}',
    description = f'**Сервер**\nВсего каналов: {allchannels}\nВсего ролей: {allroles}\nВсего участников: {allmembers}\nВсего Войс каналов: {allvoice}\nВсего текстовых каналов: {alltext}\n**Участников**\nВсего участников: {allmembers}\n**Другое**\nСоздатель: {ctx.guild.owner}\n',
    colour = discord.Colour.from_rgb(255, 0, 0)
  )
  embed.set_thumbnail(
    url=ctx.guild.icon_url)
  embed.set_footer(
   text=f'ID Сервера: {ctx.guild.id}') 
  embed.set_image(url="https://cdn.discordapp.com/attachments/940584688748216401/940901637743083530/discord_avatarka.jpg")
  await ctx.send(embed=embed)


@bot.command()
async def servers(ctx):
    servers = len(bot.guilds)
    embed = discord.Embed(
        title = 'Planet Bot',
        description = f'я нахожусь на {servers} серверах',
        colour = discord.Colour.from_rgb(255, 0, 0)
    )
    embed.set_image(url = 'https://media.discordapp.net/attachments/943933147375083654/945285528973086740/1581155354_vsthemes_ru-12.jpg?width=1182&height=655')
    embed.set_footer(text=f'От LunarBot',icon_url= f"https://media.discordapp.net/attachments/944926251280367616/945358689605398558/unknown-21.png")  
    await ctx.send(embed=embed)

@bot.command(pass_context=True)
@commands.cooldown(1, 3, commands.BucketType.user)    
async def mems(ctx):
    embed = discord.Embed(title="", description="")
    async with aiohttp.ClientSession() as cs:
        async with cs.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
            res = await r.json()
            embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
            await ctx.send(embed=embed)


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        names = Embed(title = '⚠️ | Подожди 3 секунды что бы у тебя прошёл cooldown', colour = discord.Colour.from_rgb(255, 0, 0))
        new_names = Embed(title = '✅ | твой cooldown прошёл', colour = discord.Colour.from_rgb(0, 255, 1))
        msg = await ctx.send(embed=names)
        time.sleep(3)
        await msg.edit(embed=new_names)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.user)    
async def reload(ctx):
    reload1 = Embed(title = 'Перезагрузка бота', description = 'бот перезагружен на 10 процентов', colour = discord.Colour.from_rgb(255, 0, 0))
    reload2 = Embed(title = 'Перезагрузка бота', description = 'бот перезагружен на 15 процентов', colour = discord.Colour.from_rgb(255, 0, 0))
    reload3 = Embed(title = 'Перезагрузка бота', description = 'бот перезагружен на 25 процентов', colour = discord.Colour.from_rgb(255, 0, 0))
    reload4 = Embed(title = 'Перезагрузка бота', description = 'бот перезагружен на 45 процентов', colour = discord.Colour.from_rgb(255, 0, 0))
    reload5 = Embed(title = 'Перезагрузка бота', description = 'бот перезагружен на 60 процентов', colour = discord.Colour.from_rgb(255, 0, 0))
    reload6 = Embed(title = 'Перезагрузка бота', description = 'бот перезагружен на 75 процентов', colour = discord.Colour.from_rgb(255, 0, 0))
    reload7 = Embed(title = 'Перезагрузка бота', description = 'бот перезагружен на 95 процентов', colour = discord.Colour.from_rgb(255, 0, 0))
    reload8 = Embed(title = 'Перезагрузка бота', description = 'бот перезагружен на 100 процентов', colour = discord.Colour.from_rgb(255, 0, 0))
    msg = await ctx.send(embed=reload1)
    time.sleep(1)
    await msg.edit(embed=reload2)
    time.sleep(3)
    await msg.edit(embed=reload3)
    time.sleep(5)
    await msg.edit(embed=reload4)
    time.sleep(7)
    await msg.edit(embed=reload5)
    time.sleep(9)
    await msg.edit(embed=reload6)
    time.sleep(11)
    await msg.edit(embed=reload7)
    time.sleep(13)
    await msg.edit(embed=reload8)

@bot.command()
@commands.cooldown(1, 3, commands.BucketType.guild)
async def youtube(msg, *, search):
    query_string = urllib.parse.urlencode({
        "search_query": search
    })
    html_content = urllib.request.urlopen(
        "http://www.youtube.com/results?" + query_string
    )
    search_results = re.findall(r"watch\?v=(\S{11})", html_content.read().decode())
    await msg.send("http://www.youtube.com/watch?v=" + search_results[0])





@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="PlanetBot | +help"))

token = 'OTMwMTY4NzM3NDM5NTYzODU2.G5QvHo.4G8U73ABisXkwEHt8kBEs5OqL2X_4p92Seb7BQ'
keep_alive.keep_alive()
bot.run(token)
