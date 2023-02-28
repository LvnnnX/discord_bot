import discord
import random
import yfinance as yf
from datetime import datetime
import plotly.graph_objs as go
from discord.ext import commands, tasks
from dotenv import load_dotenv
from bs4 import BeautifulSoup
import requests
import re
from itertools import cycle
import json
import requests
import tweepy
from requests_oauthlib import OAuth1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


load_dotenv()


with open("E:\\Folder_apps\\NGODING\\Discord_bot\\token.json") as f:
    tokens = json.load(f)
    bearer_token = tokens["bearer_token"]
    api_key = tokens["api_key"]
    api_key_secret = tokens["api_key_secret"]
    access_token = tokens["access_token"]
    access_token_secret = tokens["access_token_secret"]

auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
client = tweepy.Client(
    bearer_token, api_key, api_key_secret, access_token, access_token_secret
)
auth1 = tweepy.OAuth1UserHandler(
    api_key, api_key_secret, access_token, access_token_secret
)
api_1 = tweepy.API(auth1)
api_2 = tweepy.Client(bearer_token=bearer_token, wait_on_rate_limit=True)

intents = discord.Intents.all()
intents.message_content = True
token = "OTc4NDY4OTQyMjg2ODQ4MDUx.Gp3gub.80-KGP2Y_ESM7hF6cWNgenJyLZ-nd91wF5mBcA"
bot = discord.Client(intents=intents)
client = commands.Bot(command_prefix="n.", intents=intents)


@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    # Ruang turu 978448938430509067
    # Test serv 952848717952741386
    hai = ["hello", "hai", "hi", "halo", "ngikngok"]
    sedih = ["sedih", "sad", "mengsad", "mengsedih"]
    print(f"{username}: {user_message} ({channel})")

    if message.author == client.user:  # type: ignore
        pass

    if user_message.lower() == "ping":
        # type: ignore
        await message.channel.send("pong! {0}ms".format(round(client.latency, 1)))
        return

    if user_message.lower() == "regen21":
        pic = [
            "regen_1.jpg",
            "regen_2.jpg",
            "regen_3.jpg",
            "regen_4.jpg",
            "regen_5.jpg",
            "regen_6.jpg",
            "regen_7.jpg",
            "regen_8.jpg",
            "regen_9.jpg",
            "regen_10.jpg",
            "regen_11.jpg",
            "regen_12.jpg",
            "deva_alerta.jpg",
        ]
        cap = [
            "Raja Pala!",
            "Ciluk baa",
            "Turu deck",
            "Alerta",
            "Boboiboy",
            "Kero keroo",
            "Geknan",
            "Yume Naraba Dore Hodo Yokatta Deshou",
            "Indahnya Pemandangan, Banyaknya tiiit",
            "Hai Kevin, Aku Gay",
            "Makan Bwang",
            "Super Saiyaa",
            "Alerta v2",
        ]
        pil = random.randint(0, len(pic) - 1)
        await message.channel.send(f"Selamat! {username} mendapatkan kartu")
        if pil == 0:
            await message.channel.send(f"Rare CARD!")
        await message.channel.send(cap[pil], file=discord.File(f"{pic[pil]}"))
        return

    if user_message.lower() in hai:
        choice = ["hello_donkey.jpg", "hello_donkey2.jpg", "hello_ngikngok.jpg"]
        await message.channel.send(f"Hai bang {username}")
        await message.channel.send(
            file=discord.File(f"{choice[random.randint(0,len(choice)-1)]}")
        )
        return

    if user_message.lower() in sedih:
        rand = random.randint(0, 1)
        if rand == 1:
            await message.channel.send("Janji gak nangis?")
        choice = [
            "sedih.jpeg",
            "sad_donkey1.gif",
            "sad_donkey2.gif",
            "sad_donkey3.jpg",
            "sad_donkey4.jpg",
        ]
        pil = random.randint(0, len(choice) - 1)
        await message.channel.send(file=discord.File(f"{choice[pil]}"))
        return

    if user_message.lower() == "kamu siapa?":
        choice = ["hello_ngikngok.jpg", "ngikngok.png", "sad_donkey4.jpg"]
        await message.channel.send("Akulah ngikngok!")
        await message.channel.send(
            file=discord.File(f"{choice[random.randint(0,len(choice)-1)]}")
        )
        return

    if user_message == "<@978468942286848051>":
        choice = ["hello_ngikngok.jpg", "ngikngok.png", "sad_donkey4.jpg"]
        await message.channel.send("Iya ngikngok?")
        await message.channel.send(
            file=discord.File(f"{choice[random.randint(0,len(choice)-1)]}")
        )
        await message.channel.send(
            """Menu ngikngok
        >> Hello (hi,halo,hai)
        >> Sedih (sad,mengsedih,mengsad)
        >> Kamu Siapa?
        >> @Ngikngok
        >> Ping (response time)
        >> Selengkapnya di n.help"""
        )
        return
    await client.process_commands(message)  # type: ignore


