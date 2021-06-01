import discord
import random
from discord.ext import commands


class Quote(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def quote(self, ctx):
        file = open('quotes.txt', 'r')

        name = []
        q = []

        for line in file:
            spl = line.split('\"')
            name.append(spl[0])
            q.append(spl[1])

        file.close()

        rand = random.randint(0, len(name))

        embedVar = discord.Embed(title="\"" + q[rand] + "\"", description="-" + name[rand], color=0x00ff00)

        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(Quote(client))
