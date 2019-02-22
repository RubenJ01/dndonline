"""As a note, this command does ***not*** understand that commands are in cogs.
This can be altered to paginate the command list for each cog that you may have.
However, this does not seem too important as of right now."""

from discord import Colour, Embed
from discord.ext.commands import command


class HelpCommand:

    def __init__(self, bot):
        self.bot = bot

    @command(name='help')
    async def help_group(self, command_name=None):
        """Sends a formatted embed in order to help users understand the commands of the bot.
        This command relies on command.brief and command.description in order to provide users
        with an adequate explanation of commands that are registered with the bot.

        :param command_name: The command that will be formatted."""
        try:
            _command = self.bot.get_command(command_name)
        except AttributeError:
            _command = None

        help_embed = Embed(colour=Colour.blue())
        if not command_name or not _command:
            # Command not found or none
            description = (f'**{bot_cmd.name}**: {bot_cmd.brief}' for bot_cmd in
                           self.bot.commands.values() if not bot_cmd.hidden)
            help_embed.description = '\n'.join(description)
            help_embed.set_footer(text='Use ;help {command_name}')
            return await self.bot.say(embed=help_embed)

        help_embed.title = f'**{_command.name}**'
        help_embed.description = _command.description
        # Adds the Aliases field if the command has aliases
        if _command.aliases:
            help_embed.add_field(name='Aliases', value=', '.join(_command.aliases))


def setup(bot):
    bot.add_cog(HelpCommand(bot))