# @client.command(help="Harga coin LUNA terkini")
# async def info(ctx):
#     kurs = 14650
#     data = yf.download(tickers="LUNA1-USD", period="1d", interval="15m")
#     data.reset_index(inplace=True)
#     tot = data["Datetime"].count() - 20
#     datafix = data[tot::]
#     stock = yf.Ticker("LUNA1-USD")
#     price = stock.info["regularMarketPrice"]
#     price = price * kurs
#     fig = go.Figure()
#     fig.add_trace(
#         go.Candlestick(
#             x=datafix["Datetime"],
#             open=datafix["Open"] * kurs,
#             high=datafix["High"] * kurs,
#             low=datafix["Low"] * kurs,
#             close=datafix["Close"] * kurs,
#             name="market data",
#         )
#     )
#     fig.update_layout(
#         title="Luna live share price (UST time)", yaxis_title="Harga (Rp)"
#     )
#     fig.update_xaxes(
#         rangeslider_visible=True,
#         rangeselector=dict(
#             buttons=list(
#                 [
#                     dict(count=15, label="15m", step="minute", stepmode="backward"),
#                     dict(count=45, label="45m", step="minute", stepmode="backward"),
#                     dict(count=1, label="HTD", step="hour", stepmode="todate"),
#                     dict(count=3, label="3h", step="hour", stepmode="backward"),
#                     dict(step="all"),
#                 ]
#             )
#         ),
#     )
#     fig.write_image(f"dia.png")
#     await ctx.send(
#         f'Harga Luna sekarang {datetime.now.strftime("%D  %H:%M")}\n Rp.{price}'
#     )
#     await ctx.send(file=discord.File(f"dia.png"))
#     return


