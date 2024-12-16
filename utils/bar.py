import pygame

class Bar:
    def __init__(self, x, y, width, height, max_value, bg_color, fg_color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.max_value = max_value
        self.current_value = max_value
        self.target_value = max_value
        self.bg_color = bg_color
        self.fg_color = fg_color
        self.decrease_speed = 1

    def draw(self, surface):
        # Calculate the width of the bar based on current value
        value_ratio = self.current_value / self.max_value
        current_width = int(self.width * value_ratio)

        # Draw the background (empty bar)
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.width, self.height))
        # Draw the foreground (current value)
        pygame.draw.rect(surface, self.fg_color, (self.x, self.y, current_width, self.height))

        # Calculate font size based on the height of the bar
        font_size = int(self.height * 1.5)
        font = pygame.font.Font(None, font_size)

        # Render the current value text on the bar
        current_value_text = font.render(f'{self.current_value}', True, (255, 255, 255))
        surface.blit(current_value_text, (self.x + self.width - current_value_text.get_width() - 10, self.y))

        # Render the max value text to the right of the bar
        max_value_text = font.render(f'{self.max_value}', True, (255, 255, 255))
        surface.blit(max_value_text, (self.x + self.width + 10, self.y))

    def update_value(self, amount):
        self.target_value = max(0, min(self.max_value, self.target_value + amount))

    def update(self):
        if self.current_value > self.target_value:
            self.current_value = max(self.target_value, self.current_value - self.decrease_speed)
        elif self.current_value < self.target_value:
            self.current_value = min(self.target_value, self.current_value + self.decrease_speed)