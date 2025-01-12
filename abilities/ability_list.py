from abilities.apply_effect_ability import ApplyEffectAbility
from abilities.basic_attack import BasicAttack
from abilities.basic_heal import BasicHeal


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
        self.max_level = 1

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.level += 1
            return True
        return False

class ApplyRegenAbility(ApplyEffectAbility):
    def __init__(self, regen_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(regen_effect, name, description, cooldown, cost, element, sprite_path, max_equipped)
        self.target = 'ally'

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
        self.target = 'ally'

    def get_upgrade_description(self):
        return f"{super().get_upgrade_description()}buff effect: {self.effect.coeffs['strength']} -> {self.effect.coeffs['strength'] + 0.1}\n"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.effect.coeffs['strength'] += 0.1
            self.level += 1
            return True
        return False

class StunAttack(BasicAttack):
    def __init__(self, coeffs, stun_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped)
        self.effect = stun_effect
        self.max_level = 1

    def use(self, user, target):
        ret = super().use(user, target)
        if not super().use(user, target):
            return ret
        target.add_effect(self.effect)
        return ret

class WoundAttack(BasicAttack):
    def __init__(self, coeffs, wound_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped)
        self.effect = wound_effect
        self.max_level = 1

    def use(self, user, target):
        ret = super().use(user, target)
        if not super().use(user, target):
            return ret
        target.add_effect(self.effect)
        return ret

class WeakenAttack(BasicAttack):
    def __init__(self, coeffs, weaken_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped)
        self.effect = weaken_effect
        self.max_level = 1

    def use(self, user, target):
        ret = super().use(user, target)
        if not super().use(user, target):
            return ret
        target.add_effect(self.effect)
        return ret

class RegenHeal(BasicHeal):
    def __init__(self, coeffs, regen_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped)
        self.effect = regen_effect
        self.max_level = 1

    def use(self, user, target):
        ret = super().use(user, target)
        if not super().use(user, target):
            return ret
        target.add_effect(self.effect)
        return ret

class BuffHeal(BasicHeal):
    def __init__(self, coeffs, buff_effect, name, description, cooldown, cost, element, sprite_path, max_equipped=10):
        super().__init__(coeffs, name, description, cooldown, cost, element, sprite_path, max_equipped)
        self.effect = buff_effect
        self.max_level = 1

    def use(self, user, target):
        ret = super().use(user, target)
        if not super().use(user, target):
            return ret
        target.add_effect(self.effect)
        return ret