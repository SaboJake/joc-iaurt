from effects.effect import Effect
from units.unit import Unit


class Wound(Effect):
    def __init__(self, name, description, duration, element, can_stack, coeffs, user):
        super().__init__(name, description, duration, None, element, can_stack)
        self.coeffs = coeffs
        self.user = user

    def apply(self, target: Unit):
        total = 0
        for key, value in self.coeffs.items():
            dec = value * getattr(self.user.stats, key)
            # print(key, getattr(self.user.stats, key))
            dec = round(dec)
            target.health -= dec
            total += dec
        return total

    def remove(self, target: Unit):
        pass

    def copy(self):
        return Wound(self.name, self.description, self.duration, self.element, self.can_stack, self.coeffs, self.user)


class Weaken(Effect):
    def __init__(self, name, description, duration, element, can_stack, coeffs, user):
        super().__init__(name, description, duration, None, element, can_stack)
        self.coeffs = coeffs
        self.user = user

    def apply(self, target: Unit):
        for key, value in self.coeffs.items():
            dec = value * getattr(self.user.stats, key)
            dec = round(dec)
            setattr(target.stats, key, getattr(target.stats, key) - dec)
        return 0

    def remove(self, target: Unit):
        pass

    def copy(self):
        return Weaken(self.name, self.description, self.duration, self.element, self.can_stack, self.coeffs, self.user)

class Stun(Effect):
    def __init__(self, name, description, duration, element, can_stack):
        super().__init__(name, description, duration, None, element, can_stack)
        self.is_stun = True

    def apply(self, target: Unit):
        return 0

    def remove(self, target: Unit):
        pass

    def copy(self):
        return Stun(self.name, self.description, self.duration, self.element, self.can_stack)
