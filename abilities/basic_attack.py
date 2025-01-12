import random

from abilities.ability import Ability

class BasicAttack(Ability):
    def __init__(self, coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(name, description, cooldown, cost, 'enemy', sprite_path, max_equipped)
        self.coeffs = {
            'strength': coeffs['strength'],
            'intelligence': coeffs['intelligence'],
            'speed': coeffs['speed']
        }
        self.element = element

    def use(self, user, target):
        if not super().use(user, target):
            return 0
        damage = user.stats.strength * self.coeffs['strength'] + user.stats.intelligence * self.coeffs['intelligence'] + user.stats.speed * self.coeffs['speed']
        crit = user.crit_chance
        # take piercing into account
        if self.element == "physical":
            damage *= 1 + user.stats.physical_piercing / 100
            crit += user.stats.physical_piercing / 100
        else:
            damage *= 1 + user.stats.elemental_piercing / 100
            crit += user.stats.elemental_piercing / 100
        # ability may crit
        if crit > random.random():
            damage *= 1.5
        damage *= 1 + user.damage_mod
        damage *= 1 + target.defense_mod
        # take target defence into account
        if self.element == "physical":
            damage -= target.stats.physical_defence
        else:
            damage -= target.stats.elemental_defence
        damage = max(1, damage)
        damage = round(damage)
        target.health -= damage
        return damage

    def get_upgrade_description(self):
        return f"strength: {self.coeffs['strength']} -> {self.coeffs['strength'] * 1.5}\nspeed: {self.coeffs['speed']} -> {self.coeffs['speed'] * 1.5}\n"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.coeffs['strength'] *= 1.5
            self.coeffs['speed'] *= 1.5
            self.level += 1
            return True
        return False