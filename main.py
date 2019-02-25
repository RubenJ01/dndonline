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
from dumpfiles.npcgen import *
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
		      'cogs.corecogs.conditions']

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

@bot.command(name="npc", brief="generate an npc that includes appearance, stats and traits" )
async def npc():
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name="Randomly generated NPC:")
	embed.add_field(name="Race:", value=raceroll, inline=False)
	embed.add_field(name="Gender:", value=genderroll, inline=False)
	embed.add_field(name="Age:", value=age, inline=False)
	embed.add_field(name="Traits:", value=traitsroll, inline=False)
	embed.add_field(name="Flaws & Secrets:", value=flawsroll, inline=False)
	embed.add_field(name="Mannerism:", value=mannerismroll, inline=False)
	embed.add_field(name="Ideal:", value=idealsroll, inline=False)
	embed.add_field(name="Talent:", value=talentsroll, inline=False)
	embed.add_field(name="Background:", value=backgroundroll, inline=False)
	embed.add_field(name="Hair:", value=hairroll + ", " + haircolourroll, inline=False)
	embed.add_field(name="Size:", value=sizeroll, inline=False)
	embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)

	await bot.say(embed=embed)

@bot.command(name="invite", brief="invite the bot to your discord server")
async def invite():
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.add_field(name="Invite the bot to your server:", value="https://discordapp.com/oauth2/authorize?client_id=506541896630403080&scope=bot&permissions=0", inline=False)
	await bot.say(embed=embed)

	
@bot.command(brief="information about the Tavern Bot")
async def about():
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name="About The Tavern Bot:")
	embed.add_field(name="Date of creation:", value="18-11-2018", inline=False)
	embed.add_field(name="Creators:", value="The Tavern Bot has been developed by: RubenJ01#0229 and Daan#2049")
	embed.add_field(name="Contributors:", value="Thanks to: willdda117#2904 for contributing to The Tavern Bot")
	embed.add_field(name="Source:", value="Since The Tavern Bot is open source you can check ouher repo: https://github.com/RubenJ01/dndonline", inline=False)
	await bot.say(embed=embed)
		
@bot.command(brief="roll a certain stat for example: dexterity")
async def stat(modifier=0):
	rolls = [randint(1,6) for _ in range(4)]
	await bot.say(f"the total of the best 3 of your 4 rolls was {sum(rolls)-min(rolls)}")			     
	
@bot.command(brief="calculate your total amount of pp gp sp cp respectively")
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
    embed = discord.Embed(
    	colour = discord.Colour.blue()
    )
    embed.add_field(name="Currency", value="You have " + str(cp) + "cp "  + str(sp) + "sp " + str(gp) + "gp " + str(pp) + "pp ", inline=False)
    await bot.say(embed=embed)

@bot.command(brief="displays the amount of servers the bot is currently running in")
async def status():
	servers = len(bot.servers)
	members = len(list(bot.get_all_members()))
	embed = discord.Embed(
 		colour = discord.Colour.blue()
 	)
	embed.add_field(name="Bot status", value="Currently running in: " + str(servers) + " servers with: " + str(members) + " members.", inline=False)
	await bot.say(embed=embed)

@bot.command(brief="roll 6 random ability scores")
async def rngstat():
	number = 0				 
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name=" Randomly generated ability scores")
	for j in range(6):
		roll1 = int(random.randint(1, 6))
		roll2 = int(random.randint(1, 6))
		roll3 = int(random.randint(1, 6))
		roll4 = int(random.randint(1, 6))
		lowest = min(roll1, roll2, roll3, roll4)
		allrolls = [roll1, roll2, roll3, roll4]
		ability = sum(allrolls) - lowest
		number = number + 1			 
		embed.add_field(name="Roll " + str(number), value=str(roll1) + ", " + str(roll2) + ", " + str(roll3) + ", " + str(roll4) + " = " + str(ability), inline=False)
	await bot.say(embed=embed)

@bot.command(brief="roll 3 random ability scores")
async def rngstat3():
	number = 0				 
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name="3 randomly generated ability scores")
	for j in range(3):
		roll1 = int(random.randint(1, 6))
		roll2 = int(random.randint(1, 6))
		roll3 = int(random.randint(1, 6))
		roll4 = int(random.randint(1, 6))
		lowest = min(roll1, roll2, roll3, roll4)
		allrolls = [roll1, roll2, roll3, roll4]
		ability = sum(allrolls) - lowest
		number = number + 1
		embed.add_field(name="Roll " + str(number), value=str(roll1) + ", " + str(roll2) + ", " + str(roll3) + ", " + str(roll4) + " = " + str(ability), inline=False)
	await bot.bot(embed=embed)
			

@bot.command(brief="link to the basic rules for d&d")
async def basic():
	await bot.say("http://media.wizards.com/2018/dnd/downloads/DnD_BasicRules_2018.pdf")					 
					 
	
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
