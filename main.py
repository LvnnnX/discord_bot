import discord
import random,json
from discord.ext import commands, tasks
from dotenv import load_dotenv
from itertools import cycle
import pathlib

BASE_DIR = pathlib.Path(__file__).parent
CMDS_DIR = BASE_DIR / "Commands"
PIC_DIR = BASE_DIR / "Pictures"
TDIR = BASE_DIR / "token"

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
with open(f'{TDIR}/dctoken.json') as f:
    tokens = json.load(f)
    token = tokens['Discord_API']
client = commands.Bot(command_prefix="n.", intents=intents)


# FOR MESSAGES #
hai = ["hello", "hai", "hi", "halo", "ngikngok"]
hai_choice = ["hello_donkey.jpg", "hello_donkey2.jpg", "hello_ngikngok.jpg"]
sedih = ["sedih", "sad", "mengsad", "mengsedih"]
sedih_choice = [
    "sedih.jpeg",
    "sad_donkey1.gif",
    "sad_donkey2.gif",
    "sad_donkey3.jpg",
    "sad_donkey4.jpg",
]
siapa_choice = ["hello_ngikngok.jpg", "ngikngok.png", "sad_donkey4.jpg"]
# END FOR MESSAGES #

# FOR ON MESSAGE "REGEN21" #
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
# END FOR "REGEN21" #


# STATUS FOR BOT
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
# END STATUS FOR BOT


# RUN BOT IF MAIN TRIGGERED
def run():
    # Ketika bot baru hidup
    @client.event
    async def on_ready():
        change_status.start()
        print("Login Success {0}".format(client.user))
        # Load semua command berbentuk file
        for get_file in CMDS_DIR.glob("*.py"):
            if get_file.name != "__init__.py":
                await client.load_extension(f"Commands.{get_file.name[:-3]}")

    # Pergantian status bot
    @tasks.loop(seconds=60)
    async def change_status():
        await client.change_presence(activity=discord.Game(next(status)))

    # Load & Unload perks!
    @client.command()
    async def load(ctx, args):
        try:
            await client.load_extension(f"Commands.{args}")
            await ctx.send(f"{args} loaded!")
        except:
            await ctx.send("load failed!")

    @client.command()
    async def unload(ctx, args):
        try:
            await client.unload_extension(f"Commands.{args}")
            await ctx.send(f"{args} unloaded!")
        except:
            await ctx.send(f"unload failed!")

    @client.command()
    async def reload(ctx,args):
        try:
            await client.unload_extension(f"Commands.{args}")
            await client.load_extension(f"Commands.{args}")
            await ctx.send(f'{args} reloaded!')
        except:
            await ctx.send(f'{args} failed reloaded')

    # Mendeteksi pesan
    @client.event
    async def on_message(message):
        username = str(message.author).split("#")[0]
        user_message = str(message.content)
        channel = str(message.channel.name)

        print(f"{username}: {user_message} ({channel})")

        if message.author == client.user:  # type: ignore
            pass

        if user_message.lower() == "ping":
            # type: ignore
            await message.channel.send("pong! {0}ms".format(round(client.latency, 1)))
            return

        if user_message.lower() == "regen21":
            pil = random.randint(0, len(pic) - 1)
            await message.channel.send(f"Selamat! {username} mendapatkan kartu")
            if pil == 0:
                await message.channel.send(f"Rare CARD!")
            await message.channel.send(
                cap[pil], file=discord.File(f"{PIC_DIR}\\{pic[pil]}")
            )
            return

        if user_message.lower() in hai:
            await message.channel.send(f"Hai bang {username}")
            await message.channel.send(
                file=discord.File(
                    f"{PIC_DIR}\\{hai_choice[random.randint(0,len(hai_choice)-1)]}"
                )
            )
            return

        if user_message.lower() in sedih:
            rand = random.randint(0, 1)
            if rand == 1:
                await message.channel.send("Janji gak nangis?")
            pil = random.randint(0, len(sedih_choice) - 1)
            await message.channel.send(
                file=discord.File(f"{PIC_DIR}\\{sedih_choice[pil]}")
            )
            return

        if user_message.lower() == "kamu siapa?":
            await message.channel.send("Akulah ngikngok!")
            await message.channel.send(
                file=discord.File(
                    f"{PIC_DIR}\\{siapa_choice[random.randint(0,len(siapa_choice)-1)]}"
                )
            )
            return

        await client.process_commands(message)  # type: ignore

    client.run(token, root_logger=True)


if __name__ == "__main__":
    run()
