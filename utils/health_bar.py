import pygame

class HealthBar:
    def __init__(self, x, y, width, height, max_health, name):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_health = max_health
        self.current_health = max_health
        self.name = name

    def draw(self, surface):
        # Calculate the width of the health bar based on current health
        health_ratio = self.current_health / self.max_health
        current_width = int(self.width * health_ratio)

        # Draw the background (empty health bar)
        pygame.draw.rect(surface, (255, 0, 0), (self.x, self.y, self.width, self.height))
        # Draw the foreground (current health)
        pygame.draw.rect(surface, (0, 255, 0), (self.x, self.y, current_width, self.height))

        # Render the current health text on the health bar
        font = pygame.font.Font(None, 24)
        current_health_text = font.render(f'{self.current_health}', True, (255, 255, 255))
        surface.blit(current_health_text, (self.x + self.width - current_health_text.get_width() - 10, self.y))

        # Render the max health text to the right of the health bar
        max_health_text = font.render(f'{self.max_health}', True, (255, 255, 255))
        surface.blit(max_health_text, (self.x + self.width + 10, self.y))

        # Render the name text
        name_text = font.render(self.name, True, (255, 255, 255))
        surface.blit(name_text, (self.x, self.y))

    def update_health(self, amount):
        self.current_health = max(0, min(self.max_health, self.current_health + amount))