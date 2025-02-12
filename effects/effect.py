from units.unit import Unit


class Effect:
    def __init__(self, name, description, duration, effect, element, can_stack):
        self.name = name
        self.description = description
        self.duration = duration
        # function that will be called when the effect is applied
        self.effect = effect
        self.element = element
        self.can_stack = can_stack

    # target is a unit object
    def apply(self, target: Unit):
        self.effect(target)
        return 0

    def remove(self, target: Unit):
        pass

    def copy(self):
        return Effect(self.name, self.description, self.duration, self.effect, self.element, self.can_stack)