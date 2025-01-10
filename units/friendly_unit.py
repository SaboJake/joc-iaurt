from units.unit import Unit
from utils.stats import Stats

level_requirements = [0, 0, 50, 75, 100, 150, 200, 250, 300, 400, 500, 600, 700, 800, 900, 1000]

class FriendlyUnit(Unit):
    def __init__(self, name, clas, base_stats: Stats, stats: Stats, level=1, xp = 0):
        super().__init__(name, base_stats, stats, level)
        self.clas = clas
        self.xp = 25
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

    def get_xp_percentage(self):
        return (self.xp - level_requirements[self.level]) / level_requirements[self.level + 1] * 100