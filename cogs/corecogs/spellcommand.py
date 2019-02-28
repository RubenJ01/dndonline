import json
import discord
from discord.ext import commands

class spellcommand():
	def __init__(self, bot):
        	self.bot = bot

	@commands.command(brief="get the details of any 5e spell")
	async def spell(self, *argument):
		spellrequest = " ".join(argument)
		spellfinal = str.casefold(spellrequest)
		with open("databases/spells.json", "r") as spells_json:
			data = json.load(spells_json)
		if spellfinal in data:
			spell_data = data[spellfinal]
			casting_time = spell_data['casting_time']						 
			components = spell_data['components']						 
			description = spell_data['description']						 
			duration = spell_data['duration']						 
			level = spell_data['level']
			rangething = spell_data['range']	
			school = spell_data['school']
			embed = discord.Embed(
				colour = discord.Colour.blue()
			)
			embed.add_field(name="Casting time:", value=f'{casting_time}', inline=False)
			embed.add_field(name="Components:", value=f'{components}', inline=False)
			embed.add_field(name="Duration:", value=f'{duration}', inline=False)
			embed.add_field(name="Spell Level:", value=f'{level}', inline=False)
			embed.add_field(name="Range:", value=f'{rangething}', inline=False)
			embed.add_field(name="School:", value=f'{school}', inline=False)
			embed.add_field(name="Description:", value=f'{description}', inline=False)	
			await self.bot.say(embed=embed)
		else:
			await self.bot.say("Spell non-existent or missing")		

def setup(bot):
	bot.add_cog(spellcommand(bot))
