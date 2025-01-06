from effects.effect import Effect


class MultiEffect(Effect):
    def __init__(self, name, duration, effect, element, can_stack, effects):
        super().__init__(name, duration, effect, element, can_stack)
        # Array of effects to apply
        self.effects = effects

    def apply(self, target):
        for effect in self.effects:
            effect.apply(target)

    def remove(self, target):
        for effect in self.effects:
            effect.remove(target)