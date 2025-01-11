from abilities.basic_attack import BasicAttack


class FocusAttack(BasicAttack):
    def __init__(self, coeffs, name, description, cooldown, cost, element, sprite_path):
        super().__init__(coeffs, name, description, cooldown, cost, element, sprite_path)
        self.focus_gain = 2

    def use(self, user, target):
        ret = super().use(user, target)
        user.current_focus += self.focus_gain
        return ret

    def get_upgrade_description(self):
        return f"{super().get_upgrade_description()}focus gain: {self.focus_gain} -> {self.focus_gain + 1}\n"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.coeffs['strength'] *= 1.5
            self.coeffs['speed'] *= 1.5
            self.level += 1
            self.focus_gain += 1
            return True
        return False
