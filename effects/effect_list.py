from effects.effect import Effect
from units.unit import Unit


class Wound(Effect):
    def __init__(self, name, duration, element, can_stack, coeffs, user):
        super().__init__(name, duration, None, element, can_stack)
        self.coeffs = coeffs
        self.user = user

    def apply(self, target: Unit):
        for key, value in self.coeffs.items():
            dec = value * getattr(self.user.stats, key)
            print(key, getattr(self.user.stats, key))
            target.health -= dec