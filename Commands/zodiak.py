import discord
from discord.ext import commands
import re, requests
from bs4 import BeautifulSoup
import numpy as np

class zodiak(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("zodiak loaded!")

    @commands.command(help="n.zodiak <nama zodiak> untuk cari info zodiak!")
    async def zodiak(self, ctx, args):
        zist_zodiak = np.array([
            "aquarius",
            "pisces",
            "aries",
            "taurus",
            "gemini",
            "cancer",
            "leo",
            "virgo",
            "libra",
            "sagitarius",
            "capricorn",
        ])
        embed = discord.Embed(
            title=f"Pencarian untuk zodiak {args.capitalize()} ",
            colour=discord.Colour.blue(),
        )
        if args.lower() not in zist_zodiak:
            # type: ignore
            embed.add_field(name=f"{args.capitalize()} bukan zodiak!")  # type: ignore
            await ctx.send(embed=embed)
        else:
            url = "https://www.fimela.com/zodiak/" + args.lower()
            alamat = requests.get(url).text
            soup = BeautifulSoup(alamat, "html.parser")
            artikel = soup.find("div", class_="container-article")
            judul = artikel.find_all("h5")  # type: ignore
            list_judul = np.array([],dtype='S')
            list_desc = np.array([],dtype='S')
            TAG_RE = re.compile(r"<[^>]+>")
            for t in judul:
                t = TAG_RE.sub("", str(t))
                t = t.capitalize()
                list_judul = np.append(list_judul,t)
            desc = artikel.find_all("div", class_="zodiak--content__item")  # type: ignore
            for x in desc[:-2]:
                x = TAG_RE.sub("", str(x))
                list_desc = np.append(list_desc,x)
            for l in range(len(list_desc)):
                embed.add_field(
                    name=f"{list_judul[l+1]}",
                    value=f"{list_desc[l][len(list_judul[l+1]):]}",
                    inline=False,
                )
            embed.set_author(
                name="by Agatha & Ngikngok",
                icon_url="https://cdn.discordapp.com/attachments/952898818767196202/1076789878404161556/320890519_721815005774688_2433660246175642108_n.jpg",
            )
            await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(zodiak(client))
