from effects.effect import Effect

# Modify a single stat of the target unit
class ModifyStatEffect(Effect):
    def __init__(self, name, duration, effect, element, can_stack, mod_add, mod_mult, mod_true, stat):
        super().__init__(name, duration, effect, element, can_stack)
        self.mod_add = mod_add
        self.mod_mult = mod_mult
        self.mod_true = mod_true
        self.stat = stat

    def apply(self, target):
        target.coeffs[self.stat].additive += self.mod_add
        target.coeffs[self.stat].multi *= self.mod_mult
        target.coeffs[self.stat].true += self.mod_true
        target.update_stats()

    def remove(self, target):
        target.coeffs[self.stat].additive -= self.mod_add
        target.coeffs[self.stat].multi /= self.mod_mult
        target.coeffs[self.stat].true -= self.mod_true
        target.update_stats()