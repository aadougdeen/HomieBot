import discord
from discord.ext import commands


class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["i"])
    async def info(self, ctx):
        embedVar = discord.Embed(title="Information", description="Discord bot for Aaron's Ancestry Account",
                                 color=0x00ff00)
        embedVar.add_field(name='Commands', value="**!info**  - description of bot and list of commands\n\n"
                                                  + "**!quote** - random dumb quote\n\n"
                                                  + "**!highlow** - higher or lower game for currency\n\n"
                                                    "**!waifu roll** - roll waifu\n\n"
                                                    "**!waifu list** -  lists your claimed characters", inline=False)
        embedVar.set_footer(text='Created by SacLamb',
                            icon_url='https://cdn.discordapp.com/avatars/154690746107035648/a_985713092df32da3a7af0fd605e83e6d.gif?size=128')
        await ctx.send(embed=embedVar)


def setup(client):
    client.add_cog(Info(client))
