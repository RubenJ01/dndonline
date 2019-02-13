import random
import os
import asyncio
import operator
import random
import json
from random import randint
from random import sample

import discord
from discord.ext.commands import Bot 
from monsterscr import *
from npcgen import *


BOT_PREFIX = (";", "/t", "!t")
client = Bot(command_prefix=BOT_PREFIX)
client.remove_command("help")

@client.event
async def on_ready():
    print("I'm in")
    print(client.user)
    await client.change_presence(game=discord.Game(name=';help | #bd-general'))

@client.event
async def on_member_join(member):
	strings = ["Welcome to the Tavern! Please leave your bears at the Bear Post.",
		"Be advised: otters are considered contraband, unless they are members of Staff.",
		"In the event of a catastrophic temporal or dimensional paradox, please avoid making eye contact with your past, future, or alternate selves.",
		"May the Gods have mercy on your soul.",
		"Have a drink. Or don't. That one might be poisoned.",
		"Remember: don't talk about alignment unless you're prepared to argue about alignment.",
		"Selûne is best girl, but don't tell Shar I said so.",
		"The Lords here all worship Loviatar, so make sure to behave unless you like being punished.",
		"Stasis pod malfunction. Prepare to discontinue hypersleep. You have been in stasis for...nine...million...nine...hundred...thousand...",
		"Necromancers be advised: keep the skeletons in your closet.  Nobody wants to see that.",
		"Keep your wands holstered, your weapons sheathed, and your staves slung.",
		"See that gnome in the corner? No? Well, he sees you, so be nice.",
		"We welcome patrons of all races and walks of life...so it's frowned upon to ask the Tabaxi if they are a furry.",
		"We have a gazebo out back for when the weather's nice. Only mildly damaged!",
		"Greeting procedure complete. Prepare for initiation.",
		"Now roll initiative!",
		"Bodies tend to go missing every once in a while, so try not to die."]
	stringspick = random.choice(strings)	
	content = "Welcome to The Tavern " + member.mention + ". " + stringspick
	channel = discord.utils.get(member.server.channels, name="general")
	await client.send_message(channel, content)

@client.command()
async def rprule(number):
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	if number == "1":
		embed.add_field(name="1. No ERP - #out-of-character", value=" Any evidence of erotic roleplay will be punished, to allow as many players as possible to take part in and enjoy the roleplaying experience here, we need to keep this age appropriate; any descriptions of characters based purely on sexual characteristics are deemed inappropriate. ", inline=False)
	elif number == "2":
		embed.add_field(name="2. Respect - #out-of-character", value=" Just treat fellow players with common decency, don't be cruel to anyone, especially if they're asking for advice, at the same time, we understand that debates can break out but when they do keep in mind that you are on a public platform and it's disrespectful to other players to be having large debates.", inline=False)
	elif number == "3":
		embed.add_field(name="3. No Keep OOC, OOC - #out-of-character", value="Out of character content should stay limited to the out of character channel, any content posted in main hall and the other roleplaying channels should be deleted, and if you have to declare the result from a roll or request another player make a roll just use the recommended format laid out later on in the document. ", inline=False)
	elif number == "4":
		embed.add_field(name="4. Approved Characters - #out-of-character", value="Please understand that in order to avoid any chaos created from having waves of unbalanced or unfair characters you need to wait to have your character sheet approved by a Roleplay DM. To get your character approved make sure you follow the character creation rules as laid out later on in the document.", inline=False)
	elif number == "5":
		embed.add_field(name="5. Leave DMing to the DMs - #out-of-character", value="Unless you ask a Roleplay DM, please leave DMing to the DMs; If there is an arc event going on and you need a DM to help keep things going or make an event occur, just hop into an out of character channel and ping the Roleplay DM you need or do a role ping for any Roleplay DM to come in. ", inline=False)
	elif number == "6":
		embed.add_field(name="6. Avoid Spotlighting - #out-of-character", value="We understand you want your character to have a strong personality and that you want your character to have character, but to keep things fair please avoid spotlighting (Trying to steal all the focus on a scene) unless it's a specific arc that really is all about you, and even then, best to stay respectful of your fellow players.", inline=False)
	elif number == "7":
		embed.add_field(name="7. Common Sense - #out-of-character", value="Unless any events spark new rules to be written here, that should be all the basic rules we need, just use your common sense, be respectful, and remember to enjoy yourself while keeping things enjoyable for others!", inline=False)
	elif number == "8":
		embed.add_field(name="8. Third Time Unlucky - #out-of-character", value="We work on a three warnings system, if you break the rules and have received three warnings from Roleplay DMs then your case will be brought up with server staff and may result in a ban from the roleplay channels or a ban from the server itself depending on the severity of your actions.", inline=False)
	elif number == "9":
		embed.add_field(name="9. RTFM - #out-of-character", value="As the sacred scrolls of the Universe dictate: RTFM. Follow this sacred acronym.", inline=False)
	await client.say(embed=embed)
	
