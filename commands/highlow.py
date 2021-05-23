import random
import discord
from discord.utils import get
from discord.ext import commands


class HighLow(commands.Cog):
    rand = random.randint(1, 100)

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def highlow(self, ctx):
        embedVar = discord.Embed(title="HighLow", description=" ", color=0x00ff00)
        embedVar.add_field(name=self.rand, value="Higher or Lower?", inline=False)

        msg = await ctx.send(embed=embedVar)

        await msg.add_reaction("⬆")
        await msg.add_reaction("⬇")

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        newRand = random.randint(1, 100)
        outcome = 'You lose.'

        if user.bot:
            return
        if (reaction.emoji == "⬆" and newRand > self.rand) or (reaction.emoji == "⬇" and newRand < self.rand):
            outcome = 'You win!'
            self.rand = newRand
            await editEmbed(user, reaction, newRand, outcome)
        else:
            self.rand = newRand
            await editEmbed(user, reaction, newRand, outcome)

async def editEmbed(user, reaction, newRand, outcome):

    await reaction.remove(user)

    embed2 = discord.Embed(title="HighLow", description=" ", color=0x00ff00)
    embed2.add_field(name=newRand, value=outcome + "\nHigher or Lower?", inline=False)
    await reaction.message.edit(embed=embed2)


def setup(client):
    client.add_cog(HighLow(client))
