import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext import commands

class charactergen():
	def __init__(self, bot):
        	self.bot = bot

	@commands.command(brief="generate a level 1 character")
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
			await self.bot.say(embed=embed)
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
			await self.bot.say(embed=embed)
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
			await self.bot.say(embed=embed)
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
			await self.bot.say(embed=embed)
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
			await self.bot.say(embed=embed)
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
			await self.bot.say(embed=embed)
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
			await self.bot.say(embed=embed)


def setup(bot):
	bot.add_cog(encountergen(bot))
