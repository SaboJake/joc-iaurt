import math

class AbilityPool:
    def __init__(self, pos, abilities, slot_size):
        self.pos = pos
        self.abilities = abilities
        self.slot_size = slot_size

    def draw(self, surface):
        for i, ability in enumerate(self.abilities):
            x = self.pos[0] + i * (self.slot_size + 10)
            y = self.pos[1]
            surface.blit(ability.image, (x, y))

    def get_ability_at_pos(self, pos):
        for i, ability in enumerate(self.abilities):
            x = self.pos[0] + i * (self.slot_size + 10)
            y = self.pos[1]
            center_x = x + self.slot_size // 2
            center_y = y + self.slot_size // 2
            distance = math.sqrt((pos[0] - center_x) ** 2 + (pos[1] - center_y) ** 2)
            if distance <= self.slot_size // 2:
                return i
        return None