import os
import asyncio
import operator
import random
from random import randint
from random import sample
import json
import discord
from discord.ext.commands import Bot 

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

