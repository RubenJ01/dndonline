import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext import commands

class helpcommand():
    def __init__(self, bot):
        self.bot = bot
    
	@commands.command(pass_context=True)
	async def help(self, ctx):
	author = ctx.message.author
	
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name="Help menu")
	embed.add_field(name=";help", value="Shows this message", inline=False)
	embed.add_field(name=";roll", value="roll dice with no advantage or disadvantage when given no parameters 1d20 is rolled parameters can be formatted like so 5d3 4d2 1d21 or simply 10 the latter only works for single dice all dice will be rolled and the total will be returned", inline=False)
	embed.add_field(name=";advantage", value="roll with advantage (format like 4d6 2d8 default is 1d20)", inline=False)
	embed.add_field(name=";disadvantage", value="roll with disadvantage (format like 4d6 2d8 default is 1d20)", inline=False)
	embed.add_field(name=";super-advantage", value="Pick the best of 3 rolls, same format as ;roll", inline=False)
	embed.add_field(name=";super-disadvantage", value="Pick the worst of 3 rolls, same format as ;roll", inline=False)
	embed.add_field(name=";rngstat3", value="Roll 1 ability score 3 times so players can use 1 for their definitive roll (best 3 rolls of a 4d6)", inline=False)
	embed.add_field(name=";rngstat", value="Roll all 6 of your ability scores (best of 3 rolls of a 4d6 6 times)", inline=False)
	embed.add_field(name=";currency", value="Calculate your total amount of pp gp sp cp respectively (format like ;currency 1gp 1pp 20sp etc)", inline=False)
	embed.add_field(name="Initiative tracker", value="The initiative tracker has 4 commands to help you keep track of initiative for your party:" + "\n" + ";initiative (charactername) (modifier) multiple names can be given, this starts the initiative tracker" + "\n" + ";next go to the next turn" + "\n" + ";back go to the previous turn" + "\n" + ";order see the order of rolled initaitives", inline=False)
	embed.add_field(name=";character", value="Generate a quick level 1 character", inline=False)
	embed.add_field(name=";npc", value="Generate a quick npc, including traits and appearence.", inline=False)
	embed.add_field(name=";encounter", value="Make an encounter for your party (format like ;encounter party level party size so for example ;encounter 15 6 this will generate an encounter for a party of level 15 with 6 members, keep in mind that the minimum party size is 2 and the maximum is 8).", inline=False)
	embed.add_field(name=";invite", value="Get an invite link for the discord bot to join your server!", inline=False)
	embed.add_field(name=";spell", value="Find the details of any 5e spell (format like: ;spell spellname)", inline=False)
	embed.add_field(name=";class", value="Find the details of any 5e class (format like: ;spell classname)", inline=False)	
	embed.add_field(name=";basic", value="Get the basic rules pdf", inline=False)
	embed.add_field(name=";about", value="Learn more about the bot", inline=False)
	embed.add_field(name="Official server", value="Please condsider joining support server: https://discord.gg/GFJMyxu", inline=False)
	await bot.send_message(author, embed=embed)
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.add_field(name="Help", value="Sended you a private message which contains the information", inline=False)
	await bot.say(embed=embed)
             
def setup(bot):
    bot.add_cog(thelp(bot))
