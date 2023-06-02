from twitchio.ext import commands
from win_loss_count import WinLoss

class WinLossCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.win_loss = WinLoss()
    
    @commands.command(name="win")
    async def incrementwins(self, ctx):
        win_count = self.win_loss.increment_win_count(ctx.channel)
        await ctx.send(f"Win counter: {win_count}")

    @commands.command(name="loss")
    async def incrementloss(self, ctx):
        loss_count = self.win_loss.increment_loss_count(ctx.channel)
        await ctx.send(f"Loss counter: {loss_count}")

    @commands.command(name="wl")
    async def displaywl(self, ctx):
        win_count = self.win_loss.increment_win_count(ctx.channel)
        loss_count = self.win_loss.increment_loss_count(ctx.channel)
        await ctx.send(f"Wins: {win_count} | Losses: {loss_count}")
    
    @commands.command(name="resetwl")
    async def resetwinloss(self, ctx):
        if ctx.author.is_mod:
            win_count, loss_count = self.win_loss.reset_win_loss_count(ctx.channel)
            await ctx.send(f"Win: {win_count} | Losses: {loss_count}")

def prepare(bot):
    bot.add_cog(WinLossCog(bot))