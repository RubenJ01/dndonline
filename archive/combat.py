@bot.command(pass_context=True)
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
		await bot.say(f"{player} has rolled {players[player][0]} on initiative")
	initiative_order = sorted(players.items(), key=lambda x: -int(x[1][0]))


	while 1:
		for p in initiative_order:
			await bot.say(f"it's {p[0]}'s turn with {p[1][1]} hp {f'and {p[1][2]} temp hp' if int(p[1][2]) > 0 else ''}")
			while 1:
				message = await bot.wait_for_message(author=ctx.message.author)
				message = message.content.split(' ')
				print(message)
				command = message[0]
				if command == "endcombat" or command == "stop":
					await bot.say("```ended combat```")
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
							await bot.say(f"```{player} is now unconscious```")
							continue
					elif command == "temp":
						players[player][2] = max(players[player][2], int(message[2]))
						
					if players[player][2] == 0:
						await bot.say(f"```{player} now has {players[player][1]}hp```")
					else:
						await bot.say(f"```{player} now has {players[player][1]}hp and {players[player][2]} temp hp```")
