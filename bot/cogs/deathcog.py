from twitchio.ext import commands
from death_count import Death

class DeathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.death = Death()
    
    @commands.command(name="death")
    async def incrementdeaths(self, ctx):
        death_count = self.death.increment_death_count(ctx.channel)
        await ctx.send(f"Death counter: {death_count}")

    @commands.command(name='resetdeaths')
    async def resetdeaths(self, ctx):
        if ctx.author.is_mod:
            death_count = self.death.reset_death_count(ctx.channel)
            await ctx.send(f"Death counter: {death_count}")

def prepare(bot):
    bot.add_cog(DeathCog(bot))
    