from math import floor

import pygame

from combat_hud.display_effect import DisplayEffect
from units.unit import Unit
from utils.health_bar import HealthBar
from utils.speed_bar import SpeedBar
from utils.focus_bar import FocusBar

BAR_HEIGHT = 20
BOX_WIDTH = 50

EFFECT_HEIGHT = 50
EFFECT_WIDTH = 20

from constants import HEALTH_CONSTANT

class DisplayUnit:
    def __init__(self, x, y, width, height, health_x, health_y, max_speed, name, sprite_paths, death_sprite_paths, unit: Unit):
        self.rect = pygame.Rect(x, y, width, height)
        self.health_bar = HealthBar(health_x, health_y, 200, BAR_HEIGHT, HEALTH_CONSTANT * getattr(unit.stats, 'vitality'), name)
        self.focus_bar = FocusBar(health_x, health_y + BAR_HEIGHT, 200, BAR_HEIGHT, getattr(unit.stats, 'focus'), "")
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

        self.health_x = health_x
        self.health_y = health_y

        self.effects = []

    def draw(self, surface):
        if self.alive:
            self.health_bar.max_value = HEALTH_CONSTANT * getattr(self.unit.stats, 'vitality')
            self.update_health(floor(self.unit.health - self.health_bar.target_value))

            # box to the right of the bars
            box_rect = pygame.Rect(self.health_bar.x + self.health_bar.width, self.health_bar.y, BOX_WIDTH, BAR_HEIGHT * 2)
            pygame.draw.rect(surface, (0, 0, 0), box_rect)
            # pygame.draw.rect(surface, (255, 255, 255), box_rect, 1)

            self.current_frame = (self.current_frame + self.animation_speed) % len(self.sprites)
            surface.blit(self.sprites[int(self.current_frame)], self.rect.topleft)
            self.health_bar.draw(surface)
            self.focus_bar.draw(surface)
            self.speed_bar.draw(surface)

            for effect in self.effects:
                effect.draw(surface)
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

    def get_next_position(self, last_x):
        if self.unit.is_enemy():
            return last_x - EFFECT_WIDTH
        return last_x + EFFECT_WIDTH

    def update_effects(self):
        new_effects = []
        last_x = self.health_x - EFFECT_WIDTH
        last_y = self.health_y
        for effects in self.unit.effects:
            if effects.duration <= 0:
                continue
            new_effects.append(DisplayEffect(effects, last_x, last_y, EFFECT_WIDTH, EFFECT_HEIGHT))
            last_x = self.get_next_position(last_x)
        self.effects = new_effects