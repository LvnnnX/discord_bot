import discord, re, requests, random
from discord.ext import commands
from bs4 import BeautifulSoup
import numpy as np

TAG_RE = re.compile(r"<[^>]+>")
# URL FOR GOMBALAN
gombal_url = f"https://www.fimela.com/relationship/read/5076974/50-kata-kata-chat-gebetan-yang-seru-dan-bikin-pdkt-lancar"
gombal_alamat = requests.get(gombal_url).text
gombal_soup = BeautifulSoup(gombal_alamat, "html.parser")
judul = gombal_soup.find(
    "div",
    class_="read-page--article-triumvirate js-article-triumvirate read-page--article-triumvirate_with-ads",
)
# Head_2 itu untuk nyimpen judul2nya
head_2 = judul.find_all("h2")  # type: ignore
# Cleaning head_2
head_clean = np.array([], dtype="S")
for key, value in enumerate(head_2):
    head_clean = np.append(head_clean, TAG_RE.sub("", str(value)))
    # Sekarang cari isi artikelnya
content = judul.find("div", class_="article-content-body__item-content")  # type: ignore
kalimat = np.array([], dtype="S")
gombal_clean = np.array([], dtype="S")
# isi = content.find_all('p')
while True:
    try:
        content = content.find_next(class_="article-content-body__item-content")  # type: ignore
        isi = content.find_all("p")  # type: ignore
        kalimat = np.append(kalimat, isi)
    except:
        break

for key, value in enumerate(kalimat):
    value = TAG_RE.sub("", str(value))
    value = re.findall(r"\".*?\"", value)
    for x in value:
        gombal_clean = np.append(gombal_clean, x)
# END GOMBALAN


# RANDOM QUOTES
all_quotes = np.array([], dtype="S")
# URL 1
url_1 = f"https://www.brilio.net/wow/40-kata-kata-keren-quotes-cocok-dijadikan-caption-medsosmu-191127s.html"
alamat_1 = requests.get(url_1).text
soup_1 = BeautifulSoup(alamat_1, "html.parser")
body_1 = soup_1.find("div", class_="main-content")
content_1 = body_1.find_all("p")  # type: ignore
for key, value in enumerate(content_1):
    value = TAG_RE.sub("", str(value))
    value = re.findall(r"\".*?\"", str(value))
    for x in value:
        all_quotes = np.append(all_quotes, x)
# URL 2
url_2 = f"https://www.brilio.net/wow/40-kata-kata-keren-quotes-cocok-dijadikan-caption-medsosmu-191127s/kata-kata-keren-quotes-cinta-2212055.html"
alamat_2 = requests.get(url_2).text
soup_2 = BeautifulSoup(alamat_2, "html.parser")
body_2 = soup_2.find("div", class_="main-content")
content_2 = body_2.find_all("p")  # type: ignore
for key, value in enumerate(content_2):
    value = TAG_RE.sub("", str(value))
    value = re.findall(r"\".*?\"", str(value))
    for x in value:
        all_quotes = np.append(all_quotes, x)
# END RANDOM QUOTES #

# MOTIVATION QUOTES NGIKNGOK
motivation_quotes = np.array([], dtype="S")
next_quotes = []
url_3 = f"https://www.cermati.com/artikel/kata-kata-motivasi-hidup-terbaik-untuk-buat-hidup-kamu-lebih-semangat"
alamat_3 = requests.get(url_3).text
soup_3 = BeautifulSoup(alamat_3, "html.parser")
body_3 = soup_3.find("ol", class_="ordered-section")
content_3 = body_3.find_all("p")  # type: ignore
for key, value in enumerate(content_3):
    value = TAG_RE.sub("", str(value))
    value = re.sub("\xa0", "", str(value))
    value = re.sub("\n\n\n\n\n", "", str(value))
    if value == "":
        continue
    next_quotes.append(value)
next_quotes.pop(0)
for key, value in enumerate(next_quotes):
    if not value.__contains__("Tip:"):
        motivation_quotes = np.append(motivation_quotes, value)
# END MOTIVATION QUOTES NGIKNGOK #


class quotes(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("quote loaded!")

    @commands.group(help="n.quotes <gombal|random|motivation>")
    async def quotes(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send(
                f"Coba tambahkan beberapa command! di {ctx.invoked_subcommand}"
            )

    # GOMBALAN DARI NGIKNGOK
    @quotes.command()
    async def gombal(self, ctx):
        pil = random.randint(0, 49)
        embed = discord.Embed(
            title=f"Gombalan dari ngikngok 💗", colour=discord.Colour.blue()
        )
        embed.add_field(name="\u200b", value=gombal_clean[pil], inline=False)
        await ctx.send(embed=embed)

    # END GOMBALAN NGIKNGOK #

    # RANDOM QUOTES NGIKNGOK
    @quotes.command()
    async def random(self, ctx):
        pil = random.randint(0, 153)
        embed = discord.Embed(
            title=f"Quotes random dari ngikngok😎🆒", colour=discord.Colour.blue()
        )
        embed.add_field(name="\u200b", value=all_quotes[pil], inline=False)
        await ctx.send(embed=embed)

    # END RANDOM QUOTES NGIKNGOK

    # MOTIVATION QUOTES NGIKNGOK
    @quotes.command()
    async def motivation(self, ctx):
        pil = random.randint(0, 143)
        embed = discord.Embed(
            title=f"Quotes motivasi dari ngikngok💪", colour=discord.Colour.blue()
        )
        embed.add_field(name="\u200b", value=all_quotes[pil], inline=False)
        await ctx.send(embed=embed)

    # END MOTIVATION QUOTES NGIKNGOK #


async def setup(client):
    await client.add_cog(quotes(client))
