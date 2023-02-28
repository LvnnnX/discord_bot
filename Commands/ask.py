import discord, pathlib, openai, json
from discord.ext import commands

BASE_DIR = pathlib.Path(__file__).parent
TOKEN_DIR = BASE_DIR.parent

with open(f"{TOKEN_DIR}/token_openai.json") as f:
    tokens = json.load(f)
    openai.api_key = tokens["secret_api_key"]

class ask(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ask loaded!")

    @commands.command(help="n.ask <pertanyaan> powered by openai!")
    async def ask(self, ctx, *args):
        model_engine = "text-davinci-003"
        question = " ".join(args)
        getdata = openai.Completion.create(
            engine=model_engine,
            prompt=question,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )
        text = getdata.choices[0].text  # type:ignore
        embed = discord.Embed(
            title=f"{question.lower().capitalize()}",
            colour=discord.Colour.blue(),
            description=text,
        )
        embed.set_author(
            name=f"{ctx.author.split('#')[0]} bertanya, ",
            icon_url=f"https://cdn.discordapp.com/attachments/952898818767196202/1014169174320369704/Screenshot_2022-08-07_132626.png",
        )
        embed.set_footer(text=f"powered by openai")
        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(ask(client))
