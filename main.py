import discord
import os
import asyncio

from random import randint

from discord.ext.commands import Bot 
from random import randrange
    
BOT_PREFIX = (";", "/")
client = Bot(command_prefix=BOT_PREFIX)

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(game=discord.Game(name=';help'))


def create_call_to_dnd_beyond(name, link, **kwargs):
	@client.command(name=name, **kwargs)
	async def _func(*name):
		name = " ".join(name)
		name = name.lower().replace(' ', '-').replace("'", "")
		await client.say(f"https://www.dndbeyond.com/{link}/{name}") 
	
def create_roller_function(name, roller, good_roll_text="you managed to roll a fabulous", **command_specifiers):
	@client.command(name=name, **command_specifiers)
	async def _func(*dice):
		if dice:
			if len(dice) == 1 and "d" not in dice[0]:
				die_type = int(dice[0])
				die_5 = max(die_type//5, 1)
				roll  = roller(1, die_type)
				if roll > die_5*4 + randint(-die_5, die_5):
					await client.say(f"```{good_roll_text} {roll}```")
				else:
					if roll not in [8,11,18]:
						await client.say(f"```You rolled a {roll}```")
					else:
						await client.say(f"```You rolled an {roll}```")
				return
				dice = [die.split("d") for die in dice]
				if len(dice) == 1 and dice[0][0] == '1':
					await client.say(f"```You rolled a {roller(1, int(dice[0][1]))}```")
			dice = [die.split("d") for die in dice]
			if len(dice) == 1 and dice[0][0] == '1':
				die_type = int(dice[0][1])
				die_5 = max(1, die_type//5)
				roll = roller(1, die_type)
				if roll > die_5*4 + randint(-die_5, die_5):
					await client.say(f"```{good_roll_text} {roll}```")
				else:
					
					await client.say(f"```You rolled a {roll}")
				return
			sum_ = 0
			rolls = []
			text = [f"```You rolled {dice[0][0]}d{dice[0][1]} "]
			s = 0
			for die in dice:
				if s:
					text.append(f", you also rolled {die[0]}d{die[1]} ")
				else:
					s = 1
				rolls.append([])
				for _ in range(int(die[0])):
					roll = roller(1, int(die[1]))
					sum_ += roll
					rolls[-1].append(str(roll))
				text.append("which became "+'+'.join(rolls[-1]))
			text.append(f"\nfor a total of {sum_}```")
			await client.say(''.join(text))
		else:
			roll = roller(1, 20)
			if roll > 16 + randint(-4, 4):
				await client.say(f"```{good_roll_text} {roll}```")
			else:
				await client.say(f"```You rolled a {roll}```")
		
create_call_to_dnd_beyond("spell" ,"spells", brief="Get a reference to any spell that is listed in D&D")
create_call_to_dnd_beyond("race", "characters/races", brief="Get a reference to any race that is listed in D&D")
create_call_to_dnd_beyond("classes", "characters/classes", brief="Get a reference to any class that is listed in D&D")
create_call_to_dnd_beyond("background", "characters/backgrounds", brief="Get a reference to any background that is listed in D&D")

create_roller_function(
	"roll",
	randint,
	brief='roll normally (format like "4d6 2d8" default is "1d20")',
    description="""roll dice with no advantage or disadvantage
	when given no parameters 1d20 is rolled
	parameters can be formatted like so "5d3 4d2 1d21" or simply "10" the latter only works for single dice
	all dice will be rolled and the total will be returned"""
)
create_roller_function(
	"advantage", 
	lambda x, y: max(randint(x,y), randint(x,y)), 
	good_roll_text="thanks to your advantage you managed to roll a(n)",
	brief='roll with advantage (format like "4d6 2d8" default is "1d20")',
    description="""roll dice with disadvantage
	when given no parameters 1d20 is rolled
	parameters can be formatted like so "5d3 4d2 1d21" or "10" the latter only works with single dice
	when rolled every single roll gets an advantage and the total is returned"""
)
create_roller_function(
	"disadvantage",
	lambda x, y: min(randint(x,y), randint(x,y)),
	good_roll_text="despite your disadvantage you managed to roll a(n)",
	brief='roll with disadvantage (format like "4d6 2d8" default is "1d20")',
	description="""roll dice with disadvantage
	when given no parameters 1d20 is rolled
	parameters can be formatted like so "5d3 4d2 1d21" or simply "10" the latter only works with single dice
	when rolled every single roll gets an disadvantage and the total is returned"""
)
create_roller_function(
	"super-advantage",
	lambda x, y: max(randint(x,y), randint(x,y), randint(x,y)), 
	good_roll_text="with super advantage you were probably expecting something high and you were right because you rolled a(n)",
	brief="pick the best of 3 rolls",
)
create_roller_function(
	"super-disadvantage",
	lambda x, y: min(randint(x,y), randint(x,y), randint(x,y)), 
	good_roll_text="despite your super-disadvantage you still managed to roll a(n)",
	brief="pick the worst of 3 rolls"
)




# @client.command(
#     name="npc",
#     brief="create a quick npc"
# )
# async def npc(race=None):
#     if race is None or race.lower() == "none":
#         # generate random race
#         pass
#     stats = [sum([randint(2, 6) for _ in range(3)]) for _ in range(6)]
#     await client.say("Currently not finished :(")
    
# @client.command(brief="Generates a random encounter")
# async def encounter():
#     enemy = random.choice(["ruben", "nathan", "mighty marnix", "Daan the almighty"])
#     place = random.choice([ "woods", "desert", "planes"])
#     weather = random.choice(["stormy", "clear", "misty"])
#     await client.say("Under development!")



	
@client.command(brief="About us")
async def about():
    await client.say("Fan made D&D discord bot!, started working on 18-11-2018")

@client.command(brief="Roll a certain stat for example: dexterity")
async def stat(modifier=0):
	rolls = [randint(1,6) for _ in range(4)]
	await client.say(f"the total of the best 3 of your 4 rolls was {sum(rolls)-min(rolls)}")
      
@client.command(brief="Roll all your stats")
async def stats():
	rolls = []
	variabeles = []
	for j in range(6):	
		for i in range(4):
			rolls.append(randint(1, 6))
			rolls.sort() 	    
		variabeles.append(sum(rolls)-min(rolls))
		rolls =[]	
	await client.say("```Your rolls are: \n" + str(variabeles) + "```")
	
@client.command(brief="Calculate your total amount of pp gp sp cp respectively")
async def currency(*coins):
    cp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "cp"])
    sp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "sp"])
    ep = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "ep"])
    gp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "gp"])
    pp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "pp"])
    total = (cp * 1) + (sp * 10) + (ep * 50) + (gp * 100) + (pp * 1000)
    cp = total%10
    total = total//10
    sp = total%10
    total = total//10
    gp = total%10
    total = total//10
    pp = total
    await client.say("```You have " + str(cp) + "cp "  + str(sp) + "sp " + str(gp) + "gp " + str(pp) + "pp " + "```")
	
@client.command()
async def initiative(*names):
    for i in range(0, len(names), 2):
        init = (f"{names[i]} rolled {randint(1,20)+eval(names[i+1])}")
		await client.say("```" + str(init) + "```") 
		
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

