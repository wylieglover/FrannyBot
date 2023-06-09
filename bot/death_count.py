from tinydb import TinyDB, Query


class Death:
    def __init__(self):
        self.db = TinyDB(
            "../DB/db.json", sort_keys=True, indent=4, separators=(",", ": ")
        )
        self.death_table = self.db.table("death_counter_table")

    def get_death_count(self, user) -> int:
        User = Query()
        death_count = self.death_table.search(User.name == user.name)[0].get(
            "death_count", 0
        )
        return death_count

    def increment_death_count(self, user) -> int:
        death_count = self.get_death_count(user)
        death_count += 1
        self.death_table.update({"death_count": death_count}, Query().name == user.name)
        return death_count

    def reset_death_count(self, user) -> int:
        death_count = self.get_death_count(user)
        death_count = 0
        self.death_table.update({"death_count": death_count}, Query().name == user.name)
        return death_count
