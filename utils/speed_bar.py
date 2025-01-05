from utils.bar import Bar

class SpeedBar(Bar):
    def __init__(self, x, y, width, height, max_speed):
        super().__init__(x, y, width, height, max_speed, (128, 128, 128), (0, 0, 255))
        self.flash_timer = 0
        self.current_value = 0
        self.target_value = 0
        self.real_value = 0

    def draw(self, surface):
        if self.current_value == self.max_value:
            self.flash_timer += 1
            if self.flash_timer % 30 < 15:
                self.fg_color = (127, 127, 255)
            else:
                self.fg_color = (0, 0, 255)
        else:
            self.fg_color = (0, 0, 255)
            self.flash_timer = 0
        super().draw(surface)

    def update_speed(self, value):
        # Increase the speed based on the elapsed time
        self.update_value(value)