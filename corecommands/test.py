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

class Fun:
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def ping(self):
        await self.client.say('pong')

