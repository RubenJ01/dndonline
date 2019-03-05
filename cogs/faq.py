import discord
from discord.ext import commands


class faqcommand():
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def faq(self, number):
        embed = discord.Embed(
            colour=discord.Colour.blue()
        )
        if number == "1":
            embed.add_field(name="1. Where do I start? I’m new to D&D. - #faq",
                            value="If you would like a one-on-one tutorial, please post in #player-help. Many users will be reluctant to give you such a tutorial, but luckily, many YouTubers have devoted entire video series to this exact thing! We highly recommend the #resources channel, which you can search for keywords like “tutorial”.  In particular, the Lords recommend the How to Play D&D 5e series from Don’t Stop Thinking: https://www.youtube.com/watch?v=OoW2CDgztKY&list=PLJmFJXf3BXjwXkNFo_-iwtHb24AuJcXqx" + "\n" + "Once you have a firmer grasp of the basics, you will be able to ask for more specific help on the topics you don’t understand. That way, our Staff and users will be able to help you much better!",
                            inline=False)
            await bot.say(embed=embed)
        if number == "2":
            embed.add_field(name="2. Where do I find games? When is the next game? How often do we run games? - #faq",
                            value="You can find ads for games under #party-up.  You can also feel free to post your own Looking for Group, Looking for DM or Looking for Players (LFG, LFDM, LFP) ads to find people for your own game.  If you do, please follow the format outlined in the Pinned Messages for that channel." + "\n" + "Currently, the Tavern is in the process of recruiting more official DMs (the Queen's Guard), with the goal of establishing a regular weekly schedule of games.  When this is completed, the schedule will likely be posted in its own channel, and a link will be placed here. If you would like to interview for the Guard, PM a Captain of Queen's Guard to apply.",
                            inline=False)
            await bot.say(embed=embed)
        if number == "3":
            embed.add_field(name="3. Do we play/host games other than D&D? - #faq",
                            value="Yes!  All tabletop games are welcome, though the vast majority of our traffic is devoted to 5th Edition D&D.  Right now, we only have one channel, #other-rpgs-talk, as well as a channel for #trading-card-games and #video-gaming." + "\n" + "If you would like to start a channel dedicated to another system, please post in #server-suggestions so we can have users vote, react and gauge how much interest there is.  We are always open to adding new channels based on user demand!",
                            inline=False)
            await bot.say(embed=embed)
        if number == "4":
            embed.add_field(name="4. Why can I not post links/images? - #faq",
                            value="Because occasionally, somebody thinks it’s a good idea to post gay furry cuphead porn out of nowhere. Or tries to spread viruses to our users" + "\n" + "Due to malicious user activity, links and images have been heavily restricted in many parts of the server. If you want to post a relevant link, ask a member of Staff and we will be happy to assist you.",
                            inline=False)
            await bot.say(embed=embed)
        if number == "5":
            embed.add_field(name="5. Where do I find [thing]? What is [channel] for? - #faq",
                            value="For a list of all the channels and their purpose, go to #tavern-menu.", inline=False)
            from discord.ext.commands import bot
            await bot.say(embed=embed)
        if number == "6":
            embed.add_field(name="6. Can I run a game here? - #faq",
                            value="Yes! However, we ask that any DM who wants to run a game in the Tavern first apply for the Queen's Guard, our approved DMs who run games in the server.  If you would like to interview for the Guard, PM a Captain of Queen's Guard to apply." + "\n" + "However, you don’t need to join the Guard just to advertise a game. Feel free to post in #party-up whenever you like, as long as you follow the format in the Pinned Messages for that channel.",
                            inline=False)
            await bot.say(embed=embed)
        if number == "7":
            embed.add_field(name="7. What do the Staff do? - #faq",
                            value="Queen of the Tavern is the founder of the tavern." + "\n" + "Lords of the Tavern are Admins. In addition to the regular duties of an Innkeeper each Lord brings something unique to the tavern" + "\n" + "Innkeepers have shown they are capable Moderators and are trusted with more responsibilities; given the ability to create channels and roles, they can act more autonomously than Bartenders, and help implement or temper the Lords’ ideas." + "Bartenders are Moderators in the Tavern, and like any good Bartender, they are great with people. They settle disputes that get out of hand, but more generally, they interact with the patrons, providing a good face for the Tavern." + "\n" + "Advisors have no permissions or moderator abilities, they serve to help make decisions on moderation issues, and exist as a step prior to becoming a mod.",
                            inline=False)
            await bot.say(embed=embed)
        if number == "8":
            embed.add_field(name="8. How do I apply for Staff? - #faq",
                            value="Currently, new Staff applications are closed.  However, the Staff list does change occasionally. If you would like to signal your interest in being a staff member one day, feel free to fill out the application for the Advisors (trial moderator) role in #announcements." + "\n" + "Remember, we always keep an eye out for users who are regularly active, and who are generally kind, considerate and helpful to their fellow users. When you step up, we notice.",
                            inline=False)
            await bot.say(embed=embed)
        if number == "9":
            embed.add_field(name="9. What is the Hall of Fame? - #faq",
                            value="The Hall of Fame is reserved for users who have distinguished themselves in some way.  Users who are particularly funny, helpful, knowledgeable, clearheaded, etc. may one day find that the staff have voted to give them a golden hero’s crest.",
                            inline=False)
            await bot.say(embed=embed)
        if number == "10":
            embed.add_field(name="10. What does [abbreviation] mean? - #faq",
                            value="See the #faq for a full list of all abbrevations.", inline=False)
            await bot.say(embed=embed)


def setup(bot):
    bot.add_cog(faqcommand(bot))
