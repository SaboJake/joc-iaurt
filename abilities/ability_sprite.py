import pygame

class AbilitySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, ability, sprite_path):
        super().__init__()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.ability = ability
        self.bought = False

    def gray_out(self, surface):
        gray_image = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        gray_image.fill((100, 100, 100, 150))  # Adjust the alpha value to make it more transparent
        surface.blit(gray_image, self.rect)