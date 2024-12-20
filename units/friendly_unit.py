from units.unit import Unit
from utils.stats import Stats


class FriendlyUnit(Unit):
    def __init__(self, name, base_stats: Stats, stats: Stats):
        super().__init__(name, base_stats, stats)
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        self.base_stats += item.stats