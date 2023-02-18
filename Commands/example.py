import discord
from discord.ext import commands


class Testing(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Ping loaded!")

    @commands.command(help='n.ping (check latency)')
    async def ping(self, ctx):
        await ctx.send("Pong! {0}ms".format(round(self.client.latency, 1)))


async def setup(client):
    await client.add_cog(Testing(client))
