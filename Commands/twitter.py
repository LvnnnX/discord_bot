import discord, json
import tweepy, pathlib
from discord.ext import commands
from requests_oauthlib import OAuth1

BASE_DIR = pathlib.Path(__file__).parent  # base directory
TOKEN_DIR = BASE_DIR.parent  # token directory a.k.a parent dir

# Getting keys for tweepy
with open(f"{TOKEN_DIR}\\token.json") as f:
    tokens = json.load(f)
    bearer_token = tokens["bearer_token"]
    api_key = tokens["api_key"]
    api_key_secret = tokens["api_key_secret"]
    access_token = tokens["access_token"]
    access_token_secret = tokens["access_token_secret"]
# End of getting keys for tweepy


# AUTHENTICATION PROCESS
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
# END OF AUTHENTICATION


# for getting name in twitter
def getname(id):
    response = api_2.get_tweet(
        id=id, expansions=["author_id"], user_fields=["username"]
    )
    return response.includes["users"][0].username  # type: ignore


# end getting name in twitter


# getting twitter id
def getid(id):
    user = api_2.get_user(username=id)
    return user[0].id  # type: ignore


# end getting twitter id


class twitter(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("twitter loaded!")

    # TWITTER TIMELINE USER 
    @commands.command(help='n.twtimeline <@nama yang ingin dicari>')
    async def twtimeline(self, ctx, *, args):
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
                    final = "" + (
                        date + "\n" + t.text + "\n=============end===========\n"
                    )
            if len(final) != 0:
                embed.add_field(name="\u200b", value=final, inline=False)
        await ctx.send(embed=embed)
    # END Twitter timeline user


    #twitter tweet past 7 days
    @commands.command(help="n.twtweet <text yang ingin dicari!>")
    async def twtweet(self, ctx, *, args):
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
    #end twitter tweet

    #twitter trending in 7 days
    @commands.command(help="n.twtrend (Top 7 Trending in Twitter Indonesia)")
    async def twtrend(self, ctx):
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
    #end twitter trending 7 days


async def setup(client):
    await client.add_cog(twitter(client))
