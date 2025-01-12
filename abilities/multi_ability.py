from abilities.ability import Ability


class MultiAbility(Ability):
    def __init__(self, abilities, name, description, cooldown, cost, target, sprite_path, max_equipped=10):
        super().__init__(name, description, cooldown, cost, target, sprite_path)
        self.abilities = abilities

    def use(self, user, target):
        if not super().use(user, target):
            return 0
        for ability in self.abilities:
            ability.use(user, target)
        return 1