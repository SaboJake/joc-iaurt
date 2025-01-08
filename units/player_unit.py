from units.friendly_unit import FriendlyUnit


class PlayerUnit(FriendlyUnit):
    def __init__(self, name, clas, base_stats, stats, level=1):
        super().__init__(name, clas, base_stats, stats, level)
        self.exp = 0
        self.exp_to_next_level = 100
        self.skill_points = 5
        self.stat_points = 5

    def gain_exp(self, exp):
        self.exp += exp
        if self.exp >= self.exp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.exp = 0
        self.exp_to_next_level *= 2
        self.base_stats += self.stats
        self.stats += self.stats
        print(f'{self.name} leveled up to level {self.level}!')

    def is_player(self):
        return True