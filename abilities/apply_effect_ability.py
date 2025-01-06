from abilities.ability import Ability

class ApplyEffectAbility(Ability):
    def __init__(self, effect, name, description, cooldown, cost, target):
        super().__init__(name, description, cooldown, cost, target)
        self.effect = effect

    def use(self, user, target):
        if not super().use(user, target):
            return 0
        target.add_effect(self.effect)