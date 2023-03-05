import discord
from pathlib import Path
from discord.utils import get
from discord.ext import commands
from discord import FFmpegPCMAudio
import sys
from mtranslate import translate

PATH = Path(__file__).parent
sys.path.insert(0,f'{PATH}')
from CogsHelper import get_korean_voices

class tts_kor(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print('tts_kor loaded!')

    @commands.command(help="Manually joins the bot into the voice channel")
    async def tts_to_kor(self, ctx, *args):
        if(ctx.author.voice):
            argumen = ' '.join(args)
            print(argumen)
            translated = translate(argumen, 'ko','auto')
            get_korean_voices.start(translated)
            channel = ctx.message.author.voice.channel
            voice = get(self.client.voice_clients, guild=ctx.guild)
            if voice and voice.is_connected:
                await voice.move_to(channel)
            else:
                voice = await channel.connect()
                # voice_client = self.client.voice_client_in(voice)
                # player = 
            source = FFmpegPCMAudio(source=f'{PATH}/audio.wav')
            # source = FFmpegPCMAudio(get_korean_voices.start(translated))
            player = voice.play(source)
        else:
            await ctx.send('Join a voice channel first!')

    @commands.command(help='leave')
    async def leave(self,ctx):
        await ctx.guild.voice_client.disconnect()

async def setup(client):
    await client.add_cog(tts_kor(client))