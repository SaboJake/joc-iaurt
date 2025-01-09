from effects.effect import Effect


class MultiEffect(Effect):
    def __init__(self, name, description, duration, effect, element, can_stack, effects):
        super().__init__(name, description, duration, effect, element, can_stack)
        # Array of effects to apply
        self.effects = effects

    def apply(self, target):
        for effect in self.effects:
            effect.apply(target)

    def remove(self, target):
        for effect in self.effects:
            effect.remove(target)

    def copy(self):
        return MultiEffect(self.name, self.description, self.duration, self.effect, self.element, self.can_stack, self.effects)