@client.command()
async def jadwal(ctx):
    # Data jadwal
    df = pd.read_excel(
        "E:\\Folder_apps\\NGODING\\Discord_bot\\Jadual Ganjil 2022-2023.xlsx",
        sheet_name="REGULER",
    )
    df.rename(
        columns={
            "Jadual Kuliah Mata Kuliah Reguler Program Studi Informatika": "Jadual",
            "Unnamed: 1": "KODE",
            "Unnamed: 2": "MATA KULIAH",
            "Unnamed: 3": "SKS",
            "Unnamed: 11": "JADWAL B",
            "Unnamed: 10": "JADWAL A",
            "Unnamed: 12": "JADWAL C",
            "Unnamed: 13": "JADWAL D",
            "Unnamed: 14": "JADWAL E",
            "Unnamed: 4": "Dosen A",
            "Unnamed: 5": "Dosen B",
            "Unnamed: 6": "Dosen C",
            "Unnamed: 7": "Dosen D",
            "Unnamed: 8": "Dosen E",
        },
        inplace=True,
    )
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    dropindex = [int(x) for x in range(0, 12)] + [int(x) for x in range(19, len(df))]
    df.drop(index=dropindex, inplace=True)
    df.drop(columns=["Jadual", "KODE", "SKS"], inplace=True)
    # Data jadwal fix

    # Data dosen
    datadosen = pd.read_excel(
        "E:\\Folder_apps\\NGODING\\Discord_bot\\Jadual Ganjil 2022-2023.xlsx",
        sheet_name="DOSEN IF",
    )
    datadosen.columns = datadosen.loc[2]
    datadosen = datadosen[3:28]
    datadosen.reset_index(drop=True, inplace=True)
    # Data dosen tersorting
    embed = discord.Embed(
        title="Jadwal Pelajaran IF'2021", colour=discord.Colour.blue()
    )

    # Memisahkan jadwal2
    kelas = ["A", "B", "C", "D", "E"]
    for x in kelas:
        for a, b in enumerate(df[f"Dosen {x}"]):
            # memisahkan jadwal
            df.loc[a, f"JADWAL {x}"] = re.sub(
                "/", "|", df.loc[a, f"JADWAL {x}"]  # type: ignore
            )  # type: ignore
            # print(b)
            # Mengganti kode dengan nama dosen
            for c, d in enumerate(datadosen["KODE"]):
                # print(d,b)
                if d == b:  # kode ketemu yang sama
                    # print('found')
                    # type: ignore #ganti ke nama
                    df.loc[a, f"Dosen {x}"] = datadosen.loc[c, "NAMA"]  # type: ignore

    # Priorities untuk sorting
    priorities = ["minggu", "sabtu", "jumat", "kamis", "rabu", "selasa", "senin"]

    # Add field to discord embed
    for new in kelas:
        for x in range(1, len(df)):
            key = df[f"JADWAL {new}"].iloc[x].split()[0]
            check = x - 1
            while check >= 0 and priorities.index(key.lower()) > priorities.index(
                df[f"JADWAL {new}"].iloc[check].split()[0].lower()
            ):
                b, c = df.iloc[check + 1].copy(), df.iloc[check].copy()
                df.iloc[check + 1], df.iloc[check] = c, b
                check -= 1
        texter = ""
        date = ""
        for x, y, z in zip(df["MATA KULIAH"], df[f"Dosen {new}"], df[f"JADWAL {new}"]):
            texter = texter + x + "\n" + y.split(",")[0] + "\n" + "." * 50 + "\n"
            date = date + z + "\n.\n.\n"
        embed.add_field(name=f"KELAS {new}", value=texter, inline=True)
        # embed.add_field(name=f'KELAS {new}',value=df['MATA KULIAH'].to_string(index=False),inline=True)
        embed.add_field(name="JAM PELAJARAN", value=date, inline=True)
        # embed.add_field(name='JAM PELAJARAN',value=df[f'JADWAL {new}'].to_string(index=False),inline=True)
        embed.add_field(name="\u200b", value="\u200b")

    embed.set_author(
        name="by Agatha & Ngikngok",
        icon_url="https://cdn.discordapp.com/attachments/952898818767196202/1014169174320369704/Screenshot_2022-08-07_132626.png",
    )
    await ctx.send(embed=embed)
    return


