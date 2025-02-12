import random

from abilities.ability import Ability

class BasicHeal(Ability):
    def __init__(self, coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(name, description, cooldown, cost, 'ally', sprite_path, max_equipped)
        self.coeffs = {
            'strength': coeffs['strength'],
            'intelligence': coeffs['intelligence'],
            'speed': coeffs['speed']
        }
        self.element = element

    def use(self, user, target):
        if not super().use(user, target):
            print("Cannot use ability")
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
        heal = round(heal)
        target.health += heal
        return heal

    def get_upgrade_description(self):
        return f"intelligence: {self.coeffs['intelligence']} -> {self.coeffs['intelligence'] * 1.5}\nspeed: {self.coeffs['speed']} -> {self.coeffs['speed'] * 1.5}\n"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.coeffs['intelligence'] *= 1.5
            self.coeffs['speed'] *= 1.5
            self.level += 1
            return True
        return False