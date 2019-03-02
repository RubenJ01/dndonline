import discord
from discord.ext import commands
from dumpfiles.aliases import *

class conditions():
	def __init__(self, bot):
        	self.bot = bot

	@commands.command(brief=conditionbrief, description=conditiondescription)
	async def condition(self, argument):
		condition = str.casefold(argument)
		with open("databases/conditions.json", "r") as conditions_json:
			data = json.load(conditions_json)
		if condition in data:
			conditiondata = data[condition]
			content = conditiondata[content]
			embed = discord.Embed(
				colour = discord.Colour.blue()
			)
			embed.add_field(name=f'Condition {condition}', value=content, inline=False)
			await self.bot.say(embed=embed)
		else:
			await self.bot.say("Condition missing")
def setup(bot):
	bot.add_cog(conditions(bot))
