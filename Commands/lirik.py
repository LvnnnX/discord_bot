import discord
from discord.ext import commands
import re, requests
from bs4 import BeautifulSoup
import numpy as np


class lirik(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Lirik loaded!")

    @commands.command(help="n.lirik <nama lagu> & <nama band> (cari lirik lagu)")
    async def lirik(self, ctx, *args1):
        # await ctx.send("Masukkan nama lagu")
        # lagu = await self.client.wait_for(
        #     "message", timeout=60, check=lambda message: message.author == ctx.author
        # )
        # await ctx.send("Masukkan nama band")
        # band = await self.client.wait_for(
        #     "message", timeout=60, check=lambda message: message.author == ctx.author
        # )
        argument = " ".join(args1).split("&")
        findlirik = argument[0].strip()
        findband = argument[1].strip()
        print(findlirik, "dan", findband)
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
        lirik = np.array([], dtype="S")
        final = ""
        for t in soup.findAll("p"):
            lirik = np.append(lirik, t)
        TAG_RE = re.compile(r"<[^>]+>")
        for a, t in np.ndenumerate(lirik[:-1]):
            clean = TAG_RE.sub("", str(t))
            clean = re.sub("\n", "", str(clean))
            if clean != "":
                final = final + (clean + "\n")
        if final != "":
            await ctx.send(final)
        if len(lirik) == 0:
            await ctx.send(f'{findband}\'s song "{findlirik}" lyrics not found!')


async def setup(client):
    await client.add_cog(lirik(client))
