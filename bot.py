import os 
from twitchio.ext import commands

class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            token=os.environ['TMI_TOKEN'],
            client_id=os.environ['CLIENT_ID'],
            nick=os.environ['BOT_NICK'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=[os.environ['CHANNEL']]
        )
    
    @commands.command(name='hi')
    async def hi(self, ctx):
        await ctx.send(ctx)

if __name__ == "__main__":
    bot = Bot()
    bot.run()
