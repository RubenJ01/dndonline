import discord
from discord.ext import commands

class Command():
    def __init__(self, bot):
        self.bot = bot
    
    @client.command()
    async def tester():
        await self.bot.say('just a test')
            
              
def setup(bot):
    bot.add_cog(Members(bot))
