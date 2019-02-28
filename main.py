import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext import commands
from discord.ext.commands import Bot 
from dumpfiles.welcomemessage import *
from dumpfiles.specialcommand import *

startup_extensions = ['cogs.taverncogs.thelp', 
		      'cogs.taverncogs.faqcommand',
		      'cogs.corecogs.normalhelp',
		      'cogs.corecogs.encountergen',
		      'cogs.taverncogs.rprule',
		      'cogs.corecogs.charactergen',
		      'cogs.corecogs.spellcommand',
		      'cogs.corecogs.classcommand',
		      'cogs.taverncogs.rules',
		      'cogs.corecogs.conditions',
		      'cogs.corecogs.npcgen',
		      'cogs.corecogs.currency',
		      'cogs.corecogs.status',
		      'cogs.corecogs.statroller']

BOT_PREFIX = (";", "/t", "!t")
bot = commands.Bot(command_prefix=BOT_PREFIX)
bot.remove_command("help")

@bot.event
async def on_ready():
    print("I'm in")
    print(bot.user)
    print(discord.__version__)	
    await bot.change_presence(game=discord.Game(name=';help | d&d 5e'))

@bot.event
async def on_member_join(member):
    if member.server.id != "362589385117401088":
        return
    strings = ["Welcome to the Tavern! Please leave your bears at the Bear Post.",
		"Be advised: otters are considered contraband, unless they are members of Staff.",
		"In the event of a catastrophic temporal or dimensional paradox, please avoid making eye contact with your past, future, or alternate selves.",
		"May the Gods have mercy on your soul.",
		"Have a drink. Or don't. That one might be poisoned.",
		"Remember: don't talk about alignment unless you're prepared to argue about alignment.",
		"Selûne is best girl, but don't tell Shar I said so.",
		"The Lords here all worship Loviatar, so make sure to behave unless you like being punished.",
		"Stasis pod malfunction. Prepare to discontinue hypersleep. You have been in stasis for...nine...million...nine...hundred...thousand...",
		"Necromancers be advised: keep the skeletons in your closet.  Nobody wants to see that.",
		"Keep your wands holstered, your weapons sheathed, and your staves slung.",
		"See that gnome in the corner? No? Well, he sees you, so be nice.",
		"We welcome patrons of all races and walks of life...so it's frowned upon to ask the Tabaxi if they are a furry.",
		"We have a gazebo out back for when the weather's nice. Only mildly damaged!",
		"Greeting procedure complete. Prepare for initiation.",
		"Now roll initiative!",
		"Bodies tend to go missing every once in a while, so try not to die."]
    stringspick = random.choice(strings)	
    content = "Welcome to The Tavern " + member.mention + ". " + stringspick
    channel = discord.utils.get(member.server.channels, name="general")
    await bot.send_message(channel, content)
	
def create_roller_function(name, roller, good_roll_text="a fabulous", **command_specifiers):
	@bot.command(name=name, **command_specifiers)
	async def _func(*dice):
		embed = discord.Embed(
			colour=discord.Colour.blue()
		)
		embed.set_author(name="Dice roller")
		if not dice:
			dice = ['1d20']
		if len(dice) == 1 and "d" not in dice[0]:
			dice = list(dice)
			dice[0] =  '1d'+dice[0]
		dice = [die.split("d") for die in dice]
		if len(dice) == 1 and dice[0][0] == '1':
			die_type = int(dice[0][1])
			die_5 = max(1, die_type//5)
			roll = roller(1, die_type)
			if roll > die_5*4 + randint(-die_5, die_5):
				embed.add_field(name=f"You rolled {dice[0][0]}d{die_type}", value=f"which became {good_roll_text} {roll}", inline=False)
			else:

				embed.add_field(name=f"You rolled {dice[0][0]}d{dice[0][1]}", value=f"which became {roll}", inline=False)
		else:
			sum_ = 0
			rolls = []
			s = 0
			for die in dice:
				rolls.append([])
				for _ in range(int(die[0])):
					roll = roller(1, int(die[1]))
					sum_ += roll
					rolls[-1].append(str(roll))
				if s:
					embed.add_field(name=f"you also rolled {die[0]}d{die[1]}", value="which became "+'+'.join(rolls[-1]), inline=False)
				else:
					embed.add_field(name=f"You rolled {dice[0][0]}d{dice[0][1]}", value="which became "+'+'.join(rolls[-1]), inline=False)
					s = 1
			embed.add_field(name="Result", value=str(sum_), inline=False)
		await bot.say(embed=embed)

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
	brief="Pick the best of 3 rolls, same format as ;roll",
)
create_roller_function(
	"super-disadvantage",
	lambda x, y: min(randint(x,y), randint(x,y), randint(x,y)), 
	good_roll_text="despite your super-disadvantage you still managed to roll a(n)",
	brief="Pick the worst of 3 rolls, same format as ;roll"
)	     							 
					 	
if __name__ == "__main__":
    for extension in startup_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extension {}\n{}'.format(extension, exc))					 
					 
async def list_servers():
    await bot.wait_until_ready()
    while not bot.is_closed:
        print("Current servers in which the bot is running:")
        for server in bot.servers:
            print(server.name)
        await asyncio.sleep(600)
			
token = os.environ.get("DISCORD_BOT_SECRET")
bot.loop.create_task(list_servers())
bot.run(token)
