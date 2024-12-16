from utils.bar import Bar

class SpeedBar(Bar):
    def __init__(self, x, y, width, height, max_speed):
        super().__init__(x, y, width, height, max_speed, (128, 128, 128), (0, 0, 255))

    def update_speed(self, delta_time, mysterious_value):
        # Increase the speed based on the elapsed time
        self.update_value(round(delta_time * mysterious_value))