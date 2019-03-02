import discord
from discord.ext import commands
from dumpfiles.aliases import *

class conditions():
	def __init__(self, bot):
        	self.bot = bot
	
	@commands.command(brief=conditionbrief, description=conditiondescription)
	async def condition(self, type):
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)	
		if type == "blinded":
			embed.add_field(name="Condition blinded:", value="A blinded creature can’t see and automatically fails any ability check that requires sight." + "\n" + "Attack rolls against the creature have advantage, and the creature’s Attack rolls have disadvantage.", inline=False)
			await self.bot.say(embed=embed)
		if type == "charmed":
			await self.bot.say(embed=embed)
		if type == "frightened":
			embed.add_field(name="Condition frightened:", value="A frightened creature has disadvantage on Ability Checks and Attack rolls while the source of its fear is within line of sight." + "\n" + "The creature can’t willingly move closer to the source of its fear.", inline=False)
			await self.bot.say(embed=embed)
		if type == "deafened":
			embed.add_field(name="Condition deafened:", value="A deafened creature can’t hear and automatically fails any ability check that requires hearing.", inline=False)
			await self.bot.say(embed=embed)	
		if type == "grappled":
			embed.add_field(name="Condition grappled:", value="A grappled creature’s speed becomes 0, and it can’t benefit from any bonus to its speed." + "\n" + "The condition ends if the Grappler is incapacitated (see the condition)." + "\n" + "The condition also ends if an effect removes the grappled creature from the reach of the Grappler or Grappling effect, such as when a creature is hurled away by the Thunderwave spell.", inline=False)
			await self.bot.say(embed=embed)
		if type == "incapacitated":
			embed.add_field(name="Condition incapacitated:", value="An incapacitated creature can’t take actions or reactions.", inline=False)
			await self.bot.say(embed=embed)
		if type == "invisible":
			embed.add_field(name="Condition invisible:", value="An invisible creature is impossible to see without the aid of magic or a Special sense. For the purpose of Hiding, the creature is heavily obscured. The creature’s location can be detected by any noise it makes or any tracks it leaves." + "\n" + "Attack rolls against the creature have disadvantage, and the creature’s Attack rolls have advantage.", inline=False)
			await self.bot.say(embed=embed)
		if type == "paralyzed": 
			embed.add_field(name="Condition paralyzed:", value="A paralyzed creature is incapacitated (see the condition) and can’t move or speak." + "\n" + "The creature automatically fails Strength and Dexterity Saving Throws." + "\n" + "Attack rolls against the creature have advantage." + "\n" + "Any Attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.", inline=False)
			await self.bot.say(embed=embed)
	

def setup(bot):
	bot.add_cog(conditions(bot))
