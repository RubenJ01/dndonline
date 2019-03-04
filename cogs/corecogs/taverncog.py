import discord
from discord.ext import commands
from dumpfiles.aliases import *

class taverncog():
	def __init__(self, bot):
        	self.bot = bot

	@commands.command(brief=rprulebrief, description=rpruledescription)
	async def rprule(self, number):
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
		await self.bot.say(embed=embed)
		
	@commands.command(brief=rulebrief, description=ruledescription)
	async def rule(self, number):
		embed = discord.Embed(
			colour = discord.Colour.blue()
		)
		if number == "1":
			embed.add_field(name="Rule 1 - #welcome-rules", value="No Malicious Behaviour" + "\n" + "Do not come in here with the intent to raid, brigade, or troll. Intentionally malicious users will be immediately and permanently banned. Come on, people, it’s common sense.", inline=False)
			await self.bot.say(embed=embed)
		if number == "2":
			embed.add_field(name="Rule 2 - #welcome-rules", value="No Obscene Content" + "\n" + "This is a SFW server. Any form of porn/hentai/etc, including links or pics, is forbidden. Erotic roleplay (ERP) is also strictly prohibited. If you must, take it to PMs and fade to black.", inline=False)
			await self.bot.say(embed=embed)		
		if number == "3":
			embed.add_field(name="Rule 3 - #welcome-rules", value="No Spam" + "\n" + " Posting large numbers of superfluous messages for the purposes of cluttering a channel or artificially boosting server rank is prohibited. Express yourself with quality, not by volume.", inline=False)
			await self.bot.say(embed=embed)
		if number == "4":
			embed.add_field(name="Rule 4 - #welcome-rules", value="No Links" + "\n" + "Posting of outside links has been disabled in most channels due to malicious user behaviour.  If you would like to post a link and cannot, ping (@) an online member of Staff and we will be happy to assist.", inline=False)
			await self.bot.say(embed=embed)
		if number == "5":
			embed.add_field(name="Rule 5 - #welcome-rules", value="No Advertising" + "\n" + " Refrain from advertising your own content (YouTube, Twitch, Discord, Social Media, etc) in a public channel without written permission from the Staff. Exceptions may be made if it is specifically related to the channel and discussion you are in (e.g.: if you are an artist in #music-arts-crafts; answering a question in #player-help; if you have been approved for #streaming, etc). That said, PMing links to other users who have asked for them is permitted.", inline=False)
			await self.bot.say(embed=embed)
		if number == "6":
			embed.add_field(name="Rule 6 - #welcome-rules", value="Be Civil" + "\n" + "You are free to engage in polite discussions and intellectual debates; in fact, we encourage it - passionate users are the best! However, avoid sliding into angry public arguments; those belong in your PMs.", inline=False)
			await self.bot.say(embed=embed)
		if number == "7":
			embed.add_field(name="Rule 7 - #welcome-rules", value="No Bullying" + "\n" + "Banter and teasing are fine, as long as it’s in good fun. However, discrimination or hate speech based on race, sex, gender, age, or sexuality is unacceptable. Racial slurs are specifically prohibited. If you are being bullied/harassed (even in PMs), feel free to report it to any member of Staff.", inline=False)
			await self.bot.say(embed=embed)
		if number == "8":
			embed.add_field(name="Rule 8 - #welcome-rules", value="Complaints Are Welcome" + "\n" + "If you have a complaint about Staff or user behaviour, you are welcome to PM any online Staff at any level. If your complaint pertains to a member of Staff, take it one level higher to a Bartender, Innkeeper or Lord, as appropriate. If possible bring evidence of misconduct, such as a screenshot, since it will make our job significantly easier! If the evidence is edited/deleted, contact a Lord, who can check the Deleted Messages Archive.", inline=False)
			await self.bot.say(embed=embed)
		if number == "9":
			embed.add_field(name="Rule 9 - #welcome-rules", value="Respect Staff Decisions" + "\n" + "The Staff reserve the right to make decisions at their own discretion. That said, if you are being unfairly treated, please bring it to the attention of a higher Staff member, as per Rule 6. Not even Staff are above the law.", inline=False)
			await self.bot.say(embed=embed)
		if number == "10":
			embed.add_field(name="Rule 10 - #welcome-rules", value="No Impersonation" + "\n" + "Do not attempt to impersonate server Staff. The job is thankless and the Innkeeper pays us in Copper Pieces, if at all. Don’t make our lives harder.", inline=False)
			await self.bot.say(embed=embed)

    		@commands.command(brief=tavernhelpbrief, description=tavernhelpdescription)
    		async def tavernhelp(self):
			embed = discord.Embed(
			    colour = discord.Colour.blue()
			)

			embed.set_author(name="Help menu")
			embed.add_field(name=";faq", value="A list of the faq (format like: ;faq (number))", inline=False)
			embed.add_field(name=";rule", value="A list of the rules (format like: ;rule (number))", inline=False)
			embed.add_field(name=";rprule", value="A list of the rprules (format like: ;rprule (number))", inline=False)
			embed.add_field(name="Support server", value="For any additional support join the official support server: https://discord.gg/GFJMyxu", inline=False)
			await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(taverncog(bot))
