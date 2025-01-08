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

    def show_info(self, surface):
        font = pygame.font.Font(None, 24)
        mouse_pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mouse_pos):
            ability = self.ability
            ability_info = f"Name: {ability.name}\nLevel: {ability.level}\n{ability.get_upgrade_description()}"
            lines = ability_info.split('\n')

            # Calculate the size of the text box
            padding = 5
            max_width = max(font.size(line)[0] for line in lines) + 2 * padding
            total_height = (len(lines) - 1) * font.get_height() + 2 * padding

            # Draw black box
            box_x = mouse_pos[0] + 10
            box_y = mouse_pos[1] + 10
            pygame.draw.rect(surface, (0, 0, 0), (box_x, box_y, max_width, total_height))
            pygame.draw.rect(surface, (255, 255, 255), (box_x, box_y, max_width, total_height), 2)

            # Draw the text
            for i, line in enumerate(lines):
                text_surface = font.render(line, True, (255, 255, 255))
                text_x = box_x + padding
                text_y = box_y + padding + i * font.get_height()
                surface.blit(text_surface, (text_x, text_y))