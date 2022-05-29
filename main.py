from email import message
from typing_extensions import Self
import discord
from random import *
import yfinance as yf
import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime
import plotly.graph_objs as go
import kaleido
from discord.ext import commands,tasks
import os
import youtube_dl
import asyncio
import music

cogs = [music]
intents = discord.Intents().all()
client = commands.Bot(command_prefix='#',intents=intents)

@client.event
async def on_ready():
    print('Login Success {0}'.format(client.user))

for i in range(len(cogs)):
    cogs[i].setup(client)


client.run("OTc4NDY4OTQyMjg2ODQ4MDUx.Gaka8M.szNKKez_fFxDrur4KZw3xHDcbW3kHpmCN0iWgo")