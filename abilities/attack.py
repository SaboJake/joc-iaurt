import random
from units.unit import Unit

class Attack:
    def __init__(self, attack_type: str, damage: int, crit_chance: float, crit_multiplier: float):
        self.attack_type = attack_type
        self.damage = damage
        self.crit_chance = crit_chance
        self.crit_multiplier = crit_multiplier

    def attack(self, attacker: Unit, target: Unit):
        attack_damage = self.damage
        if self.attack_type == "physical":
            self.crit_chance += attacker.stats.physical_piercing / 100
            self.crit_multiplier += attacker.stats.physical_piercing / 100
            attack_damage -= target.stats.physical_defence
        elif self.attack_type == "elemental":
            self.crit_chance += attacker.stats.elemental_piercing / 100
            self.crit_multiplier += attacker.stats.elemental_piercing / 100
            attack_damage -= target.stats.elemental_defence

        is_crit = random.randint(1, 100) <= self.crit_chance * 100
        if is_crit:
            attack_damage *= self.crit_multiplier

        target.health -= attack_damage
        return attack_damage