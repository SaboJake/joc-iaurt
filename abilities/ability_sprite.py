import pygame

class AbilitySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, ability):
        super().__init__()
        self.image = pygame.image.load(ability.sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect(center=(x, y))
        self.ability = ability
        self.bought = False
        mask = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.ellipse(mask, (255, 255, 255, 255), mask.get_rect())

        # Apply the mask to the image
        self.image = self.image.copy()
        self.image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)


    def gray_out(self, surface, x, y):
        gray_image = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        gray_image.fill((0, 0, 0, 150))
        surface.blit(gray_image, (x, y))
        mask = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.ellipse(mask, (255, 255, 255, 255), mask.get_rect())

        # Apply the mask to the image
        gray_image = gray_image.copy()
        gray_image.blit(mask, (0, 0), special_flags=pygame.BLEND_RGBA_MIN)