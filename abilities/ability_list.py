from abilities.apply_effect_ability import ApplyEffectAbility
from abilities.basic_attack import BasicAttack


class FocusAttack(BasicAttack):
    def __init__(self, coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped)
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

class ApplyWoundAbility(ApplyEffectAbility):
    def __init__(self, wound_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(wound_effect, name, description, cooldown, cost, element, sprite_path, max_equipped)

    def get_upgrade_description(self):
        return f"{super().get_upgrade_description()}wound effect: {self.effect.coeffs['strength']} -> {self.effect.coeffs['strength'] + 0.1}\n"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.effect.coeffs['strength'] += 0.1
            self.level += 1
            return True
        return False

class ApplyWeakenAbility(ApplyEffectAbility):
    def __init__(self, weaken_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(weaken_effect, name, description, cooldown, cost, element, sprite_path, max_equipped)

    def get_upgrade_description(self):
        return f"{super().get_upgrade_description()}weaken effect: {self.effect.coeffs['strength']} -> {self.effect.coeffs['strength'] + 0.1}\n"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.effect.coeffs['strength'] += 0.1
            self.level += 1
            return True
        return False

class ApplyStunAbility(ApplyEffectAbility):
    def __init__(self, stun_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(stun_effect, name, description, cooldown, cost, element, sprite_path, max_equipped)

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.level += 1
            return True
        return False

class ApplyRegenAbility(ApplyEffectAbility):
    def __init__(self, regen_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(regen_effect, name, description, cooldown, cost, element, sprite_path, max_equipped)

    def get_upgrade_description(self):
        return f"{super().get_upgrade_description()}regen effect: {self.effect.coeffs['strength']} -> {self.effect.coeffs['strength'] + 0.1}\n"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.effect.coeffs['strength'] += 0.1
            self.level += 1
            return True
        return False

class ApplyBuffAbility(ApplyEffectAbility):
    def __init__(self, buff_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(buff_effect, name, description, cooldown, cost, element, sprite_path, max_equipped)

    def get_upgrade_description(self):
        return f"{super().get_upgrade_description()}buff effect: {self.effect.coeffs['strength']} -> {self.effect.coeffs['strength'] + 0.1}\n"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.effect.coeffs['strength'] += 0.1
            self.level += 1
            return True
        return False

class StunAttack(BasicAttack, ApplyStunAbility):
    def __init__(self, coeffs, stun_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        BasicAttack.__init__(self, coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped)
        ApplyStunAbility.__init__(self, stun_effect, name, description, cooldown, cost, element, sprite_path)

    def use(self, user, target):
        ret = BasicAttack.use(self, user, target)
        ApplyStunAbility.use(self, user, target)
        return ret

    def get_upgrade_description(self):
        return f"{BasicAttack.get_upgrade_description()}{ApplyStunAbility.get_upgrade_description()}"

    def ability_upgrade(self):
        return BasicAttack.ability_upgrade(self) or ApplyStunAbility.ability_upgrade(self)