from units.unit import Unit


class Effect:
    def __init__(self, name, duration, effect, element, can_stack):
        self.name = name
        self.duration = duration
        # function that will be called when the effect is applied
        self.effect = effect
        self.element = element
        self.can_stack = can_stack

    # target is a unit object
    def apply(self, target: Unit):
        self.effect(target)

    def remove(self, target: Unit):
        pass