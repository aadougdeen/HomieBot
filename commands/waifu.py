import random
import discord
from discord.ext import commands
from main import collection


class Waifu(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.group(aliases=["w"])
    async def waifu(self, ctx):
        return

    @waifu.command(aliases=["r"])
    @commands.cooldown(1, 1, commands.BucketType.user)
    async def roll(self, ctx):
        # Generate random number
        global rand
        rand = random.randint(1, 8000)

        # Retrieve document from MongoDB
        global result
        result = collection.find_one({"_id": rand})

        # Send new embed message
        embed = discord.Embed(title=result["name"], description=" ", color=0x00ff00)
        embed.set_image(url=result["img"])
        msg = await ctx.send(embed=embed)
        await msg.add_reaction(":claim:849023397514313738")

    @waifu.command(aliases=["l"])
    async def list(self, ctx):
        user = ctx.message.author
        results = collection.find({"users": user.id})
        msg = "**Characters claimed by " + str(user) + "**\n"

        for x in results:
            msg += x["name"] + "\n"

        await ctx.send(msg)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            await ctx.send("Wait {:.2f}s".format(error.retry_after))

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        # If the reaction is from a bot, ignore the reaction
        if user.bot:
            return

        # If the user tries to claim the character
        if (reaction.emoji.id == 849023397514313738):
            # The user already claimed this character
            if (collection.find({"_id": result["_id"], "users": user.id}).count() > 0):
                await reaction.message.channel.send("You have already claimed this character.")
            else:
                collection.update_one({"_id": result["_id"]}, {"$push": {"users": user.id}})
                await reaction.message.channel.send("<a:claim:849023397514313738> Claimed <a:claim:849023397514313738>")


def setup(client):
    client.add_cog(Waifu(client))
