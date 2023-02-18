import discord
from discord.ext import commands
import pandas as pd
import pathlib
import re

BASE_DIR = pathlib.Path(__file__).parent.parent
EXCEL_DIR = BASE_DIR / "Excel"

class jadwal(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Jadwal loaded!")
    
    @commands.command(help='n.jadwal (jadwal Informatika 2021)')
    async def jadwal(self, ctx):
        # Data jadwal
        df = pd.read_excel(
            f"{EXCEL_DIR}\\Jadual Ganjil 2022-2023.xlsx",
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
            f"{EXCEL_DIR}\\Jadual Ganjil 2022-2023.xlsx",
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
                df[f'JADWAL {x}'].iloc[a] = re.sub(
                    "/", "|", str(df[f'JADWAL {x}'].iloc[a])  # type: ignore
                )  # type: ignore
                # print(b)
                # Mengganti kode dengan nama dosen
                for c, d in enumerate(datadosen["KODE"]):
                    # print(d,b)
                    if d == b:  # kode ketemu yang sama
                        # print('found')
                        # type: ignore #ganti ke nama
                        df[f"Dosen {x}"].iloc[a] = datadosen.loc[c, "NAMA"]  # type: ignore

        # Priorities untuk sorting
        priorities = ["minggu", "sabtu", "jumat", "kamis", "rabu", "selasa", "senin"]
        df = df.astype({f"MATA KULIAH": str})
        # Add field to discord embed
        for new in kelas:
            df = df.astype({f"JADWAL {new}": str, f'Dosen {new}': str}) 
            for x in range(1, len(df)):
                key = df[f"JADWAL {new}"].iloc[x-1].split()[0]
                if(key=='nan'):
                    continue
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
                print(texter)
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

async def setup(client):
    await client.add_cog(jadwal(client))