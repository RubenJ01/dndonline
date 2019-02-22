import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext import commands

class Members():
    def __init__(self, bot):
        self.bot = bot
    
    @client.command()
    async def tester(self):
        await self.bot.say('just a test')
            
              
def setup(bot):
    bot.add_cog(Members(bot))
