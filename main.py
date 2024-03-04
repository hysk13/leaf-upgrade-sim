# Run This File

import discord
from discord.ext import commands

client = commands.Bot(command_prefix="/", intents=discord.Intents.all())


@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

  await client.load_extension('commands.about')
  await client.load_extension('commands.account')
  await client.load_extension('commands.leaf')
  await client.load_extension('commands.character')
  await client.load_extension('commands.shop')

  await client.tree.sync()


@client.event
async def on_message(message):
  if message.author == client.user:
    return

f = open('./token.txt', 'r')
client.run(f.read())
