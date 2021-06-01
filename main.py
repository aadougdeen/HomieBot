import os
import discord
from discord.ext import commands
import pymongo
from pymongo import MongoClient

client = MongoClient("MONGOCLIENT")
db = client["discordbot"]
collection = db["characters"]

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print('Bot is online.')

@client.command()
async def load(ctx, extension):
    client.load_extension(f'commands.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'commands.{extension}')

for filename in os.listdir('./commands'):
    if filename.endswith('.py'):
        client.load_extension(f'commands.{filename[:-3]}')


client.run('TOKEN')


