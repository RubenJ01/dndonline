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
ideals = ["Aspiration", "Discovery", "Glory", "Nation", "Redemption", "Selfknowledge", "Greed", "Might", "No limits"]
idealsroll = random.choice(ideals)
mannerisms = ["Prone to singing, whistling or humming quietly", "Speaks in rhyme or some other peculiar way", "Particularly low or high voice" , "Slurs words, lisps or stutters", "Enunciates overly clearly", "Speaks loudly", "Whispers", "Uses flowery speech or long words", "Frequently uses the wrong word", "Uses colorful oaths and exclemations", "Makes constant jokes or puns", "Prone to predictions of doom", "Fidgets", "Squints", "Stares into the distance", "Chews something", "Paces", "Taps fingers", "Bites fingernails", "Twirls hair or tugs beard"]
mannrtismroll = random.choice(mannerisms)
talents = ["Plays a musical instrument", "Speaks several langauges fluently", "Unbelievably lucky", "Perfect memory", "Great with animals", "Great with children", "Great at solving puzzles", "Great at one game", "Great at impersonations", "Draws beatifully", "Sings beatifully", "Drinks everyone unde the table", "Expert carpenter", "Expert cook", "Expert dart thrower and rock skipper", "Expert juggler", "Skilled actor and master of disguise", "Skilled dancer", "Knows thieves' cant"]
talentsroll = random.choice(talents)
rolls = []
variabeles = []
for j in range(6):	
	for i in range(4):
		rolls.append(randint(1, 6))
		rolls.sort() 	    
	variabeles.append(sum(rolls)-min(rolls))
	rolls =[]
