import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext import commands

class status():
	def __init__(self, bot):
        	self.bot = bot
		
	@bot.command(brief="displays the amount of servers the bot is currently running in")
	async def status(self):
		servers = len(bot.servers)
		members = len(list(bot.get_all_members()))
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Bot status", value="Currently running in: " + str(servers) + " servers with: " + str(members) + " members.", inline=False)
		await self.bot.say(embed=embed)
		
def setup(bot):
	bot.add_cog(status(bot))
