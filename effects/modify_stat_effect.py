from effects.effect import Effect


class ModifyStatEffect(Effect):
    def __init__(self, name, duration, effect, mod_add, mod_mult, mod_true, stats: [str]):
        super().__init__(name, duration, effect)
        self.mod_add = mod_add
        self.mod_mult = mod_mult
        self.mod_true = mod_true
        self.stats = stats

    def apply(self, target):
        for stat in self.stats:
            target.coeffs[stat].additive += self.mod_add
            target.coeffs[stat].multi *= self.mod_mult
            target.coeffs[stat].true += self.mod_true
            target.update_stats()

    def remove(self, target):
        for stat in self.stats:
            target.coeffs[stat].additive -= self.mod_add
            target.coeffs[stat].multi /= self.mod_mult
            target.coeffs[stat].true -= self.mod_true
            target.update_stats()