@client.command(pass_context=True)
async def combat(ctx, *players_n_health):
	players = {}
	last_added = players_n_health[0]
	for p in players_n_health:
		try:
			n = int(p)
			players[last_added].append(n)
		except ValueError:
			last_added = p
			players[last_added] = []
	for player in players:
		players[player][0] = players[player][0]+randint(1,20)
		await client.say(f"{player} has rolled {players[player][0]} on initiative")
	initiative_order = sorted(players.items(), key=lambda x: -int(x[1][0]))


	while 1:
		for p in initiative_order:
			await client.say(f"it's {p[0]}'s turn with {p[1][1]} hp {f'and {p[1][2]} temp hp' if int(p[1][2]) > 0 else ''}")
			while 1:
				message = await client.wait_for_message(author=ctx.message.author)
				message = message.content.split(' ')
				print(message)
				command = message[0]
				if command == "endcombat" or command == "stop":
					await client.say("```ended combat```")
					return
				elif command == "next":
					break
				else:
					player = message[1]
					if len(players[player]) == 2:
						players[player].append(0)
					if command == "heal":
						 players[player][1] += int(message[2])
					elif command == "damage":
						dmg = players[player][2] - int(message[2]) 
						if dmg < 0:
							players[player][1] += dmg
							players[player][2] = 0
						else:
							players[player][2] = max(dmg, 0)
						if players[player][1] <= 0:
							players[player][1] = 0
							await client.say(f"```{player} is now unconscious```")
							continue
					elif command == "temp":
						players[player][2] = max(players[player][2], int(message[2]))
						
					if players[player][2] == 0:
						await client.say(f"```{player} now has {players[player][1]}hp```")
					else:
						await client.say(f"```{player} now has {players[player][1]}hp and {players[player][2]} temp hp```")


def create_call_to_dnd_beyond(name, link, **kwargs):
	@client.command(name=name, **kwargs)
	async def _func(*name):
		name = " ".join(name)
		name = name.lower().replace(' ', '-').replace("'", "")
		await client.say(f"https://www.dndbeyond.com/{link}/{name}") 
	
def create_roller_function(name, roller, good_roll_text="you managed to roll a fabulous", **command_specifiers):
	@client.command(name=name, **command_specifiers)
	async def _func(*dice):
		embed = discord.Embed(
			colour=discord.Colour.blue()
		)
		if dice:
			if len(dice) == 1 and "d" not in dice[0]:
				dice = list(dice)
				dice[0] =  '1d'+dice[0]
			dice = [die.split("d") for die in dice]
			if len(dice) == 1 and dice[0][0] == '1':
				die_type = int(dice[0][1])
				die_5 = max(1, die_type//5)
				roll = roller(1, die_type)
				if roll > die_5*4 + randint(-die_5, die_5):
					await client.say(f"```{good_roll_text} {roll}```")
				else:

					await client.say(f"```You rolled a {roll}```")
				return
			embed.set_author(name="Dice roller")
			sum_ = 0
			rolls = []
			s = 0
			for die in dice:
				rolls.append([])
				for _ in range(int(die[0])):
					roll = roller(1, int(die[1]))
					sum_ += roll
					rolls[-1].append(str(roll))
				if s:
					embed.add_field(name=f"you also rolled {die[0]}d{die[1]}", value="which became "+'+'.join(rolls[-1]), inline=False)
				else:
					embed.add_field(name=f"You rolled {dice[0][0]}d{dice[0][1]}", value="which became "+'+'.join(rolls[-1]), inline=False)
					s = 1
			embed.add_field(name="Result", value=str(sum_), inline=False)
			await client.say(embed=embed)
		else:
			roll = roller(1, 20)
			if roll > 16 + randint(-4, 4):
				await client.say(f"```{good_roll_text} {roll}```")
			else:
				await client.say(f"```You rolled a {roll}```")

		
create_call_to_dnd_beyond("spell" ,"spells", brief="Get a reference to any spell that is listed in D&D")
create_call_to_dnd_beyond("race", "characters/races", brief="Get a reference to any race that is listed in D&D")
create_call_to_dnd_beyond("classes", "characters/classes", brief="Get a reference to any class that is listed in D&D")
create_call_to_dnd_beyond("background", "characters/backgrounds", brief="Get a reference to any background that is listed in D&D")

create_roller_function(
	"roll",
	randint,
	brief='roll normally (format like "4d6 2d8" default is "1d20")',
    	description="""roll dice with no advantage or disadvantage
	when given no parameters 1d20 is rolled
	parameters can be formatted like so "5d3 4d2 1d21" or simply "10" the latter only works for single dice
	all dice will be rolled and the total will be returned"""
)
create_roller_function(
	"advantage", 
	lambda x, y: max(randint(x,y), randint(x,y)), 
	good_roll_text="thanks to your advantage you managed to roll a(n)",
	brief='roll with advantage (format like "4d6 2d8" default is "1d20")',
    description="""roll dice with disadvantage
	when given no parameters 1d20 is rolled
	parameters can be formatted like so "5d3 4d2 1d21" or "10" the latter only works with single dice
	when rolled every single roll gets an advantage and the total is returned"""
)
create_roller_function(
	"disadvantage",
	lambda x, y: min(randint(x,y), randint(x,y)),
	good_roll_text="despite your disadvantage you managed to roll a(n)",
	brief='roll with disadvantage (format like "4d6 2d8" default is "1d20")',
	description="""roll dice with disadvantage
	when given no parameters 1d20 is rolled
	parameters can be formatted like so "5d3 4d2 1d21" or simply "10" the latter only works with single dice
	when rolled every single roll gets an disadvantage and the total is returned"""
)
create_roller_function(
	"super-advantage",
	lambda x, y: max(randint(x,y), randint(x,y), randint(x,y)), 
	good_roll_text="with super advantage you were probably expecting something high and you were right because you rolled a(n)",
	brief="Pick the best of 3 rolls, same format as ;roll",
)
create_roller_function(
	"super-disadvantage",
	lambda x, y: min(randint(x,y), randint(x,y), randint(x,y)), 
	good_roll_text="despite your super-disadvantage you still managed to roll a(n)",
	brief="Pick the worst of 3 rolls, same format as ;roll"
)

@client.command(name="npc", brief="create a quick npc" )
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

	await client.say(embed=embed)

@client.command(name="invite", brief="Invite the bot to your discord server")
async def invite():
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.add_field(name="Invite the bot to your server:", value="https://discordapp.com/api/oauth2/authorize?client_id=506541896630403080&permissions=0&scope=bot", inline=False)
	await client.say(embed=embed)	

@client.command()
async def spelltest(argument):
    with open("spells.json", "r") as spells_json:
        data = json.load(spells_json)
    spell_data = data[argument]
    casting_time = spell_data['casting_time']						 
    components = spell_data['components']						 
    description = spell_data['description']						 
    duration = spell_data['duration']						 
    level = spell_data['level']
    rangething = spell_data['range']	
    school = spell_data['school']
    await client.say(f'Casting time: {casting_time}')
    await client.say(f'Components: {components}')
    await client.say(f'Description: {description}')
    await client.say(f'Duration: {duration}')
    await client.say(f'Level: {level}')
    await client.say(f'Range: {rangething}')
    await client.say(f'Level: {school}')
					 
@client.command(brief="Welcome!")
async def welcome():
	strings = ["Welcome to the Tavern! Please leave your bears at the Bear Post.",
		"Welcome to the Tavern! Be advised: otters are considered contraband, unless they are members of Staff.",
		"Welcome to the Tavern! In the event of a catastrophic temporal or dimensional paradox, please avoid making eye contact with your past, future, or alternate selves.",
		"Welcome to the Tavern! May the Gods have mercy on your soul.",
		"Welcome to the Tavern! Have a drink. Or don't. That one might be poisoned.",
		"Welcome to the Tavern! Remember: don't talk about alignment unless you're prepared to argue about alignment.",
		"Welcome to the Tavern! Selûne is best girl, but don't tell Shar I said so.",
		"Welcome to the Tavern! The Lords here all worship Loviatar, so make sure to behave unless you like being punished.",
		"Welcome to the Tavern! Stasis pod malfunction. Prepare to discontinue hypersleep. You have been in stasis for...nine...million...nine...hundred...thousand...",
		"Welcome to the Tavern! Necromancers be advised: keep the skeletons in your closet.  Nobody wants to see that.",
		"Welcome to the Tavern! Keep your wands holstered, your weapons sheathed, and your staves slung.",
		"Welcome to the Tavern! See that gnome in the corner? No? Well, he sees you, so be nice.",
		"Welcome to the Tavern! We welcome patrons of all races and walks of life...so it's frowned upon to ask the Tabaxi if they are a furry.",
		"Welcome to the Tavern! We have a gazebo out back for when the weather's nice. Only mildly damaged!",
		"Welcome to the Tavern! Greeting procedure complete. Prepare for initiation.",
		"Welcome to the Tavern! Now roll initiative!",
		"Welcome to the Tavern! Bodies tend to go missing every once in a while, so try not to die."]
	stringspick = random.choice(strings)	   
	await client.say(stringspick)
	
@client.command(brief="About us")
async def about():
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name="About The Tavern Bot:")
	embed.add_field(name="Date of creation:", value="18-11-2018", inline=False)
	embed.add_field(name="Creators:", value="The Tavern Bot has been developed by: RubenJ01#0229 and Daan#2049")
	embed.add_field(name="Contributors:", value="Thanks to: willdda117#2904 for contributing to The Tavern Bot")
	embed.add_field(name="Source:", value="Since The Tavern Bot is open source you can check ouher repo: https://github.com/RubenJ01/dndonline", inline=False)
	await client.say(embed=embed)

