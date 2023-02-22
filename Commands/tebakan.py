import discord, re, requests, random
from discord.ext import commands
from bs4 import BeautifulSoup
import numpy as np

# Get Tebakan
url = f"https://www.gramedia.com/best-seller/tebak-tebakan-lucu/"
alamat = requests.get(url).text
soup = BeautifulSoup(alamat, "html.parser")

container = soup.find("div", class_="entry-content g1-typography-xl")
tebakan = container.find_all("li")  # type:ignore
list_tebakan = np.array([],dtype='S')
TAG_RE = re.compile(r"<[^>]+>")
for key, value in enumerate(tebakan[4:-12]):
    list_tebakan = np.append(list_tebakan,TAG_RE.sub("", str(value)))
# End get tebakan


class tebak_tebakan(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("tebak-tebakan loaded!")

    @commands.command()
    async def tebak(self, ctx):
        pil = random.randint(0, 128)
        embed = discord.Embed(
            title=f"Tebak-tebakan by ngikngok😛", colour=discord.Colour.blue()
        )
        text = list_tebakan[pil].split("\n")
        embed.add_field(name=text[0], value=text[1], inline=False)
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(tebak_tebakan(client))
