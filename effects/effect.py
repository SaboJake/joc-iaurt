from units.unit import Unit


class Effect:
    def __init__(self, name, duration, effect):
        self.name = name
        self.duration = duration
        # function that will be called when the effect is applied
        self.effect = effect

    # target is a unit object
    def apply(self, target: Unit):
        self.effect(target)

    def remove(self, target: Unit):
        pass