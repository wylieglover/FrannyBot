#bot.py
import os 
from death_count import Death
from twitchio.ext import commands, routines
from tinydb import TinyDB, Query

cogs = [
    "cogs.deathcog",
    "cogs.winlosscog"
]

class Bot(commands.Bot):
    def __init__(self):
        self.db = TinyDB('../db.json', sort_keys=True, indent=4, separators=(',', ': '))
        self.death_table = self.db.table('death_counter_table')
        self.win_loss_table = self.db.table('win_loss_counter_table')

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

    def initialize_db(self, channels):
        User = Query()
        for channel in channels:
            death_table_users = self.death_table.search(User.name == channel)
            if not death_table_users:
                self.death_table.insert({"name": channel, "death_count": 0})
            
            win_loss_table_users = self.win_loss_table.search(User.name == channel)
            if not win_loss_table_users:
                self.win_loss_table.insert({"name": channel, "win count": 0, "loss count": 0})
    
    async def event_ready(self):
        print(f"Logged in as | {self.nick}")
        print(f'Logged into {self.channels}')
        self.initialize_db(self.channels)

if __name__ == "__main__":
    bot = Bot()
    bot.run()
