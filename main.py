import discord
import os
import asyncio
import urllib.request
import urllib.error
from random import randint
from random import sample
from discord.ext.commands import Bot 
from random import randrange
from monsterscr import *
from npcgen import *
import random

BOT_PREFIX = (";", "/")
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")

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
		embed = discord.Embed(
			colour=discord.Colour.blue()
		)
		if dice:
			if len(dice) == 1 and "d" not in dice[0]:
				die_type = int(dice[0])
				die_5 = max(die_type//5, 1)
				roll  = roller(1, die_type)
				if roll > die_5*4 + randint(-die_5, die_5):
					embed.add_field(good_roll_text)
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

					await client.say(f"```You rolled a {roll}```")
				return
			embed.set_author(name="Dice roller")
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
			await client.say(embed=embed)
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
	brief="Pick the best of 3 rolls, same format as ;roll",
)
create_roller_function(
	"super-disadvantage",
	lambda x, y: min(randint(x,y), randint(x,y), randint(x,y)), 
	good_roll_text="despite your super-disadvantage you still managed to roll a(n)",
	brief="Pick the worst of 3 rolls, same format as ;roll"
)

@client.command(name="npc", brief="create a quick npc" )
async def npc():
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name="Randomly generated NPC:")
	embed.add_field(name="Race:", value=raceroll, inline=False)
	embed.add_field(name="Gender:", value=genderroll, inline=False)
	embed.add_field(name="Age:", value=age, inline=False)
	embed.add_field(name="Traits:", value=traitsroll, inline=False)
	embed.add_field(name="Background:", value=backgroundroll, inline=False)
	embed.add_field(name="Hair:", value=hairroll + ", " + haircolourroll, inline=False)
	embed.add_field(name="Size:", value=sizeroll, inline=False)
	embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)

	await client.say(embed=embed)

@client.command(name="invite", brief="Invite the bot to your discord server")
async def invite():
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.add_field(name="Invite the bot to your server:", value="https://discordapp.com/api/oauth2/authorize?client_id=506541896630403080&permissions=0&scope=bot", inline=False)
	await client.say(embed=embed)
	
# @client.command(brief="Generates a random encounter")
# async def encounter():
#     enemy = random.choice(["ruben", "nathan", "mighty marnix", "Daan the almighty"])
#     place = random.choice([ "woods", "desert", "planes"])
#     weather = random.choice(["stormy", "clear", "misty"])
#     await client.say("Under development!")



	
@client.command(brief="About us")
async def about():
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name="About d&d online:")
	embed.add_field(name="Date of creation:", value="18-11-2018", inline=False)
	embed.add_field(name="Creators:", value="D&D online has been developed by: RubenJ01#0229 and Daan#2049")
	embed.add_field(name="Source:", value="Since d&d online is open source you can check ouher repo: https://github.com/RubenJ01/dndonline", inline=False)
	await client.say(embed=embed)

@client.command()
async def initiative(*args):
    global initiative_roles
    for x in range(0,len(args),2):
        initiative_role = random.randint(1,20)
        if initiative_role != 1:
            initiative_role += int(args[x+1])
        output = args[x]
        output += " your initiative is "
        output += str(initiative_role)
        initiative_roles += [[args[x],int(initiative_role)]]
        await client.say(output)
        await client.say(initiative_roles)
    #initiative_roles["WILDCARD"][1].sort()
    #initiative_roles.reverse()
    for y in range(0,len(args),2):
        output = initiative_roles[0][0]
        output += " you roled "
        output += str(initiative_roles[1][1])
    await client.say(output)

@client.command()
async def next():
    global initiative_roles
    initiative_roles += [initiative_roles[0]]
    del initiative_roles[0]
    await client.say(initiative_roles)


@client.command()
async def stop():
    global initiative_roles
    initiative_roles = []
    await client.say("initiative clerd")
		
@client.command(brief="Roll a certain stat for example: dexterity")
async def stat(modifier=0):
	rolls = [randint(1,6) for _ in range(4)]
	await client.say(f"the total of the best 3 of your 4 rolls was {sum(rolls)-min(rolls)}")			     
	
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
    embed = discord.Embed(
    	colour = discord.Colour.blue()
    )
    embed.add_field(name="Currency", value="You have " + str(cp) + "cp "  + str(sp) + "sp " + str(gp) + "gp " + str(pp) + "pp ", inline=False)
    await client.say(embed=embed)

@client.command()
async def test(*test, init):
	rolls = []
	variabeles = []
	for j in range(6):	
		for i in range(4):
			rolls.append(randint(1, 6))
			rolls.sort() 	    
		variabeles.append(sum(rolls)-min(rolls))
		rolls =[]
	total = init + variabeles
	await client.say(test + total)