initiative_roles = []

@client.command()
async def faq(number):
	if number == "1":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="1. Where do I start? I’m new to D&D. - #faq", value="If you would like a one-on-one tutorial, please post in #player-help. Many users will be reluctant to give you such a tutorial, but luckily, many YouTubers have devoted entire video series to this exact thing! We highly recommend the #resources channel, which you can search for keywords like “tutorial”.  In particular, the Lords recommend the How to Play D&D 5e series from Don’t Stop Thinking: https://www.youtube.com/watch?v=OoW2CDgztKY&list=PLJmFJXf3BXjwXkNFo_-iwtHb24AuJcXqx" + "\n" + "Once you have a firmer grasp of the basics, you will be able to ask for more specific help on the topics you don’t understand. That way, our Staff and users will be able to help you much better!", inline=False)
		await client.say(embed=embed)
	if number == "2":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="2. Where do I find games? When is the next game? How often do we run games? - #faq", value="You can find ads for games under #party-up.  You can also feel free to post your own Looking for Group, Looking for DM or Looking for Players (LFG, LFDM, LFP) ads to find people for your own game.  If you do, please follow the format outlined in the Pinned Messages for that channel." + "\n" + "Currently, the Tavern is in the process of recruiting more official DMs (the Queen's Guard), with the goal of establishing a regular weekly schedule of games.  When this is completed, the schedule will likely be posted in its own channel, and a link will be placed here. If you would like to interview for the Guard, PM a Captain of Queen's Guard to apply.", inline=False)
		await client.say(embed=embed)
	if number == "3":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="3. Do we play/host games other than D&D? - #faq", value="Yes!  All tabletop games are welcome, though the vast majority of our traffic is devoted to 5th Edition D&D.  Right now, we only have one channel, #other-rpgs-talk, as well as a channel for #trading-card-games and #video-gaming." + "\n" + "If you would like to start a channel dedicated to another system, please post in #server-suggestions so we can have users vote, react and gauge how much interest there is.  We are always open to adding new channels based on user demand!", inline=False)
		await client.say(embed=embed)
	if number == "4":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="4. Why can I not post links/images? - #faq", value="Because occasionally, somebody thinks it’s a good idea to post gay furry cuphead porn out of nowhere. Or tries to spread viruses to our users" + "\n" + "Due to malicious user activity, links and images have been heavily restricted in many parts of the server. If you want to post a relevant link, ask a member of Staff and we will be happy to assist you.", inline=False)
		await client.say(embed=embed)
	if number == "5":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="5. Where do I find [thing]? What is [channel] for? - #faq", value="For a list of all the channels and their purpose, go to #tavern-menu.", inline=False)
		await client.say(embed=embed)
	if number == "6":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="6. Can I run a game here? - #faq", value="Yes! However, we ask that any DM who wants to run a game in the Tavern first apply for the Queen's Guard, our approved DMs who run games in the server.  If you would like to interview for the Guard, PM a Captain of Queen's Guard to apply." + "\n" + "However, you don’t need to join the Guard just to advertise a game. Feel free to post in #party-up whenever you like, as long as you follow the format in the Pinned Messages for that channel.", inline=False)
	if number == "7":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="7. What do the Staff do? - #faq", value="Queen of the Tavern is the founder of the tavern." + "\n" + "Lords of the Tavern are Admins. In addition to the regular duties of an Innkeeper each Lord brings something unique to the tavern" + "\n" + "Innkeepers have shown they are capable Moderators and are trusted with more responsibilities; given the ability to create channels and roles, they can act more autonomously than Bartenders, and help implement or temper the Lords’ ideas." + "Bartenders are Moderators in the Tavern, and like any good Bartender, they are great with people. They settle disputes that get out of hand, but more generally, they interact with the patrons, providing a good face for the Tavern." + "\n" + "Advisors have no permissions or moderator abilities, they serve to help make decisions on moderation issues, and exist as a step prior to becoming a mod." ,inline=False)
		await client.say(embed=embed)
	if number == "8":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="8. How do I apply for Staff? - #faq", value="Currently, new Staff applications are closed.  However, the Staff list does change occasionally. If you would like to signal your interest in being a staff member one day, feel free to fill out the application for the Advisors (trial moderator) role in #announcements." + "\n" + "Remember, we always keep an eye out for users who are regularly active, and who are generally kind, considerate and helpful to their fellow users. When you step up, we notice.", inline=False)
		await client.say(embed=embed)
	if number == "9":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="9. What is the Hall of Fame? - #faq", value="The Hall of Fame is reserved for users who have distinguished themselves in some way.  Users who are particularly funny, helpful, knowledgeable, clearheaded, etc. may one day find that the staff have voted to give them a golden hero’s crest.", inline=False)
		await client.say(embed=embed)
	if number == "10":
		embed = discord.Embed(
        		colour = discord.Colour.blue()
    		)
		embed.add_field(name="10. What does [abbreviation] mean? - #faq", value="See the #faq for a full list of all abbrevations.", inline=False)	
		await client.say(embed=embed)
	

