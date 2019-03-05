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

	@commands.command()
	async def faq(self, number):
		embed = discord.Embed(
			colour=discord.Colour.blue()
		)
		if number == "1":
			embed.add_field(name="1. Where do I start? I’m new to D&D. - #faq",
							value="If you would like a one-on-one tutorial, please post in #player-help. Many users will be reluctant to give you such a tutorial, but luckily, many YouTubers have devoted entire video series to this exact thing! We highly recommend the #resources channel, which you can search for keywords like “tutorial”.  In particular, the Lords recommend the How to Play D&D 5e series from Don’t Stop Thinking: https://www.youtube.com/watch?v=OoW2CDgztKY&list=PLJmFJXf3BXjwXkNFo_-iwtHb24AuJcXqx" + "\n" + "Once you have a firmer grasp of the basics, you will be able to ask for more specific help on the topics you don’t understand. That way, our Staff and users will be able to help you much better!",
							inline=False)
			await self.bot.say(embed=embed)
		if number == "2":
			embed.add_field(name="2. Where do I find games? When is the next game? How often do we run games? - #faq",
							value="You can find ads for games under #party-up.  You can also feel free to post your own Looking for Group, Looking for DM or Looking for Players (LFG, LFDM, LFP) ads to find people for your own game.  If you do, please follow the format outlined in the Pinned Messages for that channel." + "\n" + "Currently, the Tavern is in the process of recruiting more official DMs (the Queen's Guard), with the goal of establishing a regular weekly schedule of games.  When this is completed, the schedule will likely be posted in its own channel, and a link will be placed here. If you would like to interview for the Guard, PM a Captain of Queen's Guard to apply.",
							inline=False)
			await self.bot.say(embed=embed)
		if number == "3":
			embed.add_field(name="3. Do we play/host games other than D&D? - #faq",
							value="Yes!  All tabletop games are welcome, though the vast majority of our traffic is devoted to 5th Edition D&D.  Right now, we only have one channel, #other-rpgs-talk, as well as a channel for #trading-card-games and #video-gaming." + "\n" + "If you would like to start a channel dedicated to another system, please post in #server-suggestions so we can have users vote, react and gauge how much interest there is.  We are always open to adding new channels based on user demand!",
							inline=False)
			await self.bot.say(embed=embed)
		if number == "4":
			embed.add_field(name="4. Why can I not post links/images? - #faq",
							value="Because occasionally, somebody thinks it’s a good idea to post gay furry cuphead porn out of nowhere. Or tries to spread viruses to our users" + "\n" + "Due to malicious user activity, links and images have been heavily restricted in many parts of the server. If you want to post a relevant link, ask a member of Staff and we will be happy to assist you.",
							inline=False)
			await self.bot.say(embed=embed)
		if number == "5":
			embed.add_field(name="5. Where do I find [thing]? What is [channel] for? - #faq",
							value="For a list of all the channels and their purpose, go to #tavern-menu.", inline=False)
			from discord.ext.commands import bot
			await self.bot.say(embed=embed)
		if number == "6":
			embed.add_field(name="6. Can I run a game here? - #faq",
							value="Yes! However, we ask that any DM who wants to run a game in the Tavern first apply for the Queen's Guard, our approved DMs who run games in the server.  If you would like to interview for the Guard, PM a Captain of Queen's Guard to apply." + "\n" + "However, you don’t need to join the Guard just to advertise a game. Feel free to post in #party-up whenever you like, as long as you follow the format in the Pinned Messages for that channel.",
							inline=False)
			await self.bot.say(embed=embed)
		if number == "7":
			embed.add_field(name="7. What do the Staff do? - #faq",
							value="Queen of the Tavern is the founder of the tavern." + "\n" + "Lords of the Tavern are Admins. In addition to the regular duties of an Innkeeper each Lord brings something unique to the tavern" + "\n" + "Innkeepers have shown they are capable Moderators and are trusted with more responsibilities; given the ability to create channels and roles, they can act more autonomously than Bartenders, and help implement or temper the Lords’ ideas." + "Bartenders are Moderators in the Tavern, and like any good Bartender, they are great with people. They settle disputes that get out of hand, but more generally, they interact with the patrons, providing a good face for the Tavern." + "\n" + "Advisors have no permissions or moderator abilities, they serve to help make decisions on moderation issues, and exist as a step prior to becoming a mod.",
							inline=False)
			await self.bot.say(embed=embed)
		if number == "8":
			embed.add_field(name="8. How do I apply for Staff? - #faq",
							value="Currently, new Staff applications are closed.  However, the Staff list does change occasionally. If you would like to signal your interest in being a staff member one day, feel free to fill out the application for the Advisors (trial moderator) role in #announcements." + "\n" + "Remember, we always keep an eye out for users who are regularly active, and who are generally kind, considerate and helpful to their fellow users. When you step up, we notice.",
							inline=False)
			await self.bot.say(embed=embed)
		if number == "9":
			embed.add_field(name="9. What is the Hall of Fame? - #faq",
							value="The Hall of Fame is reserved for users who have distinguished themselves in some way.  Users who are particularly funny, helpful, knowledgeable, clearheaded, etc. may one day find that the staff have voted to give them a golden hero’s crest.",
							inline=False)
			await self.bot.say(embed=embed)
		if number == "10":
			embed.add_field(name="10. What does [abbreviation] mean? - #faq",
							value="See the #faq for a full list of all abbrevations.", inline=False)
			await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(taverncog(bot))
