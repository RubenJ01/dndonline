import discord
import os
import random
import asyncio
import aiohttp
import json
import collections

from random import randint

from discord import Game
from discord.ext.commands import Bot 
from random import randrange
    

BOT_PREFIX = (";", "/")
client = Bot(command_prefix=BOT_PREFIX)

def randadv(bottom, top):
    """
    this is the randint function but now as if rolled with advantage
    """
    return max(randint(bottom, top), randint(bottom, top))

def randdisadv(bottom, top):
    """
    this is the randint function but now as if rolled with disadvantage
    """
    return min(randint(bottom, top), randint(bottom, top))

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(game=discord.Game(name=';help'))


@client.command(
    name="advantage",
    brief='roll with advantage (format like "4d6 2d8" default is "1d20")',
    description="""roll dice with disadvantage
    when given no parameters 1d20 is rolled
    parameters can be formatted like so "5d3 4d2 1d21" or "10" the latter only works with single dice
    when rolled every single roll gets an advantage and the total is returned"""
                
)
async def adv(*dice)
    if dice:
        if len(dice) == 0 and "d" not in dice[0]:
            await client.say(f"you rolled a {randint(1, int(dice[0]))}")
            return
        sum_ = 0
        dice = [die.split("d") for die in dice]
        for die in dice:
            for _ in range(int(die[0])):
                sum_ += randadv(1, int(die[1]))
        await client.say(f"you rolled a total of {sum_}")
    else:
        await client.say(f"you rolled a {randadv(1, int(die))}")
    
@client.command(
    name="disadvantage",
    brief='roll with disadvantage (format like "4d6 2d8" default is "1d20")',
    description="""roll dice with disadvantage
    when given no parameters 1d20 is rolled
    parameters can be formatted like so "5d3 4d2 1d21" or simply "10" the latter only works with single dice
    when rolled every single roll gets an disadvantage and the total is returned"""
)        
async def disadv(*dice):
    if dice:
        if len(dice) == 0 and "d" not in dice[0]:
            await client.say(f"you rolled a {randdisadv(1, int(dice[0]))}")
            return
        sum_ = 0
        dice = [die.split("d") for die in dice]
        for die in dice:
            for _ in range(int(die[0])):
                sum_ += randdisadv(1, int(die[1]))
        await client.say(f"you rolled a total of {sum_}")
    else:
        await client.say(f"you rolled a {randdisadv(1, 20)}")
               
@client.command(
    name="roll",
    decription='roll without advantage or disadvantage (format like "4d6 2d8" default is "1d20")',
    brief="Calls to the void to return the sacred numbers",
    description="""roll dice with no advantage or disadvantage
    when given no parameters 1d20 is rolled
    parameters can be formatted like so "5d3 4d2 1d21" or simply "10" the latter only works for single dice
    all dice will be rolled and the total will be returned"""
)
async def roll(*dice):
    if dice:
        if len(dice) == 0 and "d" not in dice[0]:
            await client.say(f"you rolled a {randint(1, int(dice[0]))}")
            return
        sum_ = 0
        dice = [die.split("d") for die in dice]
        for die in dice:
            for _ in range(int(die[0])):
                sum_ += randint(1, int(die[1]))
        await client.say(f"you rolled a total of {sum_}")
    else:
        await client.say(f"you rolled a {randint(1, 20)})

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
        await client.say("After rolling 4 times your roll became a: " + str(variabel))
    else:
        rolls = []
        for i in range(4):
            rolls.append(randrange(1,6))
        rolls.sort()
        variabel = sum(rolls[-3:]) + int(modifier)
        await client.say("After rolling 4 times your roll became a: " + str(variabel))
                    
        
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
