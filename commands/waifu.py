import discord
from discord.ext import commands

class Waifu(commands.Cog):
    def __init__(self, client):
        self.client=client

    @commands.group()
    async def waifu(self, ctx):
        return

    @waifu.command()
    @commands.cooldown(1,10, commands.BucketType.user)
    async def roll(self, ctx):
        await ctx.send("Roll")

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Wait {:.2f}s".format(error.retry_after))

def setup(client):
    client.add_cog(Waifu(client))