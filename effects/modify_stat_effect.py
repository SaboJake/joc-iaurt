from effects.effect import Effect


class ModifyStatEffect(Effect):
    def __init__(self, name, duration, effect):
        super().__init__(name, duration, effect)
