import pygame

from units.unit import Unit
from utils.health_bar import HealthBar
from utils.speed_bar import SpeedBar


class Enemy:
    def __init__(self, x, y, width, height, max_health, health_x, health_y, max_speed, name, sprite_paths, death_sprite_paths, unit: Unit):
        self.rect = pygame.Rect(x, y, width, height)
        self.health_bar = HealthBar(health_x, health_y, 200, 20, max_health, name)
        self.speed_bar = SpeedBar(x, y - height / 10 - 1, width, height / 10, max_speed)
        self.alive = True
        self.sprites = [pygame.transform.scale(pygame.image.load(path).convert_alpha(),
                                               (width, height)) for path in sprite_paths]
        self.death_sprites = [pygame.transform.scale(pygame.image.load(path).convert_alpha(),
                                                     (width, height)) for path in death_sprite_paths]
        self.current_frame = 0
        self.animation_speed = 0.1
        self.death_animation_done = False
        self.unit = unit

    def draw(self, surface):
        if self.alive:
            self.current_frame = (self.current_frame + self.animation_speed) % len(self.sprites)
            surface.blit(self.sprites[int(self.current_frame)], self.rect.topleft)
            self.health_bar.draw(surface)
            self.speed_bar.draw(surface)
        elif not self.death_animation_done:
            if self.current_frame < len(self.death_sprites) - 1:
                self.current_frame += self.animation_speed
            else:
                self.death_animation_done = True
            surface.blit(self.death_sprites[int(self.current_frame)], self.rect.topleft)

    def update_health(self, amount):
        self.health_bar.update_value(amount)
        if self.health_bar.target_value <= 0:
            self.alive = False
            self.current_frame = 0