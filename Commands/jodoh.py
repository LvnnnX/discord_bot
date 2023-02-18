import discord
from discord.ext import commands

class jodoh(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print('jodoh loaded!')

    @commands.command(help='n.jodoh <tanggal1> <tanggal2> (pencocokan tanggal lahir)')
    async def jodoh(self, ctx, args1, args2):
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
    
async def setup(client):
    await client.add_cog(jodoh(client))