@client.command()
async def initiative(*args):
    global initiative_roles
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    for x in range(0,len(args),2):
        initiative_role = random.randint(1,20)
        if initiative_role != 1:
            initiative_role += int(args[x+1])
        output = args[x]
        output += " your initiative is "
        output += str(initiative_role)
        initiative_roles += [[args[x],int(initiative_role)]]
        embed.add_field(name="Initiative roll", value=output, inline=False)

    initiative_roles.sort(key=lambda x: x[1])
    initiative_roles.reverse()

    output = "The order of combat is "
    for y in range(0,len(initiative_roles)):
        output += initiative_roles[y][0]
        output +=", "
    embed.add_field(name="Combat order", value=output, inline=False)   

    output = "It's the turn of "
    output += str(initiative_roles[0][0])
    embed.add_field(name="Turn", value=output, inline=False)
    await client.say(embed=embed)

@client.command()
async def next():
    global initiative_roles
    initiative_roles += [initiative_roles[0]]
    del initiative_roles[0]
    output = "It's the turn of "
    output += str(initiative_roles[0][0])
    output += ", "
    output += str(initiative_roles[1][0])
    output += " is next."
    embed = discord.Embed(
        colour = discord.Colour.blue()
    )
    embed.add_field(name=";next", value=output, inline=False)
    await client.say(embed=embed)


@client.command()
async def stop():
    global initiative_roles
    initiative_roles = []
    embed = discord.Embed(
    	colour = discord.Colour.blue()
    )
    embed.add_field(name=";stop", value="Initiative cleared", inline=False)
    await client.say(embed=embed)

@client.command()
async def order():
    global initiative_roles
    embed = discord.Embed(
    	colour = discord.Colour.blue()
    )
    initiative_roles.sort(key=lambda x: x[1])
    initiative_roles.reverse()
    output = "The order of combat is "
    for y in range(0,len(initiative_roles)):
        output += initiative_roles[y][0]
        output +=", "
    embed.add_field(name=";restart", value=output, inline=False)
    await client.say(embed=embed)

@client.command()
async def back():
    global initiative_roles
    embed = discord.Embed(
    	colour = discord.Colour.blue()
    )
    initiative_roles =[initiative_roles[-1]] + initiative_roles
    del initiative_roles[-1]
    output = "It's the turn of "
    output += str(initiative_roles[0][0])
    output += ", "
    output += str(initiative_roles[1][0])
    output += " is next."
    embed.add_field(name=";back", value=output, inline=False)
    await client.say(embed=embed)

		
@client.command(brief="Roll a certain stat for example: dexterity")
async def stat(modifier=0):
	rolls = [randint(1,6) for _ in range(4)]
	await client.say(f"the total of the best 3 of your 4 rolls was {sum(rolls)-min(rolls)}")			     
	
