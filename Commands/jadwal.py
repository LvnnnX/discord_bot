import discord
from discord.ext import commands
import pandas as pd
import pathlib

BASE_DIR = pathlib.Path.cwd().parent
EXCEL_DIR = BASE_DIR / "Excel"

kelas_valid = ['A','B','C','D','E','F']
df = pd.read_excel(f'{EXCEL_DIR}/Jadual Genap 2022-2023 eDIT 1.xlsx')
webex = pd.read_excel(f'{EXCEL_DIR}/Webex Dosen.xlsx')
df = df[11:18]
df.rename(columns={'Unnamed: 0' : 'Kode', 'Unnamed: 1':'Mata Kuliah', 'Unnamed: 2':'SKS','INISIAL DOSEN':'A', 'Unnamed: 4' : 'B','Unnamed: 5' : 'C','Unnamed: 6' : 'D','Unnamed: 7' : 'E','Unnamed: 8' : 'F','HARI / WAKTU' : 'Jadwal A','Unnamed: 10' : 'Jadwal B','Unnamed: 11' : 'Jadwal C','Unnamed: 12' : 'Jadwal D','Unnamed: 13' : 'Jadwal E','Unnamed: 14' : 'Jadwal F'},inplace=True)
df.drop(columns=["Kode", "SKS"], inplace=True)
df = df.astype({f"Mata Kuliah": str})


class jadwal(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Jadwal loaded!")
    
    @commands.command(help='n.jadwal (jadwal Informatika 2021)')
    async def jadwal(self, ctx, args):
        if(args.lower()=='all'):
            all_kelas = kelas_valid
            embed = discord.Embed(
                title=f"Jadwal Semua Kelas Informatika 21 | Genap 2023", colour=discord.Colour.blue()
            )
        elif(args.upper() in kelas_valid):
            all_kelas = [f'{args.upper()}']
            embed = discord.Embed(
                title=f"Jadwal Kelas {args.upper()} Informatika 21 | Genap 2023", colour=discord.Colour.blue()
            )
        else:
            embed = discord.Embed(
            title=f"Kelas {args.upper()} tidak valid!", colour=discord.Colour.blue()
            )
            await ctx.send(embed=embed)
            return
        
        # Data jadwal
        # df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
        # dropindex = [int(x) for x in range(0, 12)] + [int(x) for x in range(19, len(df))]
        # df.drop(index=dropindex, inplace=True)
        # Data jadwal fix

        # Priorities untuk sorting
        priorities = ["minggu", "sabtu", "jumat", "kamis", "rabu", "selasa", "senin"]
        # Add field to discord embed
        #KELAS A#
        for kelas in all_kelas:
            kelas_df = df.copy()
        # display(kelas_df)
            for key in range(len(kelas_df)):
                hari_now=kelas_df[f'Jadwal {kelas}'].iloc[key].split('/')[0].strip().lower()
                for key2 in range(key+1,len(kelas_df)):
                    hari_next=kelas_df[f'Jadwal {kelas}'].iloc[key2].split('/')[0].strip().lower()
                    if(priorities.index(hari_now)<priorities.index(hari_next)):
                        b,a = kelas_df.iloc[key2].copy() ,kelas_df.iloc[key].copy()
                        kelas_df.iloc[key2],kelas_df.iloc[key] = a,b
                        hari_now = hari_next
                    elif(priorities.index(hari_now)==priorities.index(hari_next)):
                        jam_now = kelas_df[f'Jadwal {kelas}'].iloc[key].split('/')[1].strip().lower()[:2]
                        jam_next = kelas_df[f'Jadwal {kelas}'].iloc[key2].split('/')[1].strip().lower()[:2]
                        if(int(jam_now)>int(jam_next)):
                            b,a = kelas_df.iloc[key2].copy() ,kelas_df.iloc[key].copy()
                            kelas_df.iloc[key2],kelas_df.iloc[key] = a,b
                linkweb = ['' for x in range(len(kelas_df))]
                for x in range(len(kelas_df)):
                    namadosen = kelas_df[f'{kelas}'].iloc[x]
                    for y in range(len(webex)):
                        namadosen2 = webex['Nama'].iloc[y]
                        if(namadosen==namadosen2):
                            linkweb[x] = (webex['Link'].iloc[y])
                kelas_df['Link Webex'] = linkweb
            texter = ""
            date = ""
            for w, x, y, z in zip(kelas_df['Link Webex'], kelas_df["Mata Kuliah"], kelas_df[f"{kelas}"], kelas_df[f"Jadwal {kelas}"]):
                texter = texter + x + "\n" + y.split(",")[0] + ("\n"+"." * 10 if len(x)<=28 else '') + ('\n'+'.'*10+'\n' if len(w)>=53 else '\n')
                date = date + z +  ('\n'+w+'\n' if w != '' else '\n.\n.\n')
            embed.add_field(name=f"『KELAS {kelas}』", value=texter, inline=True)
            # embed.add_field(name=f'KELAS {new}',value=df['MATA KULIAH'].to_string(index=False),inline=True)
            embed.add_field(name="『JAM PELAJARAN』", value=date, inline=True)
            # embed.add_field(name='JAM PELAJARAN',value=df[f'JADWAL {new}'].to_string(index=False),inline=True)
            embed.add_field(name="\u200b", value="\u200b")

        embed.set_author(
            name="by Agatha & Ngikngok",
            icon_url="https://cdn.discordapp.com/attachments/952898818767196202/1076789878404161556/320890519_721815005774688_2433660246175642108_n.jpg",
        )
        embed.set_footer(text='source: Jadual Genap 2022-2023 eDIT 1')
        await ctx.send(embed=embed)

async def setup(client):
    await client.add_cog(jadwal(client))