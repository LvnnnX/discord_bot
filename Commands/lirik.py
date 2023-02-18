import discord
from discord.ext import commands
import re,requests
from bs4 import BeautifulSoup

class lirik(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print('Lirik loaded!')

    @commands.command(help='n.lirik (pencarian lirik lagu)')
    async def lirik(self, ctx):
        await ctx.send("Masukkan nama lagu")
        lagu = await self.client.wait_for(
            "message", timeout=60, check=lambda message: message.author == ctx.author
        )
        await ctx.send("Masukkan nama band")
        band = await self.client.wait_for(
            "message", timeout=60, check=lambda message: message.author == ctx.author
        )
        findlirik = lagu.content
        findband = band.content
        url = (
            "https://lirik.web.id/"
            + findband[0]
            + "/"
            + "".join(re.sub(" ", "-", findband))
            + "/lirik-lagu-"
            + "".join(re.sub(" ", "-", findband))
            + "-"
            + "".join(re.sub(" ", "-", findlirik))
            + "/"
        )
        alamat = requests.get(url).text
        soup = BeautifulSoup(alamat, "html.parser")
        lirik = []
        final = ""
        for t in soup.findAll("p"):
            lirik.append(t)
        TAG_RE = re.compile(r"<[^>]+>")
        for t in lirik[:-1]:
            clean = TAG_RE.sub("", str(t))
            final = final + (clean + "\n")
        if final != "":
            await ctx.send(final)
        if len(lirik) == 0:
            await ctx.send(f'{findband}\'s song "{findlirik}" lyrics not found!')

async def setup(client):
    await client.add_cog(lirik(client))