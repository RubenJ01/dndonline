import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext import commands

class others():
	def __init__(self, bot):
        	self.bot = bot

	@commands.command(brief="information about the Tavern Bot")
	async def about(self):
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="About The Tavern Bot:")
		embed.add_field(name="Date of creation:", value="18-11-2018", inline=False)
		embed.add_field(name="Creators:", value="The Tavern Bot has been developed by: RubenJ01#0229 and Daan#2049")
		embed.add_field(name="Contributors:", value="Thanks to: willdda117#2904 for contributing to The Tavern Bot")
		embed.add_field(name="Source:", value="Since The Tavern Bot is open source you can check ouher repo: https://github.com/RubenJ01/dndonline", inline=False)
		await self.bot.say(embed=embed)

	@commands.command(brief="link to the basic rules for d&d")
	async def basic(self):
		await self.bot.say("http://media.wizards.com/2018/dnd/downloads/DnD_BasicRules_2018.pdf")	

	@commands.command(name="invite", brief="invite the bot to your discord server")
	async def invite(self):
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Invite the bot to your server:", value="https://discordapp.com/oauth2/authorize?client_id=506541896630403080&scope=bot&permissions=0", inline=False)
		await self.bot.say(embed=embed)
		
def setup(bot):
	bot.add_cog(others(bot))
