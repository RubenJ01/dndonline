import random
import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext.commands import Bot 
from dumpfiles.monsterscr import *
from dumpfiles.npcgen import *

class RNG():
    def __init__(self, bot):
        self.bot = bot

@commands.command()
async def ping(self):
    await client.say("pong")

def setup(bot):
    bot.add_cog(RNG(bot))