@client.command(brief="Random level 1 character creator")
async def character():
	alignment = ["Lawfull good", "Neutral good", "Chaotic good", "Lawful neutral", "Neutral", "Chaotic"]
	alignmentroll = random.choice(alignment)

	background = ["Acolyte", "Criminal", "Folk hero", "Noble", "Sage", "Soldier"]
	backgroundroll = random.choice(background)

	proficiency = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
	proficiencyroll = random.sample(proficiency, 4)

	classes = ["Cleric", "Fighter", "Rogue", "Wizard", "Ranger", "Druid", "Bard"]
	classesroll = random.choice(classes)

	race = ["Hill dwarf", "Mountain dwarf", "High elf", "Wood elf", "Lightfoot halfling", "Stout halfling"]
	raceroll = random.choice(race)


	rolls = []
	variabeles = []
	for j in range(6):    
		for i in range(4):
			rolls.append(randint(1, 6))
			rolls.sort()         
		variabeles.append(sum(rolls)-min(rolls))
		rolls =[]	
	if classesroll == "Cleric": 
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		cantrips = ["Guidance", "light", "Resistance", "Sacred flame", "Spare the dying", "Thaumaturgy"]
		cantripsroll = random.sample(cantrips, 3)
		spells = ["Bless", "Command", "Cure wounds", "Detect magic", "Guiding bolt", "Healing word", "Inflict wounds", "Sanctuary", "Schield of faith"]
		spellsroll = random.sample(spells, 2)
		embed = discord.Embed(
		colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="8 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		embed.add_field(name="Cantrips:", value=', '.join(cantripsroll), inline=False)
		embed.add_field(name="Spells:", value=', '.join(spellsroll), inline=False)
		await client.say(embed=embed)
	if classesroll == "Fighter": 
		fightingstyle = ["Archery (swap light crossbow and 20 bolts for a longbow and 20 arrows; at your option, also swap chain mail for leather armor)", "Defense", "Dueling", "Great Weapon Fighting (swap longsword and shield for a greataxe", "Protection", "Two-Weapon Fighting (swap longsword for two short swords)"]
		fightingstyleroll = random.choice(fightingstyle)
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="10 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		embed.add_field(name="Fightingstyle:", value=fightingstyleroll, inline=False)
		await client.say(embed=embed)
	if classesroll == "Rogue":
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="8 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		await client.say(embed=embed)
	if classesroll == "Wizard":
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		cantrips = ["Acid splash", "Dancing lights", "Fire bolt", "Light", "Mage hand", "Minor illusion", "Posion spray", "Prestidigation", "Ray of frost", "Shocking grasp"]
		cantripsroll = random.sample(cantrips, 3)
		spells = ["Burning hands", "Charm person", "Comprehend languages", "Detect magic", "Disguise self", "Identify", "Mage armor", "Magic missile", "Shield", "Silent image", "Sleep", "Thunderwave",]
		spellsroll = random.sample(spells, 6)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="6 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		embed.add_field(name="Cantrips:", value=', '.join(cantripsroll), inline=False)
		embed.add_field(name="Spells:", value=', '.join(spellsroll), inline=False)
		await client.say(embed=embed)
	if classesroll == "Ranger":
		equipment1 = ["Scale Mail", "Leather Armor"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Two shortswords", "Two simple melee weapons"]
		equipment2roll = random.choice(equipment2)
		equipment3 = ["a Dungeoneer's Pack", "An Explorer's Pack, A Longbow and a Quiver of 20 Arrows"]
		equipment3roll = random.choice(equipment3)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="6 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll + ", " + equipment3roll, inline=False)
		await client.say(embed=embed)
	if classesroll == "Druid":
		equipment1 = ["A wooden schield", "Any simple weapon"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["A Scimitar", "any simple melee weapon, Leather Armor, an Explorer's Pack, and a druidic focus"]
		equipment2roll = random.choice(equipment2)
		spells = ["Absorb Elements", "Animal Friendship", "Beast bond", "Charm Person", "Create or Destroy water", "Cure wounds", "Detect Magic"]
		spellsroll = random.sample(spells, 2)
		cantripsroll = random.sample(cantrips, 2)
		cantrips = ["Control Flames", "Create Bonfire", "Druidcraft", "Frostbite", "Guidance", "Gust", "Infestation", "Magic Stone", "Mending", "Mold Earth"]
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="8 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		embed.add_field(name="Cantrips:", value=', '.join(cantripsroll), inline=False)
		embed.add_field(name="Spells:", value=', '.join(spellsroll), inline=False)
		await client.say(embed=embed)
	if classesroll == "Bard":
		equipment1 = ["A Rapier", "A longsword", "Any simple weapon"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["A diplomat's pack", "An entertainer's pack"]
		equipment2roll = random.choice(equipment2)
		equipment3 = ["A lute", "any other musical instrument Leather Armor, and a Dagger"]
		equipment3roll = random.choice(equipment3)
		cantrips = ["Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigation", "Thunderclap", "True Strike", "Vicious Mockery"]
		cantripsroll = random.sample(cantrips, 2)
		spells = ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic", "Disguise Self", "Dissonant Whispers", "Earth Tremor", "Fearie Fire", "Feather Fall", "Healing Word", "Heroism", "Identify", "Illusory Script", "Longstrider", "Silent Image", "Sleep", "Speak with Animals", "Tasha's Hideous Laughter", "Thunderwave", "Unseen servant"]
		spellsroll = random.sample(spells, 2)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="8 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll + ", " + equipment3roll, inline=False)
		embed.add_field(name="Cantrips:", value=', '.join(cantripsroll), inline=False)
		embed.add_field(name="Spells:", value=', '.join(spellsroll), inline=False)
		await client.say(embed=embed)

@client.command()
async def rngstat():
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
		embed.add_field(name="Roll", value=str(roll1) + ", " + str(roll2) + ", " + str(roll3) + ", " + str(roll4) + " = " + str(ability), inline=False)
	await client.say(embed=embed)

@client.command()
async def rngstat3():
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
		embed.add_field(name="Roll", value=str(roll1) + ", " + str(roll2) + ", " + str(roll3) + ", " + str(roll4) + " = " + str(ability), inline=False)
	await client.say(embed=embed)

			

@client.command(brief="The definitions of combat conditions")
async def condition(type):
	if type == "blinded":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition blinded:", value="A blinded creature can’t see and automatically fails any ability check that requires sight." + "\n" + "Attack rolls against the creature have advantage, and the creature’s Attack rolls have disadvantage.", inline=False)
		await client.say(embed=embed)
	if type == "charmed":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition charmed:", value="A charmed creature can’t Attack the charmer or target the charmer with harmful Abilities or magical effects." + "\n" + "The charmer has advantage on any ability check to interact socially with the creature.", inline=False)
		await client.say(embed=embed)
	if type == "frightened":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition frightened:", value="A frightened creature has disadvantage on Ability Checks and Attack rolls while the source of its fear is within line of sight." + "\n" + "The creature can’t willingly move closer to the source of its fear.", inline=False)
		await client.say(embed=embed)
	if type == "deafened":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition deafened:", value="A deafened creature can’t hear and automatically fails any ability check that requires hearing.", inline=False)
		await client.say(embed=embed)	
	if type == "grappled":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition grappled:", value="A grappled creature’s speed becomes 0, and it can’t benefit from any bonus to its speed." + "\n" + "The condition ends if the Grappler is incapacitated (see the condition)." + "\n" + "The condition also ends if an effect removes the grappled creature from the reach of the Grappler or Grappling effect, such as when a creature is hurled away by the Thunderwave spell.", inline=False)
		await client.say(embed=embed)
	if type == "incapacitated":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition incapacitated:", value="An incapacitated creature can’t take actions or reactions.", inline=False)
		await client.say(embed=embed)
	if type == "invisible":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition invisible:", value="An invisible creature is impossible to see without the aid of magic or a Special sense. For the purpose of Hiding, the creature is heavily obscured. The creature’s location can be detected by any noise it makes or any tracks it leaves." + "\n" + "Attack rolls against the creature have disadvantage, and the creature’s Attack rolls have advantage.", inline=False)
		await client.say(embed=embed)
	if type == "paralyzed": 
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition paralyzed:", value="A paralyzed creature is incapacitated (see the condition) and can’t move or speak." + "\n" + "The creature automatically fails Strength and Dexterity Saving Throws." + "\n" + "Attack rolls against the creature have advantage." + "\n" + "Any Attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.", inline=False)
		await client.say(embed=embed)
		
@client.command(pass_context=True)
async def help(ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	
	embed.set_author(name="Help menu")
	embed.add_field(name=";help", value="Shows this message", inline=False)
	embed.add_field(name=";roll", value="roll dice with no advantage or disadvantage when given no parameters 1d20 is rolled parameters can be formatted like so 5d3 4d2 1d21 or simply 10 the latter only works for single dice all dice will be rolled and the total will be returned", inline=False)
	embed.add_field(name=";advantage", value="roll with advantage (format like 4d6 2d8 default is 1d20)", inline=False)
	embed.add_field(name=";disadvantage", value="roll with disadvantage (format like 4d6 2d8 default is 1d20)", inline=False)
	embed.add_field(name=";super-advantage", value="Pick the best of 3 rolls, same format as ;roll", inline=False)
	embed.add_field(name=";super-disadvantage", value="Pick the worst of 3 rolls, same format as ;roll", inline=False)
	embed.add_field(name=";rngstat", value="Roll 1 ability score (best 3 rolls of a 4d6)", inline=False)
	embed.add_field(name=";rngstat3", value="Roll 1 ability score 3 times so players can use 1 for their definitive roll (best 3 rolls of a 4d6)", inline=False)
	embed.add_field(name=";rngstat", value="Roll all 6 of your ability scores (best of 3 rolls of a 4d6 6 times)", inline=False)
	embed.add_field(name=";currency", value="Calculate your total amount of pp gp sp cp respectively (format like ;currency 1gp 1pp 20sp etc)", inline=False)
	embed.add_field(name=";initiative", value="Insert a name + modifier respectively and roll initiative multple names can be given", inline=False)
	embed.add_field(name=";character", value="Generate a quick level 1 character", inline=False)
	embed.add_field(name=";npc", value="Generate a quick npc, including traits and appearence.", inline=False)
	embed.add_field(name=";encounter", value="Make an encounter for your party (format like ;encounter party level party size so for example ;encounter 15 6 this will generate an encounter for a party of level 15 with 6 members, keep in mind that the minimum party size is 2 and the maximum is 8).", inline=False)
	embed.add_field(name=";invite", value="Get an invite link for the discord bot to join your server!", inline=False)
	embed.add_field(name=";about", value="Learn more about the bot", inline=False)
	embed.add_field(name="Official server", value="Please condsider joining ouher official server: https://discord.gg/sYPVXv8", inline=False)
	await client.send_message(author, embed=embed)
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.add_field(name="Help", value="Sended you a private message which contains the information", inline=False)
	await client.say(embed=embed)
	
@client.command(brief="An encounter generator for d&d 5e")
async def encounter(level, size):
	if level == "1": 	
		if size == "2":
			enc = random.sample(crkwart, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.sample(crkwart, 3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.sample(crkwart, 4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.sample(crkwart, 4)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=enc2, inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.sample(crkwart, 1)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.sample(crkwart, 2)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.sample(crkwart, 3)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "2":
		if size == "2":
			enc = random.sample(crhalf, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.sample(crhalf, 3)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.sample(crhalf, 1)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.sample(crhalf, 2)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == 6:
			enc = random.sample(crhalf, 6)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=enc2, inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.sample(crhalf, 1)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.sample(crhalf, 2)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "3":
		if size == "2":
			enc = random.sample(crhalf, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.sample(crhalf, 2)
			enc2 = random.sample(crkwart, 1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.sample(cr2, 1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.sample(cr2, 1)
			enc2 = random.sample(crhalf, 1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr3)
			enc2 = random.choice(crhalf)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr3)
			enc2 = random.sample(crhalf, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
			await client.say(embed=embed)
	if level == "4":
		if size == "2":
			enc = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr2)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc =  random.choice(cr3)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr4)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr4)
			enc2 = random.sample(cr1, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
			await client.say(embed=embed)
	if level == "5": 
		if size == "2":
			enc = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr4)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr6)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr6)
			enc2 = random.sample(cr2, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
			await client.say(embed=embed)
	if level == "6":
		if size == "2":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr4)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr7)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr7)
			enc2 = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "7":
		if size == "2":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr7)
			enc2 = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr7)
			enc2 = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr7)
			enc2 = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "8":
		if size == "2":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr7)
			enc2 = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr8)
			enc2 = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr8)
			enc2 = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "9":
		if size == "2":
			enc = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr4)
			enc2 = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr9)
			enc2 = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "10":
		if size == "2":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr10)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr4)
			enc2 = random.choice(cr10)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr10)
			enc2 = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "11":
		if size == "2":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr10)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr5)
			enc2 = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr11)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "12":
		if size == "2":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr10)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr12)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "12":
		if size == "2":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr12)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "13":
		if size == "2":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr13)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "14":
		if size == "2":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr14)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "15":
		if size == "2":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr15)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr15)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr15)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "16":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr15)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr16)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "17":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr17)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr17)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr17)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "18":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr18)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr18)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr18)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "19":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr17)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr19)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr19)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr19)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "20":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr15)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr19)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr20)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr20)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr20)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
													
														
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers in which the bot is running:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
			
token = os.environ.get("DISCORD_BOT_SECRET")
client.loop.create_task(list_servers())
client.run(token)
