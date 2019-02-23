


@commands.command()
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
	await bot.say(embed=embed)
