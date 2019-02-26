from dumpfiles.npcgen import *
import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext import commands

class npcgen():
	def __init__(self, bot):
        	self.bot = bot
		
	@commands.command(name="npc", brief="generate an npc that includes appearance, stats and traits" )
	async def npc():
		embed = discord.Embed(
			colour = discord.Colour.blue()
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
