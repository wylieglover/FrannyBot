from twitchio.ext import commands
from win_loss_count import WinLoss

class WinLossCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.win_loss = WinLoss()
    
    @commands.command(name="win", aliases=["w"])
    async def incrementwins(self, ctx):
        win_count = self.win_loss.increment_win_count(ctx.channel)
        await ctx.send(f"Wins: {win_count}")

    @commands.command(name="loss", aliases=["l"])
    async def incrementloss(self, ctx):
        loss_count = self.win_loss.increment_loss_count(ctx.channel)
        await ctx.send(f"Losses: {loss_count}")

    @commands.command(name="wl", aliases=["winloss", "wins", "losses", "WL"])
    async def displaywl(self, ctx):
        win_count = self.win_loss.get_win_count(ctx.channel)
        loss_count = self.win_loss.get_loss_count(ctx.channel)

        ratio = 0
        if(win_count != 0):
            ratio = round(win_count / (win_count + loss_count), 2)
        await ctx.send(f"{win_count}W  {loss_count}L | {ratio}")
    
    @commands.command(name="resetwl", aliases=["rwl"])
    async def resetwinloss(self, ctx):
        if ctx.author.is_mod:
            win_count, loss_count = self.win_loss.reset_win_loss_count(ctx.channel)
            await ctx.send(f"W: {win_count} | L: {loss_count}")

def prepare(bot):
    bot.add_cog(WinLossCog(bot))
    