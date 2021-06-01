import random
import discord
from discord.ext import commands


class HighLow(commands.Cog):
    # Generate random number
    rand = random.randint(1, 100)

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def highlow(self, ctx):

        # Create and send embed containing the Higher or Lower game
        embedVar = discord.Embed(title="HighLow", description=" ", color=0x00ff00)
        embedVar.add_field(name=self.rand, value="Higher or Lower?", inline=False)
        msg = await ctx.send(embed=embedVar)

        # Add reactions to the embed that will be used to play the game
        await msg.add_reaction(":higher:848999214855356505")
        await msg.add_reaction(":lower:848999285542092870")

    # Listen for a reaction to be added
    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # Generate new random number to be used in higher/lower comparison
        newRand = random.randint(1, 100)

        # Default outcome
        outcome = 'You lose.'

        # If the reaction is from a bot, ignore the reaction
        if user.bot:
            return
        # Correct guess
        if (reaction.emoji.id == 848999214855356505 and newRand > self.rand) or (
                reaction.emoji.id == 848999285542092870 and newRand < self.rand):
            outcome = 'You win!'
            self.rand = newRand
            await editEmbed(user, reaction, newRand, outcome)

        # Incorrect guess
        elif (reaction.emoji.id == 848999214855356505 or reaction.emoji.id == 848999285542092870):
            self.rand = newRand
            await editEmbed(user, reaction, newRand, outcome)


# Edit message to the new embed
async def editEmbed(user, reaction, newRand, outcome):
    # Remove the user's reaction to the message
    await reaction.remove(user)

    # Send new embed message
    embed2 = discord.Embed(title="HighLow", description=" ", color=0x00ff00)
    embed2.add_field(name=newRand, value=outcome + "\nHigher or Lower?", inline=False)
    await reaction.message.edit(embed=embed2)


def setup(client):
    client.add_cog(HighLow(client))
