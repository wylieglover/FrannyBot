import os 
from death_count import Death
from twitchio.ext import commands, routines
from tinydb import TinyDB, Query

cogs = [
    "cogs.deathcog",
]

class Bot(commands.Bot):
    def __init__(self):
        self.db = TinyDB('../db.json')
        self.channels = os.environ["CHANNELS"].split("#")
        super().__init__(
            token=os.environ['TMI_TOKEN'],
            client_id=os.environ['CLIENT_ID'],
            nick=os.environ['BOT_NICK'],
            prefix=os.environ['BOT_PREFIX'],
            initial_channels=self.channels
        )

        for cog in cogs:
            self.load_module(cog)
            self.reloadcogs.start(bot=self)

    def initialize_db(self, channels):
        User = Query()
        for channel in channels:
            users = self.db.search(User.name == channel)
            if not users:
                self.db.insert({"name": channel, "death_count": 0})
    
    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f'Logged into {self.channels}')
        self.initialize_db(self.channels)

    @routines.routine(seconds=5)
    async def reloadcogs(self, bot):
        for cog in cogs:
            bot.reload_module(cog)

if __name__ == "__main__":
    bot = Bot()
    bot.run()
