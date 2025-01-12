
def same_side(user, target):
    return user.is_enemy() == target.is_enemy()

class Ability:
    def __init__(self, name, description, cooldown, cost, target, sprite_path):
        self.name = name
        self.description = description
        self.cooldown = cooldown
        self.cost = cost
        # self, ally, enemy or all
        self.target = target
        self.sprite_path = sprite_path
        self.level = 0
        self.max_level = 3

    def use(self, user, target):
        if user.current_focus < self.cost:
            return 0
        if not self.check_valid_target(user, target):
             return 0
        user.current_focus -= self.cost
        return 1

    def check_valid_target(self, user, target):
        # print(self.target)
        if self.target == 'self' and user != target:
            return False
        if self.target == 'ally' and not same_side(user, target):
            return False
        if self.target == 'enemy' and  same_side(user, target):
            return False
        return True

    def get_upgrade_description(self):
        return "Amongus"

    def ability_upgrade(self):
        if self.level < self.max_level:
            self.level += 1
            return True
        return False