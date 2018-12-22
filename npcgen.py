import discord
import os
import asyncio
from random import randint
from random import sample
from discord.ext.commands import Bot 
from random import randrange
import random

def npcgen():
	background = ["Acolyte", "Criminal", "Folk hero", "Noble", "Sage", "Soldier"]
	backgroundroll = random.choice(background)
	traits = ["Nervous", "Excited", "Clumsy", "Distant", "Friendly", "Caring", "Anxious", "Laid-back", "Quiet", "Enthousiastic", "Mean", "Pridefull"]
	traitsroll = random.choice(traits)
	gender = ["Male", "Female"]
	genderroll = random.choice(gender)
	size = [3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7]
	sizeroll = random.choice(size)
	hair = ["Long", "Short"]
	hairroll = random.choice(hair)
	haircolour = ["blonde", "black", "white", "orange"]
	haircolourroll = random.choice(haircolour)
	race = ["Hill dwarf", "Mountain dwarf", "High elf", "Wood elf", "Lightfoot halfling", "Stout halfling"]
	raceroll = random.choice(race)
	age = random.randint(20, 100)
	rolls = []
	variabeles = []
	for j in range(6):	
		for i in range(4):
			rolls.append(randint(1, 6))
			rolls.sort() 	    
		variabeles.append(sum(rolls)-min(rolls))
		rolls =[]
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
