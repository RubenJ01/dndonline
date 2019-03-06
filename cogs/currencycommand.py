import discord
from discord.ext import commands
from dumpfiles.aliases import *


class currencycommand():
    def __init__(self, bot):
        self.bot = bot

    @commands.command(brief=currencybrief, description=currencydescription)
    async def currency(self, *coins):
        cp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "cp"])
        sp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "sp"])
        ep = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "ep"])
        gp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "gp"])
        pp = sum([int(coin[:-2]) for coin in coins if coin[-2:] == "pp"])
        total = (cp * 1) + (sp * 10) + (ep * 50) + (gp * 100) + (pp * 1000)
        cp = total % 10
        total = total // 10
        sp = total % 10
        total = total // 10
        gp = total % 10
        total = total // 10
        pp = total
        embed = discord.Embed(
            colour=discord.Colour.blue()
        )
        embed.add_field(name="Currency",
                        value="You have " + str(cp) + "cp " + str(sp) + "sp " + str(gp) + "gp " + str(pp) + "pp ",
                        inline=False)
        await self.bot.say(embed=embed)


def setup(bot):
    bot.add_cog(currencycommand(bot))
