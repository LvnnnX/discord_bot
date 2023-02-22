import discord, re, requests
from discord.ext import commands
from bs4 import BeautifulSoup
import numpy as np


class kalender(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("kalender loaded!")

    @commands.command()
    async def kalender(self, ctx, args):
        bulan = np.array(
            [
                "januari",
                "februari",
                "maret",
                "april",
                "mei",
                "juni",
                "juli",
                "agustus",
                "september",
                "oktober",
                "november",
                "desember",
            ]
        )
        if args not in bulan:
            await ctx.send(f"{args} bukan nama bulan yang valid!")
            return
        dpt = np.array(["januari", "februari", "maret", "april"])
        pil = "07" if args not in dpt else "06"
        url = (
            f"https://www.enkosa.com/2022/{pil}/kalender-bali-{args}-2023-lengkap.html"
        )
        alamat = requests.get(url).text
        soup = BeautifulSoup(alamat, "html.parser")

        judul = soup.find("div", class_="entry-content")
        hariraya = judul.find_all("h3")  # type: ignore
        listhr = judul.find_all("ul")  # type: ignore
        daftarjudul = np.array([],dtype='S')
        listraya = np.array([],dtype='S')

        TAG_RE = re.compile(r"<[^>]+>")
        for a, b in zip(hariraya[:-1], listhr[:-1]):
            cleana = TAG_RE.sub("\n", str(a))
            cleanb = TAG_RE.sub("\n", str(b))
            cleana = cleana.replace("\n\n", "\n")
            cleanb = cleanb.replace("\n\n", "\n")
            daftarjudul = np.append(daftarjudul,cleana)
            listraya = np.append(listraya,cleanb)

        embed = discord.Embed(
            title=f"Kalender Bali bulan {args.capitalize()}",
            colour=discord.Colour.blue(),
        )
        embed.set_author(
            name="by Agatha & Ngikngok",
            icon_url="https://cdn.discordapp.com/attachments/952898818767196202/1014169174320369704/Screenshot_2022-08-07_132626.png",
        )
        for a, x in enumerate(daftarjudul):
            embed.add_field(name=x, value=listraya[a], inline=False)
        embed.set_footer(text='powered by enkosa.com')
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(kalender(client))
