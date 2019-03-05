from dumpfiles.npcgen import *
import discord
from discord.ext import commands
from dumpfiles.aliases import *


class npcgen():
	def __init__(self, bot):
		self.bot = bot

	@commands.command(name="npc", brief=npcbrief, description=npcdescription)
	async def npc(self):
		embed = discord.Embed(
			colour=discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated NPC:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Gender:", value=genderroll, inline=False)
		embed.add_field(name="Age:", value=age, inline=False)
		embed.add_field(name="Traits:", value=traitsroll, inline=False)
		embed.add_field(name="Flaws & Secrets:", value=flawsroll, inline=False)
		embed.add_field(name="Mannerism:", value=mannerismroll, inline=False)
		embed.add_field(name="Ideal:", value=idealsroll, inline=False)
		embed.add_field(name="Talent:", value=talentsroll, inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Hair:", value=hairroll + ", " + haircolourroll, inline=False)
		embed.add_field(name="Size:", value=sizeroll, inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		await self.bot.say(embed=embed)


def setup(bot):
	bot.add_cog(npcgen(bot))
