from utils.stats import Stats


class Unit:
    BASE_HEALTH_COEF = 10

    class Coeff:
        def __init__(self, additive=0, multi=1, true=0):
            self.additive = additive
            self.multi = multi
            self.true = true
        def update(self, value: int) -> int:
            return (value + self.additive) * self.multi + self.true

    def __init__(self, name, base_stats: Stats, stats: Stats):
        self.name = name
        self.stats = stats
        self.base_stats = base_stats
        self.health = stats.vitality * self.BASE_HEALTH_COEF
        self.effects = []
        self.coeffs = {
            'vitality': self.Coeff(),
            'strength': self.Coeff(),
            'intelligence': self.Coeff(),
            'speed': self.Coeff(),
            'focus': self.Coeff()
        }

    # Should be called every time a coefficient is changed
    def update_stats(self):
        self.stats.vitality = self.stats.coefs['vitality'].update(self.base_stats.vitality)
        self.stats.strength = self.stats.coefs['strength'].update(self.base_stats.strength)
        self.stats.intelligence = self.stats.coefs['intelligence'].update(self.base_stats.intelligence)
        self.stats.speed = self.stats.coefs['speed'].update(self.base_stats.speed)
        self.stats.focus = self.stats.coefs['focus'].update(self.base_stats.focus)

    def add_effect(self, effect):
        self.effects.append(effect)

    def apply_effects(self):
        for effect in self.effects:
            effect.apply(self)
            effect.duration -= 1
            if effect.duration == 0:
                effect.remove(self)
                self.effects.remove(effect)