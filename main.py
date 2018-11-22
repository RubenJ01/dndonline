import discord
import os
import random
import asyncio
import aiohttp
import json
import collections
from discord import Game
from discord.ext.commands import Bot 
from random import randrange


BOT_PREFIX = (";", "/")
client = Bot(command_prefix=BOT_PREFIX)


@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(game=discord.Game(name=';help'))

@client.command(
  name="roll",
  decription="rolls any number of dice",
  brief="Calls to the void to return the sacred numbers",
)
async def roll(die, advantage=None): # =None, advantage=None
  if die is not None:
    #mischien moet dit nog worden veranderd afhankelijk van de formating van de input
    if advantage is None:
      await client.say("you rolled a " + str(random.randint(1, int(die))))
    elif "dis" in advantage:
      await client.say("you rolled a " + str(min(random.randint(1, int(die)), random.randint(1, int(die)))))
    else:
      await client.say("you rolled a " + str(max(random.randint(1, int(die)), random.randint(1, int(die)))))

@client.command(brief="Generates a random encounter")
async def encounter():
  enemy = random.choice(["ruben", "nathan", "marnix", "Daan the almighty"])
  place = random.choice([ "woods", "desert", "planes"])
  weather = random.choice(["stormy", "clear", "misty"])
  await client.say("the enemy is " + enemy + ", you are in the " + place + ", and the weather is " + weather)

@client.command(brief="Get a reference to any spell that is listed in D&D" )
async def spell(*name):
  name = " ".join(name)
  name = name.lower().replace(' ', '-').replace("'", "")
  await client.say(f"https://www.dndbeyond.com/spells/{name}")
  
@client.command(brief="Get a reference to any race that is listed in D&D" )
async def race(*name):
  name = " ".join(name)
  name = name.lower().replace(' ', '-').replace("'", "")
  await client.say(f"https://www.dndbeyond.com/characters/races/{name}") 

@client.command(brief="Get a reference to any class that is listed in D&D" )
async def classes(*name):
  name = " ".join(name)
  name = name.lower().replace(' ', '-').replace("'", "")
  await client.say(f"https://www.dndbeyond.com/characters/classes/{name}")

@client.command(brief="Get a reference to any background that is listed in D&D" )
async def background(*name):
  name = " ".join(name)
  name = name.lower().replace(' ', '-').replace("'", "")
  await client.say(f"https://www.dndbeyond.com/characters/backgrounds/{name}")

@client.command(brief="About us")
async def about():
  await client.say("Fan made D&D discord bot!, started working on 18-11-2018")

@client.command(brief="Roll a certain stat for example: dexterity")
async def stat(modifier=None):
    if modifier is None:
        rolls = []
        for i in range(4):
            rolls.append(randrange(1,6))
        rolls.sort()
        variabel = sum(rolls[-3:])
        await client.say(variabel)
    else:
        rolls = []
        for i in range(4):
            rolls.append(randrange(1,6))
        rolls.sort()
        variabel = sum(rolls[-3:]) + modifier
        await client.say(variabel)


async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)

token = os.environ.get("DISCORD_BOT_SECRET")
client.loop.create_task(list_servers())
client.run(token)
