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
        self.real_value = max_value

    def draw(self, surface):
        # Calculate the width of the bar based on current value
        value_ratio = self.current_value / self.max_value
        current_width = int(self.width * value_ratio)

        # Draw the background (empty bar)
        pygame.draw.rect(surface, self.bg_color, (self.x, self.y, self.width, self.height))
        # Draw the foreground (current value)
        pygame.draw.rect(surface, self.fg_color, (self.x, self.y, current_width, self.height))

    def update_value(self, amount):
        self.real_value = max(0, min(self.max_value, self.real_value + amount))
        self.target_value = round(self.real_value)

    def update(self):
        if self.current_value > self.target_value:
            self.current_value = max(self.target_value, self.current_value - self.decrease_speed / 100 * self.max_value)
        elif self.current_value < self.target_value:
            self.current_value = min(self.target_value, self.current_value + self.decrease_speed / 100 * self.max_value)