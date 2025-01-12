import math

class AbilityPool:
    def __init__(self, pos, abilities, slot_size):
        self.pos = pos
        self.abilities = abilities
        self.slot_size = slot_size

    def draw(self, surface):
        max_per_row = 6
        for i, ability in enumerate(self.abilities):
            row = i // max_per_row
            col = i % max_per_row
            x = self.pos[0] + col * (self.slot_size + 10)
            y = self.pos[1] + row * (self.slot_size + 10)
            surface.blit(ability.image, (x, y))

    def get_ability_at_pos(self, pos):
        max_per_row = 6
        for i, ability in enumerate(self.abilities):
            row = i // max_per_row
            col = i % max_per_row
            x = self.pos[0] + col * (self.slot_size + 10)
            y = self.pos[1] + row * (self.slot_size + 10)
            center_x = x + self.slot_size // 2
            center_y = y + self.slot_size // 2
            distance = math.sqrt((pos[0] - center_x) ** 2 + (pos[1] - center_y) ** 2)
            if distance <= self.slot_size // 2:
                return i
        return None

    def get_next_item_center(self):
        max_per_row = 6
        next_index = len(self.abilities)
        row = next_index // max_per_row
        col = next_index % max_per_row
        center_x = self.pos[0] + col * (self.slot_size + 10) + self.slot_size // 2
        center_y = self.pos[1] + row * (self.slot_size + 10) + self.slot_size // 2
        return center_x, center_y

    def update_save_data(self, save_data):
        save_data["ability_pool_abilities"] = self.abilities

    def get_save_data(self, save_data):
        self.abilities = save_data["ability_pool_abilities"]