@client.command(brief="Calculate your total amount of pp gp sp cp respectively")
async def currency(*coins):
    cp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "cp"])
    sp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "sp"])
    ep = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "ep"])
    gp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "gp"])
    pp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "pp"])
    total = (cp * 1) + (sp * 10) + (ep * 50) + (gp * 100) + (pp * 1000)
    cp = total%10
    total = total//10
    sp = total%10
    total = total//10
    gp = total%10
    total = total//10
    pp = total
    embed = discord.Embed(
    	colour = discord.Colour.blue()
    )
    embed.add_field(name="Currency", value="You have " + str(cp) + "cp "  + str(sp) + "sp " + str(gp) + "gp " + str(pp) + "pp ", inline=False)
    await client.say(embed=embed)

@client.command()
async def status():
	servers = len(client.servers)
	members = len(list(client.get_all_members()))
	embed = discord.Embed(
 		colour = discord.Colour.blue()
 	)
	embed.add_field(name="Bot status", value="Currently running in: " + str(servers) + " servers with: " + str(members) + " members.", inline=False)
	await client.say(embed=embed)

@client.command()
async def test(*test, init):
	rolls = []
	variabeles = []
	for j in range(6):	
		for i in range(4):
			rolls.append(randint(1, 6))
			rolls.sort() 	    
		variabeles.append(sum(rolls)-min(rolls))
		rolls =[]
	total = init + variabeles
	await client.say(test + total)

@client.command(brief="Reference 1 of the server rules")
async def rule(number):
	if number == "1":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 1 - #welcome-rules", value="No Malicious Behaviour" + "\n" + "Do not come in here with the intent to raid, brigade, or troll. Intentionally malicious users will be immediately and permanently banned. Come on, people, it’s common sense.", inline=False)
		await client.say(embed=embed)
	if number == "2":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 2 - #welcome-rules", value="No Obscene Content" + "\n" + "This is a SFW server. Any form of porn/hentai/etc, including links or pics, is forbidden. Erotic roleplay (ERP) is also strictly prohibited. If you must, take it to PMs and fade to black.", inline=False)
		await client.say(embed=embed)		
	if number == "3":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 3 - #welcome-rules", value="No Spam" + "\n" + " Posting large numbers of superfluous messages for the purposes of cluttering a channel or artificially boosting server rank is prohibited. Express yourself with quality, not by volume.", inline=False)
		await client.say(embed=embed)
	if number == "4":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 4 - #welcome-rules", value="No Links" + "\n" + "Posting of outside links has been disabled in most channels due to malicious user behaviour.  If you would like to post a link and cannot, ping (@) an online member of Staff and we will be happy to assist.", inline=False)
		await client.say(embed=embed)
	if number == "5":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 5 - #welcome-rules", value="No Advertising" + "\n" + " Refrain from advertising your own content (YouTube, Twitch, Discord, Social Media, etc) in a public channel without written permission from the Staff. Exceptions may be made if it is specifically related to the channel and discussion you are in (e.g.: if you are an artist in #music-arts-crafts; answering a question in #player-help; if you have been approved for #streaming, etc). That said, PMing links to other users who have asked for them is permitted.", inline=False)
		await client.say(embed=embed)
	if number == "6":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 6 - #welcome-rules", value="Be Civil" + "\n" + "You are free to engage in polite discussions and intellectual debates; in fact, we encourage it - passionate users are the best! However, avoid sliding into angry public arguments; those belong in your PMs.", inline=False)
		await client.say(embed=embed)
	if number == "7":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 7 - #welcome-rules", value="No Bullying" + "\n" + "Banter and teasing are fine, as long as it’s in good fun. However, discrimination or hate speech based on race, sex, gender, age, or sexuality is unacceptable. Racial slurs are specifically prohibited. If you are being bullied/harassed (even in PMs), feel free to report it to any member of Staff.", inline=False)
		await client.say(embed=embed)
	if number == "8":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 8 - #welcome-rules", value="Complaints Are Welcome" + "\n" + "If you have a complaint about Staff or user behaviour, you are welcome to PM any online Staff at any level. If your complaint pertains to a member of Staff, take it one level higher to a Bartender, Innkeeper or Lord, as appropriate. If possible bring evidence of misconduct, such as a screenshot, since it will make our job significantly easier! If the evidence is edited/deleted, contact a Lord, who can check the Deleted Messages Archive.", inline=False)
		await client.say(embed=embed)
	if number == "9":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 9 - #welcome-rules", value="Respect Staff Decisions" + "\n" + "The Staff reserve the right to make decisions at their own discretion. That said, if you are being unfairly treated, please bring it to the attention of a higher Staff member, as per Rule 6. Not even Staff are above the law.", inline=False)
		await client.say(embed=embed)
	if number == "10":
		embed = discord.Embed(
 		colour = discord.Colour.blue()
 		)
		embed.add_field(name="Rule 10 - #welcome-rules", value="No Impersonation" + "\n" + "Do not attempt to impersonate server Staff. The job is thankless and the Innkeeper pays us in Copper Pieces, if at all. Don’t make our lives harder.", inline=False)
		await client.say(embed=embed)
		
		
	
