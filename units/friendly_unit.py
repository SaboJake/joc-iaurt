from units.unit import Unit
from utils.stats import Stats


class FriendlyUnit(Unit):
    def __init__(self, name, clas, base_stats: Stats, stats: Stats, level=1):
        super().__init__(name, base_stats, stats, level)
        self.clas = clas
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.base_stats += item.stats

    def remove_item(self, item):
        self.items.remove(item)
        self.base_stats -= item.stats

    def is_enemy(self):
        return False

    def is_player(self):
        return False