@client.command(help="Mencari lirik lagu")
async def lirik(ctx):
    await ctx.send("Masukkan nama lagu")
    lagu = await client.wait_for(
        "message", timeout=60, check=lambda message: message.author == ctx.author
    )
    await ctx.send("Masukkan nama band")
    band = await client.wait_for(
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
    return


@client.command()
async def zodiak(ctx, args):
    list_zodiak = [
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
    ]
    embed = discord.Embed(
        title=f"Pencarian untuk zodiak {args.capitalize()} ",
        colour=discord.Colour.blue(),
    )
    if args.lower() not in list_zodiak:
        # type: ignore
        embed.add_field(name=f"{args.capitalize()} bukan zodiak!")  # type: ignore
        await ctx.send(embed=embed)
    else:
        url = "https://www.fimela.com/zodiak/" + args.lower()
        alamat = requests.get(url).text
        soup = BeautifulSoup(alamat, "html.parser")
        artikel = soup.find("div", class_="article")
        judul = artikel.findAll("h5")  # type: ignore
        list_judul = []
        list_desc = []
        for t in judul:
            TAG_RE = re.compile(r"<[^>]+>")
            t = TAG_RE.sub("", str(t))
            t = t.capitalize()
            list_judul.append(t)
        desc = artikel.findAll("p", class_="zodiak--content__item-text")  # type: ignore
        for x in desc:
            TAG_RE = re.compile(r"<[^>]+>")
            x = TAG_RE.sub("", str(x))
            list_desc.append(x)
        for l in range(len(list_desc)):
            embed.add_field(
                name=f"{list_judul[l+1]}", value=f"{list_desc[l]}", inline=False
            )
        embed.set_author(
            name="by Agatha & Ngikngok",
            icon_url="https://cdn.discordapp.com/attachments/952898818767196202/1014169174320369704/Screenshot_2022-08-07_132626.png",
        )
        await ctx.send(embed=embed)
        return


@client.command()
async def kbbi(ctx, *args):
    argument = " ".join(args)
    url = f"https://kbbi.web.id/{argument}"
    alamat = requests.get(url).text
    soup = BeautifulSoup(alamat, "html.parser")
    judul = soup.find("div", class_="content")
    main_text = judul.find_all("b")  # type: ignore
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
    return


@client.command(
    help="Pencocokan jodoh, n.jodoh (tanggal lahirmu) (tanggal lahir pasangan)"
)
async def jodoh(ctx, args1, args2):
    sum_tanggal = int(args1) + int(args2)
    embed = discord.Embed(
        title=f"Hasil kalkulasi perjodohan", colour=discord.Colour.blue()
    )
    hasil_2 = "Anda dan dia dapat membangun hubungan yang harmonis apabila kedua belah pihak bisa bekerjasama dengan baik serta bijaksana dalam menghadapi cobaan cinta yang datang silih berganti.\nKeberhasilan hubungan kalian sangat bergantung pada kehati-hatian anda dalam menjaga perasaan pasangan dari hal-hal yang mungkin dapat menyakiti hatinya.\nAnda dan dia dapat membangun hubungan yang harmonis apabila kedua belah pihak bisa bekerjasama dengan baik serta bijaksana dalam menghadapi cobaan cinta yang datang silih berganti.\nKeberhasilan hubungan kalian sangat bergantung pada kehati-hatian anda dalam menjaga perasaan pasangan dari hal-hal yang mungkin dapat menyakiti hatinya."
    hasil_3 = "Lingkungan sosial yang menunjukkan adanya banyak lawan jenis di salah satu pasangan, misalnya lingkungan anda atau si dia bisa memicu kecemburuan ringan.\nKeterbukaan antara kedua belah pihak pasangan sangat diperlukan untuk memperkuat rasa saling percaya.\nJangan membiasakan diri menyepelekan persoalan kecil karena sekecil apa pun sebuah persoalan tetap berpotensi untuk membuat hubungan berada dalam masalah yang lebih besar.\nKomunikasi adalah kunci sukses yang paling berperan penting dalam memberikan kontribusi keberlangsungan hubungan tetap berjalan dengan baik."
    hasil_4 = "Perbedaan pendapat dengan pasangan adalah hal yang wajar terjadi sehingga tidak perlu diperpanjang lagi karena hal itu justru akan berpotensi membuat masalah menjadi semakin rumit.\nJangan berpikiran bahwa pasangan selalu menuntut sesuatu yang lebih karena sebenarnya ia hanya sedang berusaha membuat anda mau bertindak atau melakukan sesuatu dengan lebih serius.\nDibalik semua tingkah serta sikapnya yang benar-benar membuat anda kesal, yakinlah bahwa sebenarnya ia adalah sosok pasangan yang sangat perhatian dan selalu menyayangi anda dengan sepenuh hatinya."
    hasil_5 = "Jika si dia memang bisa selalu membuat anda merasa bahagia dan nyaman menjalani hubungan, maka bukan hal yang tidak mungkin bahwa ia adalah jodoh yang diturunkan oleh Sang Pencipta untuk menemani hidup anda.\nNamun, jika pasangan anda saat ini justru kerap membuat hati anda merasa sedih dan gelisah, maka mungkin saja ia hanyalah bagian dari sepenggal kisah hidup yang harus anda lewati sedari menunggu hingga jodoh yang sesungguhnya datang kepada anda."
    hasil_6 = "Pasang surut hubungan anda merupakan bagian dari proses pendewasaan cinta. Jalani saja semua seperti air yang mengalir. Tidak perlu menengok masa lalu, hidup anda adalah tentang hari ini dan hari esok. \nJangan mudah terpengaruh oleh orang lain karena hubungan anda sepenuhnya milik anda.\n Hubungan anda bersama si dia bisa menjadi lebih baik apabila satu sama lain tidak segan untuk mau lebih terbuka.\n Maka dari itu, mulai saat ini hindarilah kebiasaan menutup-nutupi sesuatu dari pasangan."
    if sum_tanggal >= 2 and sum_tanggal <= 14:
        embed.add_field(name="\u200b", value=str(hasil_2), inline=False)
    elif sum_tanggal >= 15 and sum_tanggal <= 29:
        embed.add_field(name="\u200b", value=str(hasil_3), inline=False)
    elif sum_tanggal >= 30 and sum_tanggal <= 41:
        embed.add_field(name="\u200b", value=str(hasil_4), inline=False)
    elif sum_tanggal >= 42 and sum_tanggal <= 53:
        embed.add_field(name="\u200b", value=str(hasil_5), inline=False)
    else:
        embed.add_field(name="\u200b", value=str(hasil_6), inline=False)
    await ctx.send(embed=embed)
    return


@client.command(help="Test aja..")
async def test(ctx, *args):
    await ctx.send("{}".format(*args))
    return


def getname(id):
    response = api_2.get_tweet(
        id=id, expansions=["author_id"], user_fields=["username"]
    )
    return response.includes["users"][0].username  # type: ignore


def getid(id):
    user = api_2.get_user(username=id)
    return user[0].id  # type: ignore


@client.command(help="Mencari timeline twitter seseorang :o n.twttimeline <@user>")
async def twttimeline(ctx, *, args):
    final = ""
    sea = api_1.user_timeline(user_id=getid(args))
    embed = discord.Embed(
        title=f"Getting {args}'s twitter timeline!", colour=discord.Colour.blue()
    )
    if len(sea) == 0:
        embed.add_field(name="Nothing Found!", value="\u200b")
    else:
        await ctx.send(f"Getting {args}'s twitter timeline!")
        for t in sea[: len(sea) if len(sea) <= 5 else 5]:
            date = t.created_at.strftime("%Y-%m-%d at %H:%M")
            if (
                len(final)
                + len(date + "\n" + t.text + "\n=============end===========\n")
                < 2000
            ):
                final = final + (
                    date + "\n" + t.text + "\n=============end===========\n"
                )
            else:
                embed.add_field(name="\u200b", value=final, inline=False)
                final = "" + (date + "\n" + t.text + "\n=============end===========\n")
        if len(final) != 0:
            embed.add_field(name="\u200b", value=final, inline=False)
    await ctx.send(embed=embed)
    return


@client.command()
async def kalender(ctx, args):
    bulan = [
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
    if args not in bulan:
        await ctx.send(f"{args} bukan nama bulan yang valid!")
        return
    dpt = ["januari", "februari", "maret", "april"]
    pil = "07" if args not in dpt else "06"
    url = f"https://www.enkosa.com/2022/{pil}/kalender-bali-{args}-2023-lengkap.html"
    alamat = requests.get(url).text
    soup = BeautifulSoup(alamat, "html.parser")

    judul = soup.find("div", class_="entry-content")
    hariraya = judul.find_all("h3")  # type: ignore
    listhr = judul.find_all("ul")  # type: ignore
    daftarjudul = []
    listraya = []

    TAG_RE = re.compile(r"<[^>]+>")
    for a, b in zip(hariraya[:-1], listhr[:-1]):
        cleana = TAG_RE.sub("\n", str(a))
        cleanb = TAG_RE.sub("\n", str(b))
        cleana = cleana.replace("\n\n", "\n")
        cleanb = cleanb.replace("\n\n", "\n")
        daftarjudul.append(cleana)
        listraya.append(cleanb)

    embed = discord.Embed(
        title=f"Kalender Bali bulan {args.capitalize()}", colour=discord.Colour.blue()
    )
    embed.set_author(
        name="by Agatha & Ngikngok",
        icon_url="https://cdn.discordapp.com/attachments/952898818767196202/1014169174320369704/Screenshot_2022-08-07_132626.png",
    )
    for a, x in enumerate(daftarjudul):
        embed.add_field(name=x, value=listraya[a], inline=False)
    await ctx.send(embed=embed)
    return


@client.command(hlep="Gombalan maut")
async def gombal(ctx):
    url = f"https://www.fimela.com/relationship/read/5076974/50-kata-kata-chat-gebetan-yang-seru-dan-bikin-pdkt-lancar"
    alamat = requests.get(url).text
    soup = BeautifulSoup(alamat, "html.parser")

    judul = soup.find(
        "div",
        class_="read-page--article-triumvirate js-article-triumvirate read-page--article-triumvirate_with-ads",
    )

    # Head_2 itu untuk nyimpen judul2nya
    head_2 = judul.find_all("h2")  # type: ignore
    # Cleaning head_2
    head_clean = []
    TAG_RE = re.compile(r"<[^>]+>")
    for key, value in enumerate(head_2):
        head_clean.append(TAG_RE.sub("", str(value)))

    # Sekarang cari isi artikelnya
    content = judul.find("div", class_="article-content-body__item-content")  # type: ignore
    kalimat = []
    kalimat_clean = []
    # isi = content.find_all('p')
    while True:
        try:
            content = content.find_next(class_="article-content-body__item-content")  # type: ignore
            isi = content.find_all("p")  # type: ignore
            kalimat.append(isi)
        except:
            break

    for key, value in enumerate(kalimat):
        value = TAG_RE.sub("", str(value))
        value = re.findall(r"\".*?\"", value)
        for x in value:
            kalimat_clean.append(x)
    pil = random.randint(0, 49)
    embed = discord.Embed(
        title=f"Gombalan dari ngikngok 💗", colour=discord.Colour.blue()
    )
    embed.add_field(name="\u200b", value=kalimat_clean[pil], inline=False)
    await ctx.send(embed=embed)
    return


@client.command(help="Quotes acak")
async def quotes(ctx):
    pil = random.randint(0,153)
    print(pil)
    all_quotes = []
    TAG_RE = re.compile(r"<[^>]+>")
    if(pil < 59):
        url_1 = f"https://www.brilio.net/wow/40-kata-kata-keren-quotes-cocok-dijadikan-caption-medsosmu-191127s.html"
        alamat_1 = requests.get(url_1).text
        soup_1 = BeautifulSoup(alamat_1, "html.parser")

        body_1 = soup_1.find("div", class_="main-content")
        content_1 = body_1.find_all("p") #type: ignore

        for key, value in enumerate(content_1):
            value = TAG_RE.sub("", str(value))
            value = re.findall(r"\".*?\"", str(value))
            for x in value:
                all_quotes.append(x)
    
    elif(pil < 153):
        pil=pil-59
        url_2 = f"https://www.brilio.net/wow/40-kata-kata-keren-quotes-cocok-dijadikan-caption-medsosmu-191127s/kata-kata-keren-quotes-cinta-2212055.html"
        alamat_2 = requests.get(url_2).text
        soup_2 = BeautifulSoup(alamat_2, "html.parser")

    
        body_2 = soup_2.find("div", class_="main-content")
        content_2 = body_2.find_all("p") #type: ignore

        for key, value in enumerate(content_2):
            value = TAG_RE.sub("", str(value))
            value = re.findall(r"\".*?\"", str(value))
            for x in value:
                all_quotes.append(x)

    else:
        pil=pil-154
        url_3 = f'https://www.cermati.com/artikel/kata-kata-motivasi-hidup-terbaik-untuk-buat-hidup-kamu-lebih-semangat'
        alamat_3 = requests.get(url_3).text
        soup_3 = BeautifulSoup(alamat_3, 'html.parser')
        body_3 = soup_3.find('ol',class_='ordered-section')
        content_3 = body_3.find_all('p') #type: ignore

        next_quotes = []
        TAG_RE = re.compile(r'<[^>]+>')
        for key,value in enumerate(content_3):
            value = TAG_RE.sub('',str(value))
            value = re.sub('\xa0','',str(value))
            value = re.sub('\n\n\n\n\n','',str(value))
            if(value==''):
                continue
            next_quotes.append(value)

        next_quotes.pop(0)
        for key,value in enumerate(next_quotes):
            if(not value.__contains__('Tip:')):
                all_quotes.append(value)
    embed = discord.Embed(
        title=f"Quotes bijak dari ngikngok😎🆒", colour=discord.Colour.blue()
    )
    embed.add_field(name="\u200b", value=all_quotes[pil], inline=False)
    await ctx.send(embed=embed)
    return

@client.command(help='Quote motivasi')
async def motivation(ctx):
    url_3 = f'https://www.cermati.com/artikel/kata-kata-motivasi-hidup-terbaik-untuk-buat-hidup-kamu-lebih-semangat'
    alamat_3 = requests.get(url_3).text
    soup_3 = BeautifulSoup(alamat_3, 'html.parser')
    body_3 = soup_3.find('ol',class_='ordered-section')
    content_3 = body_3.find_all('p') #type: ignore

    next_quotes = []
    qutoes_fix = []
    TAG_RE = re.compile(r'<[^>]+>')
    for key,value in enumerate(content_3):
        value = TAG_RE.sub('',str(value))
        value = re.sub('\xa0','',str(value))
        value = re.sub('\n\n\n\n\n','',str(value))
        if(value==''):
            continue
        next_quotes.append(value)

    next_quotes.pop(0)
    for key,value in enumerate(next_quotes):
        if(not value.__contains__('Tip:')):
            qutoes_fix.append(value)

    print(*qutoes_fix,sep='\n')
    print(len(qutoes_fix))

@client.command(
    help="Mencari Tweet yang mengandung kata tertentu (7 hari terakhir) n.tweet <text>"
)
async def tweet(ctx, *, args):
    final = ""
    query = f"{args} -is:retweet "
    limit = 5
    embed = discord.Embed(
        title=f"Getting {args} in past 7 days", colour=discord.Colour.blue()
    )
    response = tweepy.Paginator(
        api_2.search_recent_tweets,
        query=query,
        max_results=100,
        tweet_fields=["created_at", "author_id"],
    ).flatten(limit=limit)
    for tweet in response:
        limit -= 1
        date = tweet.created_at.strftime("%m-%d %H:%M")
        code = "@" + getname(tweet.id) + " at " + str(date)
        if (
            len(
                final
                + code
                + "\nTweeted :\n"
                + tweet.text.strip()
                + "\n=======end tweet========\n"
            )
            < 1024
        ):
            final = (
                final
                + code
                + "\nTweeted :\n"
                + tweet.text.strip()
                + "\n=======end tweet========\n"
            )
        else:
            embed.add_field(name="\u200b", value="\u200b")
            embed.add_field(name="\u200b", value=final, inline=False)
            final = (
                ""
                + code
                + "\nTweeted :\n"
                + tweet.text.strip()
                + "\n=======end tweet========\n"
            )

    if limit == 5:
        embed.add_field(name="Nothing Found!", value="\u200b", inline=False)
    else:
        embed.add_field(name="\u200b", value=final, inline=False)
    await ctx.send(embed=embed)
    return


@client.command(help="Top 7 Trending in Twitter Indonesia")
async def twttrend(ctx):
    embed = discord.Embed(
        title=f"7 Trending News in Indonesia!", colour=discord.Colour.blue()
    )
    final = ""
    response = api_1.get_place_trends(id=1044316)
    for t in response:
        for a, u in enumerate(t["trends"][:7]):
            final = final + (
                f"{a+1}. "
                + (u["name"] if u["name"][0] != "#" else u["name"][1:])
                + "\n"
            )
    embed.add_field(name="\u200b", value=final, inline=False)
    await ctx.send(embed=embed)
    return


star5 = [
    "Balmung GG GEMING",
    "Icewind Arrow",
    "Negating Cube",
    "Chakram of The Seas",
    "Molten Shield V2",
    "Thunderblades",
    "Rosy Edge",
    "Absolute Zero",
    "Dual EM Stars",
    "Scythe of the Crow",
]
star4 = [
    "Thunderous Halberd",
    "Nightingale's Feather",
    "Pummeler",
    "Staff of Scars",
    "The Terminator",
]
star3 = ["EM Blade", "Combat Blade", "Frosted Spear", "Composite Bow"]
battery = "Weapon Batery III"


@client.command(help="gacha frigg TOF")
async def gacha(ctx):
    name = str(ctx.author).split("#")[0]
    df = pd.read_csv(
        "E:\\Folder_apps\\NGODING\\Discord_bot\\NgikngokTOF.csv", index_col=0
    )
    if name not in list(df["name"]):
        dataauthor = [0, name, 0]
        # df = df.append(pd.Series(dataauthor, index=df.columns[:len(dataauthor)]), ignore_index=True)
        df.loc[len(df)] = pd.Series(dataauthor)  # type: ignore
        df.to_csv("NgikngokTOF.csv")
    del df
    df = pd.read_csv("NgikngokTOF.csv", index_col=0)
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
    pity = df.loc[df[df == name].index[0], "pity"]  # type: ignore
    ans = []
    luckynum = random.randint(0, 10)
    for _ in np.arange(0, 10):
        pity += 1
        if pity == 80:
            ans.append(1)
        elif pity % 10 == luckynum:
            ans.append(2)
        else:
            ssr = 0.0075 + (pity * (1.25 / 80) / 100)
            sr = 0.01 + (pity * (11 / 80) / 100)
            r = 0.9140 - (pity * (11.40 / 80) / 100)
            batt = 0.0685 - (pity * (0.85 / 80) / 100)
            ans.append(np.random.choice(np.arange(1, 5), p=[ssr, sr, r, batt]))
    if pity >= 80:
        pity = pity % 80
    final = ""
    ssrrp = 0.5 / 9
    srrp = 1 / 5
    rrp = 1 / 4
    for x in ans:
        if x == 1:
            pil = np.random.choice(
                np.arange(0, len(star5)),
                p=[0.5, ssrrp, ssrrp, ssrrp, ssrrp, ssrrp, ssrrp, ssrrp, ssrrp, ssrrp],
            )
            final = final + "[SSR] ✭✭✭✭✭ " + star5[pil] + "\n"
        elif x == 2:
            pil = np.random.choice(
                np.arange(0, len(star4)), p=[srrp, srrp, srrp, srrp, srrp]
            )
            final = final + "[SR]  ✭✭✭✭✰ " + star4[pil] + "\n"
        elif x == 3:
            pil = np.random.choice(np.arange(0, len(star3)), p=[rrp, rrp, rrp, rrp])
            final = final + "[R]   ✭✭✭✰✰ " + star3[pil] + "\n"
        else:
            final = final + "[Batt]✭✭✰✰✰ " + battery + "\n"
    embed = discord.Embed(title=f"{name}'s Gacha", colour=discord.Colour.blue())
    df.loc[df[df == name].index[0], "pity"] = pity
    df.to_csv(f"E:\\Folder_apps\\NGODING\\Discord_bot\\NgikngokTOF.csv")
    embed.set_author(
        name="by Agatha & Ngikngok",
        icon_url="https://cdn.discordapp.com/attachments/952898818767196202/1014169174320369704/Screenshot_2022-08-07_132626.png",
    )
    embed.add_field(name=f"Hasil Gacha | {pity}/80 |", value=final, inline=False)
    await ctx.send(embed=embed)
    return


status = cycle(
    [
        "Cilukkk",
        "Baaa!",
        "NgikNgook",
        "Ingat jangan percaya Aris",
        "Ingat berdoa",
        "Hemat Uang",
        "Kerja Bagus",
    ]
)


@client.event
async def on_ready():
    change_status.start()
    print("Login Success {0}".format(client.user))


@tasks.loop(seconds=60)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))


client.run(token)
