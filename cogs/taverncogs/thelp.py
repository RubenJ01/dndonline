import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext import commands

class thelp():
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    async def tester(self):
        embed = discord.Embed(
            colour = discord.Colour.blue()
        )

        embed.set_author(name="Help menu")
        embed.add_field(name=";faq", value="A list of the faq (format like: ;faq (number))", inline=False)
        embed.add_field(name=";rule", value="A list of the rules (format like: ;rule (number))", inline=False)
        embed.add_field(name=";rprule", value="A list of the rprules (format like: ;rprule (number))", inline=False)
        embed.add_field(name="Support server", value="For any additional support join the official support server: https://discord.gg/GFJMyxu", inline=False)
        await bot.say(embed=embed)           
              
def setup(bot):
    bot.add_cog(thelp(bot))

