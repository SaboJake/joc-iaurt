from effects.effect import Effect
from units.unit import Unit

mod_map = {
    'damage_mod': 'damage_mod',
    'defense_mod': 'defense_mod',
    'healing_mod': 'healing_mod',
    'healing_received_mod': 'healing_received_mod',
    'crit_chance': 'crit_chance'
}

# Modify a single modifier of the target unit
# modifier - damage dealt/taken, healing dealt/received, crit chance
# Only multiplicative changes
class ModifyModEffect(Effect):
    def __init__(self, name, description, duration, effect, element, can_stack, mult, mod):
        super().__init__(name, description, duration, effect, element, can_stack)
        self.mult = mult
        self.mod = mod

    def apply(self, target: Unit):
        if self.mod in mod_map:
            setattr(target, mod_map[self.mod], getattr(target, mod_map[self.mod]) * self.mult)

    def remove(self, target: Unit):
        if self.mod in mod_map:
            setattr(target, mod_map[self.mod], getattr(target, mod_map[self.mod]) / self.mult)

    def copy(self):
        return ModifyModEffect(self.name, self.description, self.duration, self.effect, self.element, self.can_stack, self.mult, self.mod)