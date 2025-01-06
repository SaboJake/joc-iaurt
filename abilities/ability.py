
class Ability:
    def __init__(self, name, description, cooldown, cost, target):
        self.name = name
        self.description = description
        self.cooldown = cooldown
        self.cost = cost
        # self, ally, enemy or all
        self.target = target