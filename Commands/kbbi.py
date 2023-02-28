import discord,re,requests
from discord.ext import commands
from bs4 import BeautifulSoup
import numpy as np

class kbbi(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print('kbbi loaded!')

    @commands.command(help='n.kbbi <kata> (pencarian kbbi)')
    async def kbbi(self, ctx, *args):
        argument = " ".join(args)
        url = f"https://kbbi.kemdikbud.go.id/entri/{argument}"
        alamat = requests.get(url).text
        soup = BeautifulSoup(alamat, "html.parser")
        judul = soup.find("div", class_="container body-content")
        main_text = judul.find_all("li")  # type: ignore
        if(len(main_text)==0):
            await ctx.send(f'{argument} tidak ditemukan!')
            return
          # type: ignore
        embed = discord.Embed(title=f"KBBI untuk {argument}", colour=discord.Colour.blue())
        TAG_RE = re.compile(r"<[^>]+>")
        texted = np.array([],dtype='S')
        for x in main_text[:-3]:
            texted = np.append(texted,TAG_RE.sub('',str(x)))
        texter = ''
        for x in texted:
            texter += x + '\n'
        embed.add_field(name=argument.capitalize(), value=texter, inline=False)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(kbbi(client))