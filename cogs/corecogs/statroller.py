import random
import discord
from discord.ext import commands
from dumpfiles.aliases import *

class statroller():
	def __init__(self, bot):
        	self.bot = bot
		
	@commands.command(brief=rngstatbrief, description=rngstatdescription)
	async def rngstat(self, amount):
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		counter = 0
		for j in range(int(amount)):
			rolls = random.choices(range(1, 7), k=4)
			total = sum(rolls) - min(rolls)
			counter = counter + 1
			for rank, (position, roll) in enumerate(sorted(enumerate(rolls), reverse=True, key=lambda item: item[1])):
				rolls[position] = f"**{roll}**" if rank < 3 else f"{roll}"
			embed.add_field(name=f'Roll {counter}', value="(" + ", ".join(rolls) + ") " + "= " + str(total), inline=False)
		await self.bot.say(embed=embed)
		
def setup(bot):
	bot.add_cog(statroller(bot))
