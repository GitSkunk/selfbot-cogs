# Mah first cog. Written for appu1232's selfbot.
# Can be used under the same license as the bot itself.

import discord
from discord.ext import commands


class ShowColor:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def color(self, ctx, rgb):
        if not rgb.startswith("#"):
            rgb = "#" + rgb
        if len(rgb) < 7:
            rgb = rgb.ljust(7, "0")
        elif len(rgb) > 7:
            rgb = rgb[:7]

        try:
            await ctx.message.delete()
        except:
            pass
        em = discord.Embed(title=rgb, color=int(rgb.strip("#"), 16))
        em.set_thumbnail(url="http://www.colorcombos.com/images/colors/{}.png".format(rgb.strip("#")))
        em.add_field(name="Useful Stuff", value="[Info and color compliments](http://www.colorhexa.com/{})".format(rgb.strip("#")), inline=True)
        await ctx.send(content=None, embed=em)


def setup(bot):
    bot.add_cog(ShowColor(bot))
