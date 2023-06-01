import os 
from twitchio.ext import commands
from tinydb import TinyDB, Query

db = TinyDB('db.json')

class Bot(commands.Bot):
    def __init__(self):
        self.channels = os.environ["CHANNELS"].split("#")
        super().__init__(
            token=os.environ['TMI_TOKEN'],
            client_id=os.environ['CLIENT_ID'],
            nick=os.environ['BOT_NICK'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=self.channels
        )
    
    def initialize_db(self, channels):
        User = Query()
        for channel in channels:
            users = db.search(User.name == channel)
            if not users:
                db.insert({"name": channel, "death_count": 0})
    
    def get_death_count(self, user):
        User = Query()
        death_count = db.search(User.name == user.name)[0].get("death_count", 0)
        return death_count

    def increment_death_count(self, user):
        death_count = self.get_death_count(user)
        death_count += 1
        db.update({"death_count": death_count}, Query().name == user.name)
        return death_count
        
    def reset_death_count(self, user):
        death_count = self.get_death_count(user)
        death_count = 0
        db.update({"death_count": death_count}, Query().name == user.name)
        return death_count

    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f'Logged into {self.channels}')
        self.initialize_db(self.channels)
    
    @commands.command(name='death')
    async def death(self, ctx):
        death_count = self.increment_death_count(ctx.channel)
        await ctx.send(f"Death counter: {death_count}")

    @commands.command(name='resetdeaths')
    async def resetdeaths(self, ctx):
        death_count = self.reset_death_count(ctx.channel)
        await ctx.send(f"Death counter: {death_count}")

if __name__ == "__main__":
    bot = Bot()
    bot.run()
