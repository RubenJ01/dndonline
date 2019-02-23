@bot.command(brief="starts the initiative tracker, (format like ;intiative name initmod)")
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
    await bot.say(embed=embed)

@bot.command(brief="move on to the next turn in the initiative tracker")
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
    await bot.say(embed=embed)


@bot.command(brief="stop the initiative tracker")
async def stop():
    global initiative_roles
    initiative_roles = []
    embed = discord.Embed(
    	colour = discord.Colour.blue()
    )
    embed.add_field(name=";stop", value="Initiative cleared", inline=False)
    await bot.say(embed=embed)

@bot.command(brief="displays the order of the rolled initiatives")
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
    await bot.say(embed=embed)

@bot.command(brief="move 1 turn back in the initiative tracker")
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
    await bot.say(embed=embed)

