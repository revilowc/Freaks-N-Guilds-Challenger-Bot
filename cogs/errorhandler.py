import discord
from discord.ext import commands

class ErrorHandler(commands.Cog):
    """A cog for global error handling."""

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """A global error handler cog."""

        if isinstance(error, commands.CommandNotFound):
            return  # Return because we don't want to show an error for every command not found
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(embed=discord.Embed(description=f"**This command is on cooldown. Please try again after {round(error.retry_after, 1)} seconds.**", color=0x00f088), delete_after=5)

        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(embed=discord.Embed(description=f"**You are missing the required permissions to run this command!**", color=0x00f088), delete_after=5)

        elif isinstance(error, commands.UserInputError):
            await ctx.send(embed=discord.Embed(description=f"**Something about your input was wrong, please check your input and try again!**", color=0x00f088), delete_after=5)

        elif isinstance(error, commands.MissingRole):
            await ctx.send(embed=discord.Embed(description=f"**You are missing the required role to run this command!**", color=0x00f088), delete_after=5)

        elif isinstance(error, commands.MissingAnyRole):
            await ctx.send(embed=discord.Embed(description=f"**You are missing the required role to run this command!**", color=0x00f088), delete_after=5)

        else:
            await ctx.send(embed=discord.Embed(description=f"**Oh no! Something went wrong while running the command!**", color=0x00f088), delete_after=5)

        await ctx.message.delete(delay=5)

def setup(bot: commands.Bot):
    bot.add_cog(ErrorHandler(bot))