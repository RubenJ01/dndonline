import discord
import os
import asyncio
import urllib.request
import urllib.error
from random import randint
from random import sample
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

# @client.command()
# async def spell(*spell):
# 	url = f"https://dnd5e.fandom.com/wiki/{' '.join(spell).title().replace(' ', '%20')}"
# 	try:
# 		response = urllib.request.urlopen(url)
# 	except urllib.error.HTTPError as e:
#   		await client.say("Unexcpected HTTPError please contact my creators")
#   		print(e.code)
# 	except urllib.error.URLError as e:
#   		await client.say("that is not a valid spell name")
# 	else:
# 		try:
# 			"""
# 			part of the code is accesed
# 			the request was fulfilled without errors
# 			"""
# 			html = response.read()
# 			index = html.index(b"<div id=\"WikiaArticle\" class=\"WikiaArticle\">")
# 			spell_type = html[
# 				html.index(b"caption", index)+11:
# 				html.index(b"</i>", index)].decode("UTF-8")
# 			casting_time_index = html.index(b"Casting Time", index)
# 			casting_time = html[
# 				casting_time_index+22
# 				:html.index(b"</td>", casting_time_index)-1].decode("UTF-8")
# 			del casting_time_index
# 			range_index = html.index(b"Range", index)
# 			range_ = html[
# 				range_index+15
# 				:html.index(b"</td>", range_index)-1].decode("UTF-8")
# 			del range_index
# 			components_index = html.index(b"Components", index)
# 			components = html[
# 				components_index+20
# 				:html.index(b"</td>", components_index)-1].decode("UTF-8")
# 			del components_index
# 			duration_index = html.index(b"Duration", index)
# 			duration = html[
# 				duration_index+18
# 				:html.index(b"</td>", duration_index)-1].decode("UTF-8")
# 			del duration_index
# 			description_index = html.index(b"<p>", index)
# 			description = html[description_index+3:html.index(b"</p", description_index)].decode("UTF-8")
# 			del description_index
# 			description.replace("</a>", "")
# 			while "<a" in description and ">" in description:
# 				description = f"{description[:description.index('<a')]} {description[description.index('>')+1:]}"
# 			description = description.replace("</a>", "")
# 			await client.say(f"""{spell_type}
# <-------------------->
# Casting Time: {casting_time}
# <-------------------->
# Range: {range_}
# <-------------------->
# Components: {components}
# <-------------------->
# Duration: {duration}
# <-------------------->
# {description}
# """)
# 		except Exception as e:
# 			await client.say("""don't mind me, I'm just your friendly neigborhood  doctor trying to find out what's wrong with this bot""")
# 			await client.say(e)


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
	
@client.command(brief="Insert a name + modifier respectively and roll initiative multple names can be given")
async def initiative(*names):
	for i in range(0, len(names), 2):
		init = f"{names[i]} rolled {randint(1,20)+eval(names[i+1])}"
		await client.say("```" + str(init) + "```")

@client.command(brief="Random level 1 character creator")
async def character():

	alignment = ["Lawfull good", "Neutral good", "Chaotic good", "Lawfull neutral", "Neutral", "Chaotic"]
	alignmentroll = random.choice(alignment)

	background = ["Acolyte", "Criminal", "Folk hero", "Noble", "Sage", "Soldier"]
	backgroundroll = random.choice(background)

	proficiency = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
	proficiencyroll = random.sample(proficiency, 4)

	classes = ["Cleric", "Fighter", "Rogue", "Wizard"]
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
		await client.say(
		"Hit points: 8 + your Constitution modifier" + 
		"\n" + "Alignment: " + alignmentroll + 
		"\n" + "Background: " + backgroundroll +
		"\n" + "Race: " + raceroll + 
		"\n" + "Proficiency's: " + str(proficiencyroll) + 
		"\n" + "Class: " + classesroll + 
		"\n" + "Ability scores: " + str(variabeles) + 
		"\n" + "Equipment packs: " + equipment1roll + ", " + equipment2roll +
		"\n" + "Cantrips: " + str(cantripsroll) +
		"\n" + "Spells: " + str(spellsroll)
		)
	if classesroll == "Fighter":    
		fightingstyle = ["Archery (swap light crossbow and 20 bolts for a longbow and 20 arrows; at your option, also swap chain mail for leather armor)", "Defense", "Dueling", "Great Weapon Fighting (swap longsword and shield for a greataxe", "Protection", "Two-Weapon Fighting (swap longsword for two short swords)"]
		fightingstyleroll = random.choice(fightingstyle)
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		await client.say(
		"Hit points: 10 + your Constitution modifier" +     
		"\n" + "Alignment: " + alignmentroll + 
		"\n" + "Background: " + backgroundroll +
		"\n" + "Race: " + raceroll + 
		"\n" + "Proficiency's: " + str(proficiencyroll) + 
		"\n" + "Class: " + classesroll + 
		"\n" + "Ability scores: " + str(variabeles) +
		"\n" + "Equipment packs: " + equipment1roll + ", " + equipment2roll +	
		"\n" + "Fighting style: " + fightingstyleroll
		)
	if classesroll == "Rogue":
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		await client.say(
		"Hit points: 8 + your Constitution modifier" +     
		"\n" + "Alignment: " + alignmentroll + 
		"\n" + "Background: " + backgroundroll +
		"\n" + "Race: " + raceroll + 
		"\n" + "Proficiency's: " + str(proficiencyroll) + 
		"\n" + "Class: " + classesroll + 
		"\n" + "Ability scores: " + str(variabeles)
		"\n" + "Equipment packs: " + equipment1roll + ", " + equipment2roll 	
		)
	if classesroll == "Wizard":
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		cantrips = ["Acid splash", "Dancing lights", "Fire bolt", "Light", "Mage hand", "Minor illusion", "Posion spray", "Prestidigation", "Ray of frost", "Shocking grasp"]
		cantripsroll = random.sample(cantrips, 3)
		spells = ["Burning hands", "Charm person", "Comprehend languages", "Detect magic", "Disguise self", "Identify", "Mage armor", "Magic missile", "Shield", "Silent image", "Sleep", "Thunderwave",]
		spellsroll = random.sample(spells, 6)
		await client.say(
		"Hit points: 6 + your Constitution modifier" + 
		"\n" + "Alignment: " + alignmentroll + 
		"\n" + "Background: " + backgroundroll +
		"\n" + "Race: " + raceroll + 
		"\n" + "Proficiency's: " + str(proficiencyroll) + 
		"\n" + "Class: " + classesroll + 
		"\n" + "Ability scores: " + str(variabeles) + 
		"\n" + "Equipment packs: " + equipment1roll + ", " + equipment2roll +
		"\n" + "Cantrips: " + str(cantripsroll) +
		"\n" + "Spells: " + str(spellsroll)
		)
    

		
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
