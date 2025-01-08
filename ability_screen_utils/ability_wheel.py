import math
import pygame

class AbilityWheel:
    def __init__(self, center, radius, num_slots, slot_size):
        self.center = center
        self.radius = radius
        self.num_slots = num_slots
        self.slot_size = slot_size
        self.slots = [None] * num_slots

    def draw(self, surface):
        angle_step = 360 / self.num_slots
        for i in range(self.num_slots):
            angle = angle_step * i
            x = self.center[0] + self.radius * math.cos(math.radians(angle))
            y = self.center[1] + self.radius * math.sin(math.radians(angle))
            pygame.draw.circle(surface, (255, 255, 255), (int(x), int(y)), self.slot_size // 2, 2)
            if self.slots[i]:
                surface.blit(self.slots[i].image, (int(x) - self.slot_size // 2, int(y) - self.slot_size // 2))

    def get_slot_at_pos(self, pos):
        for i in range(self.num_slots):
            angle_step = 360 / self.num_slots
            angle = angle_step * i
            x = self.center[0] + self.radius * math.cos(math.radians(angle))
            y = self.center[1] + self.radius * math.sin(math.radians(angle))
            distance = math.sqrt((pos[0] - x) ** 2 + (pos[1] - y) ** 2)
            if distance <= self.slot_size // 2:
                return i
        return None
