
class Ability:
    def __init__(self, name, description, cooldown, cost, target):
        self.name = name
        self.description = description
        self.cooldown = cooldown
        self.cost = cost
        # self, ally, enemy or all
        self.target = target

    def use(self, user, target):
        if user.stats.focus < self.cost:
            return 0
        # if not self.check_valid_target(user, target):
        #     return 0 # gen verific eu sa atace ce trebuie si ma enerva ca voiam sa dea si inamicii heal si se futea
        user.stats.focus -= self.cost
        return 1

    def check_valid_target(self, user, target):
        print(self.target)
        if self.target == 'self' and user != target:
            return False
        if self.target == 'ally' and target.is_enemy:
            return False
        if self.target == 'enemy' and not target.is_enemy:
            return False
        return True