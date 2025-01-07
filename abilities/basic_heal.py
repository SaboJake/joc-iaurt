import random

from abilities.ability import Ability

class BasicHeal(Ability):
    def __init__(self, coeffs, name, description, cooldown, cost, element, sprite_path):
        super().__init__(name, description, cooldown, cost, 'ally', sprite_path)
        self.coeffs = {
            'strength': coeffs['strength'],
            'intelligence': coeffs['intelligence'],
            'speed': coeffs['speed']
        }
        self.element = element

    def use(self, user, target):
        if not super().use(user, target):
            return 0
        heal = user.stats.strength * self.coeffs['strength'] + user.stats.intelligence * self.coeffs['intelligence'] + user.stats.speed * self.coeffs['speed']
        crit = user.crit_chance
        # take piercing into account
        if self.element == "physical":
            heal *= 1 + user.stats.physical_piercing / 100
            crit += user.stats.physical_piercing / 100
        else:
            heal *= 1 + user.stats.elemental_piercing / 100
            crit += user.stats.elemental_piercing / 100
        # heal may crit
        if crit > random.random():
            heal *= 1.5
        heal *= 1 + user.healing_mod
        heal *= 1 + target.healing_received_mod
        # healing ignores target defence
        heal = max(1, heal)
        # target.health += heal
        return heal