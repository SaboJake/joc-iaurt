import pygame

class AbilitySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, ability, sprite_path):
        super().__init__()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.ability = ability