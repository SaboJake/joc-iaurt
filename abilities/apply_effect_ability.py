from abilities.ability import Ability

class ApplyEffectAbility(Ability):
    def __init__(self, effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(name, description, cooldown, cost, 'enemy', sprite_path, max_equipped)
        self.effect = effect
        self.element = element

    def use(self, user, target):
        if not super().use(user, target):
            return 0
        target.add_effect(self.effect)
        return 0

    def get_upgrade_description(self):
        return "Amongus"