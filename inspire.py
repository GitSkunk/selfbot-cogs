import discord
from discord.ext import commands
import requests

class Inspiration:

    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['im'], pass_context=True)
    async def inspireme(self, ctx):
        page = requests.get("http://inspirobot.me/api?generate=true")
        if page.status_code != 200:
            await ctx.send("Problem getting an inspirational pic: {} - {}".format(page.status_code, page.reason))
        else:
            try:
                await self.bot.delete_message(ctx.message)
            except:
                pass
            pic = page.content.decode('utf-8')
            em = discord.Embed(title="Inspirobot")
            em.set_image(url=pic)
            await ctx.send(content=None, embed=em)


def setup(bot):
    bot.add_cog(Inspiration(bot))
