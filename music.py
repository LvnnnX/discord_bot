import discord
from discord.ext import commands
import youtube_dl
from random import *
import yfinance as yf
import datetime
import plotly.graph_objs as go

class music(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send('Join dulu')
        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
        else:
            await ctx.voice_client.move_to(voice_channel)

    @commands.command()
    async def disconnect(self,ctx):
        await ctx.voice_client.disconnect()

    @commands.command()
    async def play(self,ctx,url):
        ctx.voice_client.stop()
        FFMPEG_OPTIONS = {'before_options' : '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options' :'-vn'}
        YDL_OPTIONS = {'format' : "bestaudio"}
        vc = ctx.voice_client
        with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
            info = ydl.extract_info(f"ytsearch: {url}", download=False)
            url2 = info['entries'][0]['formats'][0]['url']
            source = await discord.FFmpegOpusAudio.from_probe(url2,**FFMPEG_OPTIONS)
            vc.play(source)

    @commands.command()
    async def pause(self,ctx):
        await ctx.voice_client.pause()

    @commands.command()
    async def stop(self,ctx):
        await ctx.voice_client.stop()

    @commands.command()
    async def leave(self,ctx):
        await ctx.voice_client.disconnect()

def setup(client):
    client.add_cog(music(client))