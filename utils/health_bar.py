import pygame
from utils.bar import Bar

class HealthBar(Bar):
    def __init__(self, x, y, width, height, max_health, name):
        super().__init__(x, y, width, height, max_health, (255, 0, 0), (0, 255, 0))
        self.name = name

    def draw(self, surface):
        super().draw(surface)

        # Calculate font size based on the height of the bar
        font_size = int(self.height * 1.5)
        font = pygame.font.Font(None, font_size)

        # Render the name text
        name_text = font.render(self.name, True, (255, 255, 255))
        surface.blit(name_text, (self.x, self.y))

        # Render the current value text on the bar
        current_value_text = font.render(f'{self.target_value}', True, (255, 255, 255))
        surface.blit(current_value_text, (self.x + self.width - current_value_text.get_width() - 10, self.y))

        # Render the max value text to the right of the bar
        max_value_text = font.render(f'{self.max_value}', True, (255, 255, 255))
        surface.blit(max_value_text, (self.x + self.width + 10, self.y))
