@client.command(brief="Random level 1 character creator")
async def character():

	alignment = ["Lawfull good", "Neutral good", "Chaotic good", "Lawfull neutral", "Neutral", "Chaotic"]
	alignmentroll = random.choice(alignment)

	background = ["Acolyte", "Criminal", "Folk hero", "Noble", "Sage", "Soldier"]
	backgroundroll = random.choice(background)

	proficiency = ["Acrobatics", "Animal Handling", "Arcana", "Athletics", "Deception", "History", "Insight", "Intimidation", "Investigation", "Medicine", "Nature", "Perception", "Performance", "Persuasion", "Religion", "Sleight of Hand", "Stealth", "Survival"]
	proficiencyroll = random.sample(proficiency, 4)

	classes = ["Cleric", "Fighter", "Rogue", "Wizard"]
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
		await client.say(
		"Hit points: 8 + your Constitution modifier" + 
		"\n" + "Alignment: " + alignmentroll + 
		"\n" + "Background: " + backgroundroll +
		"\n" + "Race: " + raceroll + 
		"\n" + "Proficiency's: " + str(proficiencyroll) + 
		"\n" + "Class: " + classesroll + 
		"\n" + "Ability scores: " + str(variabeles) + 
		"\n" + "Equipment packs: " + equipment1roll + ", " + equipment2roll +
		"\n" + "Cantrips: " + str(cantripsroll) +
		"\n" + "Spells: " + str(spellsroll)
		)
	if classesroll == "Fighter":    
		fightingstyle = ["Archery (swap light crossbow and 20 bolts for a longbow and 20 arrows; at your option, also swap chain mail for leather armor)", "Defense", "Dueling", "Great Weapon Fighting (swap longsword and shield for a greataxe", "Protection", "Two-Weapon Fighting (swap longsword for two short swords)"]
		fightingstyleroll = random.choice(fightingstyle)
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		await client.say(
		"Hit points: 10 + your Constitution modifier" +     
		"\n" + "Alignment: " + alignmentroll + 
		"\n" + "Background: " + backgroundroll +
		"\n" + "Race: " + raceroll + 
		"\n" + "Proficiency's: " + str(proficiencyroll) + 
		"\n" + "Class: " + classesroll + 
		"\n" + "Ability scores: " + str(variabeles) +
		"\n" + "Equipment packs: " + equipment1roll + ", " + equipment2roll +	
		"\n" + "Fighting style: " + fightingstyleroll
		)
	if classesroll == "Rogue":
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		await client.say(
		"Hit points: 8 + your Constitution modifier" +     
		"\n" + "Alignment: " + alignmentroll + 
		"\n" + "Background: " + backgroundroll +
		"\n" + "Race: " + raceroll + 
		"\n" + "Proficiency's: " + str(proficiencyroll) + 
		"\n" + "Class: " + classesroll + 
		"\n" + "Ability scores: " + str(variabeles) +
		"\n" + "Equipment packs: " + equipment1roll + ", " + equipment2roll 	
		)
	if classesroll == "Wizard":
		equipment1 = ["Mace", "Scale mail", "Light crossbow and 20 bolts", "Shield", "Holy symbol"]
		equipment1roll = random.choice(equipment1)
		equipment2 = ["Backpack, sack, lantern, 2 oil flasks, tinderbox, 12 pitons, hammer, waterskin, rations (4 days), 5 gp", "Backpack, 2 sacks, 6 torches, 3 oil flasks, tinderbox, 10-foot pole, 50 feet of rope, waterskin, rations (4 days), steel mirror", "Backpack, 4 sacks, holy symbol or thieves’ tools, 12 pitons, 50 feet of rope, waterskin, rations (4 days)"]
		equipment2roll = random.choice(equipment2)
		cantrips = ["Acid splash", "Dancing lights", "Fire bolt", "Light", "Mage hand", "Minor illusion", "Posion spray", "Prestidigation", "Ray of frost", "Shocking grasp"]
		cantripsroll = random.sample(cantrips, 3)
		spells = ["Burning hands", "Charm person", "Comprehend languages", "Detect magic", "Disguise self", "Identify", "Mage armor", "Magic missile", "Shield", "Silent image", "Sleep", "Thunderwave",]
		spellsroll = random.sample(spells, 6)
		await client.say(
		"Hit points: 6 + your Constitution modifier" + 
		"\n" + "Alignment: " + alignmentroll + 
		"\n" + "Background: " + backgroundroll +
		"\n" + "Race: " + raceroll + 
		"\n" + "Proficiency's: " + str(proficiencyroll) + 
		"\n" + "Class: " + classesroll + 
		"\n" + "Ability scores: " + str(variabeles) + 
		"\n" + "Equipment packs: " + equipment1roll + ", " + equipment2roll +
		"\n" + "Cantrips: " + str(cantripsroll) +
		"\n" + "Spells: " + str(spellsroll)
		)
