from utils.stats import Stats

from constants import HEALTH_CONSTANT

class Unit:

    class Coeff:
        def __init__(self, additive=0, multi=1, true=0):
            self.additive = additive
            self.multi = multi
            self.true = true
        def update(self, value: int) -> int:
            return (value + self.additive) * self.multi + self.true

    def __init__(self, name, base_stats: Stats, stats: Stats, level = 1):
        self.name = name
        self.stats = stats
        self.base_stats = base_stats
        self.health = stats.vitality * HEALTH_CONSTANT
        self.current_focus = stats.focus
        self.is_stunned = False
        self.level = level
        self.effects = []
        self.coeffs = {
            'vitality': self.Coeff(),
            'strength': self.Coeff(),
            'intelligence': self.Coeff(),
            'speed': self.Coeff(),
            'focus': self.Coeff(),
            'elemental_piercing': self.Coeff(),
            'physical_piercing': self.Coeff(),
            'elemental_defence': self.Coeff(),
            'physical_defence': self.Coeff()
        }
        # Used for dealing/taking extra damage; may be changed by effects
        self.damage_mod = 0
        self.defense_mod = 0
        # Used for dealing/receiving extra healing; may be changed by effects
        self.healing_mod = 0
        self.healing_received_mod = 0
        # Base crit chance
        self.crit_chance = 0.15

        # List of abilities
        self.abilities = []

    # Should be called every time a coefficient is changed
    def update_stats(self):
        self.stats.vitality = self.coeffs['vitality'].update(self.base_stats.vitality)
        self.stats.strength = self.coeffs['strength'].update(self.base_stats.strength)
        self.stats.intelligence = self.coeffs['intelligence'].update(self.base_stats.intelligence)
        self.stats.speed = self.coeffs['speed'].update(self.base_stats.speed)
        self.stats.focus = self.coeffs['focus'].update(self.base_stats.focus)
        self.stats.elemental_piercing = self.coeffs['elemental_piercing'].update(self.base_stats.elemental_piercing)
        self.stats.physical_piercing = self.coeffs['physical_piercing'].update(self.base_stats.physical_piercing)
        self.stats.elemental_defence = self.coeffs['elemental_defence'].update(self.base_stats.elemental_defence)
        self.stats.physical_defence = self.coeffs['physical_defence'].update(self.base_stats.physical_defence)

    def add_effect(self, effect):
        # if effect can stack add a new instance of the effect
        if effect.can_stack:
            self.effects.append(effect.copy())
        else:
            # if effect can't stack, remove all previous effects of the same type
            for e in self.effects:
                if e.name == effect.name:
                    e.remove(self)
                    self.effects.remove(e)
            self.effects.append(effect)

    def apply_effects(self):
        total = 0
        new_effects = []
        for effect in self.effects:
            total += effect.apply(self)
            effect.duration -= 1
            if effect.duration > 0:
                new_effects.append(effect)
            else:
                effect.remove(self)
        self.effects = new_effects
        return total


    def is_enemy(self):
        return True

    def is_player(self):
        return False