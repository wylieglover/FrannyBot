from twitchio.ext import commands
from death_count import Death

class DeathCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.death = Death()
    
    @commands.command(name="death", aliases=["d"])
    async def incrementdeaths(self, ctx):
        death_count = self.death.increment_death_count(ctx.channel)
        await ctx.send(f'Death counter: {death_count}')

    @commands.command(name="deaths", aliases=["deathcounter", "deathcount"])
    async def displaydeaths(self, ctx):
        death_count = self.death.get_death_count(ctx.channel)
        await ctx.send(f"Death counter: {death_count}")

    @commands.command(name="resetdeaths", aliases=["resetdeath", "resetd", "rd"])
    async def resetdeaths(self, ctx):
        if ctx.author.is_mod:
            death_count = self.death.reset_death_count(ctx.channel)
            await ctx.send(f"Death counter: {death_count}")

def prepare(bot):
    bot.add_cog(DeathCog(bot))
    