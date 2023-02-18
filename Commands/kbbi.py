import discord,re,requests
from discord.ext import commands
from bs4 import BeautifulSoup

class kbbi(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print('kbbi loaded!')

    @commands.command(help='n.kbbi <kata> (pencarian kbbi)')
    async def kbbi(self, ctx, *args):
        argument = " ".join(args)
        url = f"https://kbbi.web.id/{argument}"
        alamat = requests.get(url).text
        soup = BeautifulSoup(alamat, "html.parser")
        judul = soup.find("div", class_="content")
        main_text = judul.find_all("b")  # type: ignore
        if(len(main_text)==0):
            await ctx.send(f'{argument} tidak ditemukan!')
            return
        texter = judul.find("div", {"id": "d1"}).get_text()  # type: ignore
        TAG_RE = re.compile(r"<[^>]+>|\n|[0-9]|-+|;|·+|:+$")
        texted = []
        s = ""
        for x in texter:
            if x != " ":
                s += x
            else:
                texted.append(s)
                s = ""
        for a, b in enumerate(main_text):
            main_text[a] = TAG_RE.sub("", str(b))
        for a, b in enumerate(texted):
            texted[a] = TAG_RE.sub("", str(b))
        embed = discord.Embed(title=f"KBBI untuk {argument}", colour=discord.Colour.blue())

        while "" in texted:
            texted.remove("")
        while "" in main_text:
            main_text.remove("")
        strings = ""
        for x in texted:
            if len(x) == 1:
                texted.remove(x)
            else:
                if len(strings) + len(x) + 1 < 1024:
                    strings = strings + " " + x
                else:
                    break
        main_text.pop(0)
        embed.add_field(name=argument.capitalize(), value=strings, inline=False)
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(kbbi(client))