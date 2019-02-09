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

background = ["Acolyte", "Criminal", "Folk hero", "Noble", "Sage", "Soldier"]
backgroundroll = random.choice(background)
traits = ["Nervous", "Excited", "Clumsy", "Distant", "Friendly", "Caring", "Anxious", "Laid-back", "Quiet", "Enthousiastic", "Mean", "Pridefull", "Argumentative", "Arrogant", "Blustering", "Rude", "Curious", "Friendly", "Honest", "Hot tempered", "Irritable", "Ponderous", "Suspicous"]
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
flaws = ["Forbidden love or susceptibility to romance", "Enjoys decadent pleasures", "Arrogance", "Prone to rage", "Has a powerfull enemy", "Specific phobia", "Shameful or scandalous history", "Secret crime or misdeed", "Possession of forbidden lore", "Foolhardy bravery"]
flawsroll = random.choice(flaws)
rolls = []
variabeles = []
for j in range(6):	
	for i in range(4):
		rolls.append(randint(1, 6))
		rolls.sort() 	    
	variabeles.append(sum(rolls)-min(rolls))
	rolls =[]
