import random
import discord
from discord.ext import commands
from dumpfiles.monsterscr import *
from dumpfiles.aliases import *

class encountergen():
	def __init__(self, bot):
        	self.bot = bot

	@commands.command(brief=encounterbrief, description=encounterdescription)
	async def encounter(self, level, size):
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
		if level == "1": 	
			if size == "2":
				enc = random.sample(crkwart, 2)			
				embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.sample(crkwart, 3)
				embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4":
				enc = random.sample(crkwart, 4)
				embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.sample(crkwart, 4)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=enc2, inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc = random.sample(crkwart, 1)
				enc2 = random.choice(cr1)
				await self.bot.say(embed=embed)
			if size == "7":
				enc = random.sample(crkwart, 2)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.sample(crkwart, 3)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "2":
			if size == "2":
				enc = random.sample(crhalf, 2)
				embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.sample(crhalf, 3)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4":
				enc = random.sample(crhalf, 1)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.sample(crhalf, 2)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == 6:
				enc = random.sample(crhalf, 6)
				enc2 = random.choice(cr2)
				embed.add_field(name="Enemy's:", value=enc2, inline=False)
				await self.bot.say(embed=embed)
			if size == "7":
				enc = random.sample(crhalf, 1)
				enc2 = random.choice(cr2)
				embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.sample(crhalf, 2)
				enc2 = random.choice(cr2)
				embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "3":
			if size == "2":
				enc = random.sample(crhalf, 2)
				embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.sample(crhalf, 2)
				enc2 = random.sample(crkwart, 1)
				embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "4":
				enc = random.sample(cr2, 1)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.sample(cr2, 1)
				enc2 = random.sample(crhalf, 1)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc = random.choice(cr3)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7":
				enc = random.choice(cr3)
				enc2 = random.choice(crhalf)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr3)
				enc2 = random.sample(crhalf, 2)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "4":
			if size == "2":
				enc = random.choice(cr2)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr2)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "4":
				enc = random.choice(cr3)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr3)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc = random.choice(cr4)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7":
				enc = random.choice(cr4)
				enc2 = random.choice(cr1)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr4)
				enc2 = random.sample(cr1, 2)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "5": 
			if size == "2":
				enc = random.choice(cr3)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr4)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4":
				enc = random.choice(cr4)
				enc2 = random.choice(cr2)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr5)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7":
				enc = random.choice(cr6)
				enc2 = random.choice(cr2)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr6)
				enc2 = random.sample(cr2, 2)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "6":
			if size == "2":
				enc = random.choice(cr4)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr4)
				enc2 = random.choice(cr2)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "4":
				enc = random.choice(cr5)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7":
				enc = random.choice(cr7)
				enc2 = random.choice(cr2)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr7)
				enc2 = random.choice(cr4)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "7":
			if size == "2":
				enc = random.choice(cr4)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr5)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4":
				enc = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc = random.choice(cr7)
				enc2 = random.choice(cr3)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "7":
				enc = random.choice(cr7)
				enc2 = random.choice(cr4)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr7)
				enc2 = random.choice(cr5)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "8":
			if size == "2":
				enc = random.choice(cr4)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr7)
				enc2 = random.choice(cr3)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc = random.choice(cr8)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7":
				enc = random.choice(cr8)
				enc2 = random.choice(cr3)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr8)
				enc2 = random.choice(cr4)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "9":
			if size == "2":
				enc = random.choice(cr5)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4":
				enc = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr8)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc = random.choice(cr9)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr4)
				enc2 = random.choice(cr9)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr9)
				enc2 = random.choice(cr5)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "10":
			if size == "2":
				enc = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr8)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr9)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr10)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr4)
				enc2 = random.choice(cr10)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr10)
				enc2 = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "11":
			if size == "2":
				enc = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr8)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr9)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr10)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr5)
				enc2 = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr11)
				enc2 = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "12":
			if size == "2":
				enc = random.choice(cr6)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr8)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr10)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr6)
				enc2 = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr12)
				enc2 = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "13":
			if size == "2":
				enc = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr8)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr13)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr6)
				enc2 = random.choice(cr13)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr13)
				enc2 = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "14":
			if size == "2":
				enc = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr8)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr13)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr14)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr6)
				enc2 = random.choice(cr14)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr14)
				enc2 = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "15":
			if size == "2":
				enc = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr9)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr13)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr14)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr15)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr6)
				enc2 = random.choice(cr15)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr15)
				enc2 = random.choice(cr7)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "16":
			if size == "2":
				enc = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr15)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr16)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr16)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr11)
				enc2 = random.choice(cr16)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr16)
				enc2 = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "17":
			if size == "2":
				enc = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr13)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr14)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr16)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr17)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr11)
				enc2 = random.choice(cr17)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr17)
				enc2 = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "18":
			if size == "2":
				enc = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr14)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr16)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr18)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr11)
				enc2 = random.choice(cr18)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr18)
				enc2 = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "19":
			if size == "2":
				enc = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr14)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr16)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr17)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr19)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr11)
				enc2 = random.choice(cr19)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr19)
				enc2 = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
		if level == "20":
			if size == "2":
				enc = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "3":
				enc = random.choice(cr15)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "4": 
				enc = random.choice(cr16)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "5":
				enc = random.choice(cr19)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "6":
				enc  = random.choice(cr20)
				embed.add_field(name="Enemy's:", value=str(enc), inline=False)
				await self.bot.say(embed=embed)
			if size == "7": 
				enc = random.choice(cr11)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
			if size == "8":
				enc = random.choice(cr20)
				enc2 = random.choice(cr12)
				embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
				await self.bot.say(embed=embed)
def setup(bot):
	bot.add_cog(encountergen(bot))
