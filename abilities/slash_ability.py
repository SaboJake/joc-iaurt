from abilities.attack import Attack
from units.unit import Unit

class SlashAbility:
    def __init__(self):
        self.attack = Attack("physical", 10, 0.1, 1.5)

    def hit(self, attacker: Unit, target: Unit):
        return self.attack.attack(attacker, target)