@client.command(brief="Random level 1 character creator")
async def character():
	alignment = ["Lawfull good", "Neutral good", "Chaotic good", "Lawful neutral", "Neutral", "Chaotic"]
	alignmentroll = random.choice(alignment)

	background = ["Acolyte", "Criminal", "Folk hero", "Noble", "Sage", "Soldier"]
	backgroundroll = random.choice(background)

	proficiency = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
	proficiencyroll = random.sample(proficiency, 4)

	classes = ["Cleric", "Fighter", "Rogue", "Wizard", "Ranger", "Druid", "Bard"]
	classesroll = random.choice(classes)

	race = ["Hill dwarf", "Mountain dwarf", "High elf", "Wood elf", "Lightfoot halfling", "Stout halfling"]
	raceroll = random.choice(race)


	rolls = []
	variabeles = []
	for j in range(6):    
		for i in range(4):
			rolls.append(randint(1, 6))
			rolls.sort()         
		variabeles.append(sum(rolls)-min(rolls))
		rolls =[]	
	if classesroll == "Cleric": 
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		cantrips = ["Guidance", "light", "Resistance", "Sacred flame", "Spare the dying", "Thaumaturgy"]
		cantripsroll = random.sample(cantrips, 3)
		spells = ["Bless", "Command", "Cure wounds", "Detect magic", "Guiding bolt", "Healing word", "Inflict wounds", "Sanctuary", "Schield of faith"]
		spellsroll = random.sample(spells, 2)
		embed = discord.Embed(
		colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="8 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		embed.add_field(name="Cantrips:", value=', '.join(cantripsroll), inline=False)
		embed.add_field(name="Spells:", value=', '.join(spellsroll), inline=False)
		await client.say(embed=embed)
	if classesroll == "Fighter": 
		fightingstyle = ["Archery (swap light crossbow and 20 bolts for a longbow and 20 arrows; at your option, also swap chain mail for leather armor)", "Defense", "Dueling", "Great Weapon Fighting (swap longsword and shield for a greataxe", "Protection", "Two-Weapon Fighting (swap longsword for two short swords)"]
		fightingstyleroll = random.choice(fightingstyle)
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="10 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		embed.add_field(name="Fightingstyle:", value=fightingstyleroll, inline=False)
		await client.say(embed=embed)
	if classesroll == "Rogue":
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="8 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		await client.say(embed=embed)
	if classesroll == "Wizard":
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		cantrips = ["Acid splash", "Dancing lights", "Fire bolt", "Light", "Mage hand", "Minor illusion", "Posion spray", "Prestidigation", "Ray of frost", "Shocking grasp"]
		cantripsroll = random.sample(cantrips, 3)
		spells = ["Burning hands", "Charm person", "Comprehend languages", "Detect magic", "Disguise self", "Identify", "Mage armor", "Magic missile", "Shield", "Silent image", "Sleep", "Thunderwave",]
		spellsroll = random.sample(spells, 6)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="6 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		embed.add_field(name="Cantrips:", value=', '.join(cantripsroll), inline=False)
		embed.add_field(name="Spells:", value=', '.join(spellsroll), inline=False)
		await client.say(embed=embed)
	if classesroll == "Ranger":
		equipment1 = ["Scale Mail", "Leather Armor"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Two shortswords", "Two simple melee weapons"]
		equipment2roll = random.choice(equipment2)
		equipment3 = ["a Dungeoneer's Pack", "An Explorer's Pack, A Longbow and a Quiver of 20 Arrows"]
		equipment3roll = random.choice(equipment3)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="6 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll + ", " + equipment3roll, inline=False)
		await client.say(embed=embed)
	if classesroll == "Druid":
		equipment1 = ["A wooden schield", "Any simple weapon"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["A Scimitar", "any simple melee weapon, Leather Armor, an Explorer's Pack, and a druidic focus"]
		equipment2roll = random.choice(equipment2)
		spells = ["Absorb Elements", "Animal Friendship", "Beast bond", "Charm Person", "Create or Destroy water", "Cure wounds", "Detect Magic"]
		spellsroll = random.sample(spells, 2)
		cantripsroll = random.sample(cantrips, 2)
		cantrips = ["Control Flames", "Create Bonfire", "Druidcraft", "Frostbite", "Guidance", "Gust", "Infestation", "Magic Stone", "Mending", "Mold Earth"]
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="8 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll, inline=False)
		embed.add_field(name="Cantrips:", value=', '.join(cantripsroll), inline=False)
		embed.add_field(name="Spells:", value=', '.join(spellsroll), inline=False)
		await client.say(embed=embed)
	if classesroll == "Bard":
		equipment1 = ["A Rapier", "A longsword", "Any simple weapon"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["A diplomat's pack", "An entertainer's pack"]
		equipment2roll = random.choice(equipment2)
		equipment3 = ["A lute", "any other musical instrument Leather Armor, and a Dagger"]
		equipment3roll = random.choice(equipment3)
		cantrips = ["Blade Ward", "Dancing Lights", "Friends", "Light", "Mage Hand", "Mending", "Message", "Minor Illusion", "Prestidigation", "Thunderclap", "True Strike", "Vicious Mockery"]
		cantripsroll = random.sample(cantrips, 2)
		spells = ["Animal Friendship", "Bane", "Charm Person", "Comprehend Languages", "Cure Wounds", "Detect Magic", "Disguise Self", "Dissonant Whispers", "Earth Tremor", "Fearie Fire", "Feather Fall", "Healing Word", "Heroism", "Identify", "Illusory Script", "Longstrider", "Silent Image", "Sleep", "Speak with Animals", "Tasha's Hideous Laughter", "Thunderwave", "Unseen servant"]
		spellsroll = random.sample(spells, 2)
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.set_author(name="Randomly generated character:")
		embed.add_field(name="Race:", value=raceroll, inline=False)
		embed.add_field(name="Class:", value=classesroll, inline=False)
		embed.add_field(name="Hit points:", value="8 + your Constitution modifier", inline=False)
		embed.add_field(name="Ability scores:", value=', '.join([str(v) for v in variabeles]), inline=False)
		embed.add_field(name="Background:", value=backgroundroll, inline=False)
		embed.add_field(name="Alignment::", value=alignmentroll, inline=False)
		embed.add_field(name="Proficiency's:", value=', '.join(proficiencyroll), inline=False)
		embed.add_field(name="Equipmentpacks:", value=equipment1roll + ", " + equipment2roll + ", " + equipment3roll, inline=False)
		embed.add_field(name="Cantrips:", value=', '.join(cantripsroll), inline=False)
		embed.add_field(name="Spells:", value=', '.join(spellsroll), inline=False)
		await client.say(embed=embed)

@client.command()
async def rngstat():
	number = 0				 
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name=" Randomly generated ability scores")
	for j in range(6):
		roll1 = int(random.randint(1, 6))
		roll2 = int(random.randint(1, 6))
		roll3 = int(random.randint(1, 6))
		roll4 = int(random.randint(1, 6))
		lowest = min(roll1, roll2, roll3, roll4)
		allrolls = [roll1, roll2, roll3, roll4]
		ability = sum(allrolls) - lowest
		number = number + 1			 
		embed.add_field(name="Roll " + str(number), value=str(roll1) + ", " + str(roll2) + ", " + str(roll3) + ", " + str(roll4) + " = " + str(ability), inline=False)
	await client.say(embed=embed)

@client.command()
async def rngstat3():
	number = 0				 
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.set_author(name="3 randomly generated ability scores")
	for j in range(3):
		roll1 = int(random.randint(1, 6))
		roll2 = int(random.randint(1, 6))
		roll3 = int(random.randint(1, 6))
		roll4 = int(random.randint(1, 6))
		lowest = min(roll1, roll2, roll3, roll4)
		allrolls = [roll1, roll2, roll3, roll4]
		ability = sum(allrolls) - lowest
		number = number + 1
		embed.add_field(name="Roll " + str(number), value=str(roll1) + ", " + str(roll2) + ", " + str(roll3) + ", " + str(roll4) + " = " + str(ability), inline=False)
	await client.say(embed=embed)

			

@client.command(brief="The definitions of combat conditions")
async def condition(type):
	if type == "blinded":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition blinded:", value="A blinded creature can’t see and automatically fails any ability check that requires sight." + "\n" + "Attack rolls against the creature have advantage, and the creature’s Attack rolls have disadvantage.", inline=False)
		await client.say(embed=embed)
	if type == "charmed":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition charmed:", value="A charmed creature can’t Attack the charmer or target the charmer with harmful Abilities or magical effects." + "\n" + "The charmer has advantage on any ability check to interact socially with the creature.", inline=False)
		await client.say(embed=embed)
	if type == "frightened":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition frightened:", value="A frightened creature has disadvantage on Ability Checks and Attack rolls while the source of its fear is within line of sight." + "\n" + "The creature can’t willingly move closer to the source of its fear.", inline=False)
		await client.say(embed=embed)
	if type == "deafened":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition deafened:", value="A deafened creature can’t hear and automatically fails any ability check that requires hearing.", inline=False)
		await client.say(embed=embed)	
	if type == "grappled":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition grappled:", value="A grappled creature’s speed becomes 0, and it can’t benefit from any bonus to its speed." + "\n" + "The condition ends if the Grappler is incapacitated (see the condition)." + "\n" + "The condition also ends if an effect removes the grappled creature from the reach of the Grappler or Grappling effect, such as when a creature is hurled away by the Thunderwave spell.", inline=False)
		await client.say(embed=embed)
	if type == "incapacitated":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition incapacitated:", value="An incapacitated creature can’t take actions or reactions.", inline=False)
		await client.say(embed=embed)
	if type == "invisible":
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition invisible:", value="An invisible creature is impossible to see without the aid of magic or a Special sense. For the purpose of Hiding, the creature is heavily obscured. The creature’s location can be detected by any noise it makes or any tracks it leaves." + "\n" + "Attack rolls against the creature have disadvantage, and the creature’s Attack rolls have advantage.", inline=False)
		await client.say(embed=embed)
	if type == "paralyzed": 
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		embed.add_field(name="Condition paralyzed:", value="A paralyzed creature is incapacitated (see the condition) and can’t move or speak." + "\n" + "The creature automatically fails Strength and Dexterity Saving Throws." + "\n" + "Attack rolls against the creature have advantage." + "\n" + "Any Attack that hits the creature is a critical hit if the attacker is within 5 feet of the creature.", inline=False)
		await client.say(embed=embed)

@client.command()
async def basic():
	await client.say("http://media.wizards.com/2018/dnd/downloads/DnD_BasicRules_2018.pdf")
		
@client.command(pass_context=True)
async def help(ctx):
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
	embed.add_field(name=";rngstat", value="Roll 1 ability score (best 3 rolls of a 4d6)", inline=False)
	embed.add_field(name=";rngstat3", value="Roll 1 ability score 3 times so players can use 1 for their definitive roll (best 3 rolls of a 4d6)", inline=False)
	embed.add_field(name=";rngstat", value="Roll all 6 of your ability scores (best of 3 rolls of a 4d6 6 times)", inline=False)
	embed.add_field(name=";currency", value="Calculate your total amount of pp gp sp cp respectively (format like ;currency 1gp 1pp 20sp etc)", inline=False)
	embed.add_field(name="Initiative tracker", value="The initiative tracker has 4 commands to help you keep track of initiative for your party:" + "\n" + ";initiative (charactername) (modifier) multiple names can be given, this starts the initiative tracker" + "\n" + ";next go to the next turn" + "\n" + ";back go to the previous turn" + "\n" + ";order see the order of rolled initaitives", inline=False)
	embed.add_field(name=";character", value="Generate a quick level 1 character", inline=False)
	embed.add_field(name=";npc", value="Generate a quick npc, including traits and appearence.", inline=False)
	embed.add_field(name=";encounter", value="Make an encounter for your party (format like ;encounter party level party size so for example ;encounter 15 6 this will generate an encounter for a party of level 15 with 6 members, keep in mind that the minimum party size is 2 and the maximum is 8).", inline=False)
	embed.add_field(name=";invite", value="Get an invite link for the discord bot to join your server!", inline=False)
	embed.add_field(name=";welcome", value="Welcome new patrons to the server with a unique welcoming message", inline=False)
	embed.add_field(name=";faq", value="Get a refernce to any question listed in the faq, format like ;faq 1", inline=False)
	embed.add_field(name=";rule", value="Get a reference to every single rule listed inn the tavern (format like: rule(number of rule)).", inline=False)
	embed.add_field(name=";basic", value="Get the basic rules pdf", inline=False)
	embed.add_field(name=";about", value="Learn more about the bot", inline=False)
	embed.add_field(name="Official server", value="Please condsider joining ouher official server: https://discord.gg/sYPVXv8", inline=False)
	await client.send_message(author, embed=embed)
	embed = discord.Embed(
		colour = discord.Colour.blue()
	)
	embed.add_field(name="Help", value="Sended you a private message which contains the information", inline=False)
	await client.say(embed=embed)
	
@client.command(brief="An encounter generator for d&d 5e")
async def encounter(level, size):
	if level == "1": 	
		if size == "2":
			enc = random.sample(crkwart, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.sample(crkwart, 3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.sample(crkwart, 4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.sample(crkwart, 4)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=enc2, inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.sample(crkwart, 1)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.sample(crkwart, 2)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.sample(crkwart, 3)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "2":
		if size == "2":
			enc = random.sample(crhalf, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.sample(crhalf, 3)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.sample(crhalf, 1)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.sample(crhalf, 2)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == 6:
			enc = random.sample(crhalf, 6)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=enc2, inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.sample(crhalf, 1)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.sample(crhalf, 2)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "3":
		if size == "2":
			enc = random.sample(crhalf, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.sample(crhalf, 2)
			enc2 = random.sample(crkwart, 1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=', '.join(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.sample(cr2, 1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.sample(cr2, 1)
			enc2 = random.sample(crhalf, 1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr3)
			enc2 = random.choice(crhalf)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr3)
			enc2 = random.sample(crhalf, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
			await client.say(embed=embed)
	if level == "4":
		if size == "2":
			enc = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr2)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc =  random.choice(cr3)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr4)
			enc2 = random.choice(cr1)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr4)
			enc2 = random.sample(cr1, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
			await client.say(embed=embed)
	if level == "5": 
		if size == "2":
			enc = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr4)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr6)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr6)
			enc2 = random.sample(cr2, 2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + ', '.join(enc2), inline=False)
			await client.say(embed=embed)
	if level == "6":
		if size == "2":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr4)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr7)
			enc2 = random.choice(cr2)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr7)
			enc2 = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "7":
		if size == "2":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr7)
			enc2 = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr7)
			enc2 = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr7)
			enc2 = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "8":
		if size == "2":
			enc = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr7)
			enc2 = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7":
			enc = random.choice(cr8)
			enc2 = random.choice(cr3)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr8)
			enc2 = random.choice(cr4)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "9":
		if size == "2":
			enc = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr4)
			enc2 = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr9)
			enc2 = random.choice(cr5)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "10":
		if size == "2":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr10)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr4)
			enc2 = random.choice(cr10)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr10)
			enc2 = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "11":
		if size == "2":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr10)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr5)
			enc2 = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr11)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "12":
		if size == "2":
			enc = random.choice(cr6)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr10)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr12)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "13":
		if size == "2":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr13)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "14":
		if size == "2":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr8)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr14)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "15":
		if size == "2":
			enc = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr9)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr15)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr6)
			enc2 = random.choice(cr15)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr15)
			enc2 = random.choice(cr7)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "16":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr15)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr16)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "17":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr13)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr17)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr17)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr17)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "18":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr18)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr18)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr18)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "19":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr14)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr17)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr19)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr19)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr19)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
	if level == "20":
		if size == "2":
			enc = random.choice(cr11)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "3":
			enc = random.choice(cr15)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "4": 
			enc = random.choice(cr16)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "5":
			enc = random.choice(cr19)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "6":
			enc  = random.choice(cr20)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc), inline=False)
			await client.say(embed=embed)
		if size == "7": 
			enc = random.choice(cr11)
			enc2 = random.choice(cr20)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
		if size == "8":
			enc = random.choice(cr20)
			enc2 = random.choice(cr12)
			embed = discord.Embed(
			colour = discord.Colour.blue()
			)
			embed.set_author(name="Encounter for party level: " + str(level) +  " and, " + str(size) + " party members")
			embed.add_field(name="Enemy's:", value=str(enc) + ", " + str(enc2), inline=False)
			await client.say(embed=embed)
													
														
async def list_servers():
    await client.wait_until_ready()
    while not client.is_closed:
        print("Current servers in which the bot is running:")
        for server in client.servers:
            print(server.name)
        await asyncio.sleep(600)
			
token = os.environ.get("DISCORD_BOT_SECRET")
client.loop.create_task(list_servers())
client.run(token)
