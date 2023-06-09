from tinydb import TinyDB, Query


class WinLoss:
    def __init__(self):
        self.db = TinyDB(
            "../DB/db.json", sort_keys=True, indent=4, separators=(",", ": ")
        )
        self.win_loss_table = self.db.table("win_loss_counter_table")

    def get_win_count(self, user) -> int:
        User = Query()
        win_count = self.win_loss_table.search(User.name == user.name)[0].get(
            "win_count", 0
        )
        return win_count

    def get_loss_count(self, user) -> int:
        User = Query()
        loss_count = self.win_loss_table.search(User.name == user.name)[0].get(
            "loss_count", 0
        )
        return loss_count

    def increment_win_count(self, user) -> int:
        win_count = self.get_win_count(user)
        win_count += 1
        self.win_loss_table.update({"win_count": win_count}, Query().name == user.name)
        return win_count

    def increment_loss_count(self, user) -> int:
        loss_count = self.get_loss_count(user)
        loss_count += 1
        self.win_loss_table.update(
            {"loss_count": loss_count}, Query().name == user.name
        )
        return loss_count

    def reset_win_loss_count(self, user) -> int:
        win_count = self.get_win_count(user)
        loss_count = self.get_loss_count(user)

        win_count = 0
        loss_count = 0

        self.win_loss_table.update({"win_count": win_count}, Query().name == user.name)
        self.win_loss_table.update({"loss_count": win_count}, Query().name == user.name)
        return win_count, loss_count
