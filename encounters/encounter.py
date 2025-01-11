import random

class Encounter():
    def __init__(self, enemies, money, xp, items=[], drop_chances=[], drop_amount=0):
        self.enemies = enemies
        self.money = money
        self.xp = xp
        self.items = items
        self.drop_chances = drop_chances
        self.drop_amount = drop_amount
        self.dropped_items = self.perform_drops()

    def perform_drops(self):
        dropped_items = []
        for _ in range(self.drop_amount):
            for item, chance in zip(self.items, self.drop_chances):
                if random.random() <= chance:
                    dropped_items.append(item)
                    break
        return dropped_items