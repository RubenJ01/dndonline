import random
import discord
from discord.ext import commands

class statroller():
	def __init__(self, bot):
        	self.bot = bot

	@commands.command(brief="roll 6 random ability scores")
	async def rngstat(self):
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
		await self.bot.say(embed=embed)
		
	@commands.command(brief="roll 3 random ability scores")
	async def rngstat3(self, amount):
		number = 0				 
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name=f'{amount} randomly generated ability scores')
		for j in range(int(amount)):
			roll1 = int(random.randint(1, 6))
			roll2 = int(random.randint(1, 6))
			roll3 = int(random.randint(1, 6))
			roll4 = int(random.randint(1, 6))
			lowest = min(roll1, roll2, roll3, roll4)
			allrolls = [roll1, roll2, roll3, roll4]
			ability = sum(allrolls) - lowest
			number = number + 1
			embed.add_field(name="Roll " + str(number), value=str(roll1) + ", " + str(roll2) + ", " + str(roll3) + ", " + str(roll4) + " = " + str(ability), inline=False)
		await self.bot.say(embed=embed)
		
	@commands.command(brief="roll a certain stat for example: dexterity")
	async def stat(self, modifier=0):
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		rolls = [randint(1,6) for _ in range(4)]
		embed.add_field(name="Randomly rolled ability score", value=f"the total of the best 3 of your 4 rolls was {sum(rolls)-min(rolls)}", inline=False)
		await self.bot.say(embed=embed)	

def setup(bot):
	bot.add_cog(statroller(bot))
