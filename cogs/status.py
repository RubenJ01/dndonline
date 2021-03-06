import discord
from discord.ext import commands
from dumpfiles.aliases import *

class status():
	def __init__(self, bot):
        	self.bot = bot
		
	@commands.command(brief=statusbrief, description=statusdescription)
	async def status(self):
		members = len(list(self.bot.get_all_members()))
		servers = len(self.bot.servers)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Bot status", value="Currently running in: " + str(servers) + " servers with: " + str(members) + " members.", inline=False)
		await self.bot.say(embed=embed)
		
def setup(bot):
	bot.add_cog(status(bot))
