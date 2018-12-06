import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
import os
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_member_join(member):
    print('Recognised that a member called ' + member.name + ' joined')
    await client.send_message(member, 'Welcome to Little_cs Fan Club, make sure to read the rules and have a good time.')
    print('Sent message to ' + member.name)

@client.event
async def on_ready():
    await client.change_presence(game=Game(name='you live', type = 3))
    print('Ready, Freddy')

client.run(os.getenv('TOKEN'))
