import json
import discord
from discord.ext import commands

class classcommand():
	def __init__(self, bot):
        	self.bot = bot

	@commands.command(name='class', brief="get the details any 5e class")
	async def class_command(self, *argument):
		classrequest = " ".join(argument)
		classfinal = str.casefold(classrequest)
		with open("databases/classes.json", "r") as classes_json:
			data = json.load(classes_json, strict=False)
		if classfinal in data:
			class_data = data[classfinal]
			hitdice = class_data['hit_dice']
			hitpointslevel1 = class_data['hit_points_at_1st_level']
			hitpointshigher = class_data['hit_points_at_higher_levels']
			armor = class_data['armor']
			weapons = class_data['weapons']
			tools = class_data['tools']
			savingthrows = class_data['saving_throws']
			skills = class_data['skills']
			equipment1 = class_data['equipment1']
			equipment2 = class_data['equipment2']
			equipment3 = class_data['equipment3']
			quickbuild = class_data['quickbuild']
			leveling = class_data['levelingtable']
			embed = discord.Embed(
				colour = discord.Colour.blue()
			)
			embed.set_author(name=f'The {classfinal} class')
			embed.add_field(name="Hit points", value=f'Hit dice: {hitdice}' + "\n" + f'Hit points at 1st level: {hitpointslevel1}' + "\n" + f'Hit points at higher levels: {hitpointshigher}', inline=False)
			embed.add_field(name="Proficiencies", value=f'Armor: {armor}' + "\n" + f'Weapons: {weapons}' + "\n" + f'Tools: {tools}' + "\n" + f'Saving throws: {savingthrows}' + "\n" + f'Skills: {skills}', inline=False)
			embed.add_field(name="Equipment", value="You start with the following equipment, in addition to the equipment granted by your background:" + "\n" + str(equipment1) + "\n" + str(equipment2) + "\n" + str(equipment3), inline=False)
			embed.add_field(name=f'The {classfinal}', value=leveling, inline=False) 
			embed.add_field(name="Quick build", value=quickbuild, inline=False)
			await self.bot.say(embed=embed)
		else:
			await self.bot.say("Class non-existent or missing")

def setup(bot):
	bot.add_cog(classcommand(bot))
