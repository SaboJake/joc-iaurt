import textwrap

import pygame

MAX_BOX_WIDTH = 200

class AbilitySprite(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, ability, prereqs=[]):
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

        self.prereqs = prereqs

    def __getstate__(self):
        state = self.__dict__.copy()
        # Remove the image from the state
        del state['image']
        return state

    def __setstate__(self, state):
        self.__dict__.update(state)
        # Recreate the image (you may need to adjust this part based on your needs)
        self.image = pygame.image.load(self.ability.sprite_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))
        mask = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.ellipse(mask, (255, 255, 255, 255), mask.get_rect())
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
            ability_info = f"Name: {ability.name}\nLevel: {ability.level} / {ability.max_level}\n{ability.description}\n{self.get_ability_stats()}"
            lines = ability_info.split('\n')

            # Wrap lines to fit within MAX_BOX_WIDTH
            wrapped_lines = []
            for line in lines:
                wrapped_lines.extend(textwrap.wrap(line, width=MAX_BOX_WIDTH // font.size('A')[0]))

            # Calculate the size of the text box
            padding = 5
            max_width = min(MAX_BOX_WIDTH, max(font.size(line)[0] for line in wrapped_lines) + 2 * padding)
            total_height = len(wrapped_lines) * font.get_height() + 2 * padding

            # Draw black box
            box_x = mouse_pos[0] + 10
            box_y = mouse_pos[1] + 10
            pygame.draw.rect(surface, (0, 0, 0), (box_x, box_y, max_width, total_height))
            pygame.draw.rect(surface, (255, 255, 255), (box_x, box_y, max_width, total_height), 2)

            # Draw the text
            text_x = box_x + padding
            for i, line in enumerate(wrapped_lines):
                text_surface = font.render(line, True, (255, 255, 255))
                text_y = box_y + padding + i * font.get_height()
                surface.blit(text_surface, (text_x, text_y))

            # if text_x > 500:
            #     return

            # If the ability is bought, show the upgrade info
            if self.bought and ability.level < ability.max_level:
                upgrade_info = ability.get_upgrade_description()
                upgrade_lines = upgrade_info.split('\n')

                # Wrap lines to fit within MAX_BOX_WIDTH
                wrapped_upgrade_lines = []
                for line in upgrade_lines:
                    wrapped_upgrade_lines.extend(textwrap.wrap(line, width=MAX_BOX_WIDTH // font.size('A')[0]))

                # Calculate the size of the upgrade text box
                upgrade_max_width = min(MAX_BOX_WIDTH,
                                        max(font.size(line)[0] for line in wrapped_upgrade_lines) + 2 * padding)
                upgrade_total_height = len(wrapped_upgrade_lines) * font.get_height() + 2 * padding

                # Draw black box for upgrade info
                upgrade_box_x = box_x + max_width - 2
                upgrade_box_y = box_y
                pygame.draw.rect(surface, (0, 0, 0),
                                 (upgrade_box_x, upgrade_box_y, upgrade_max_width, upgrade_total_height))
                pygame.draw.rect(surface, (255, 255, 255),
                                 (upgrade_box_x, upgrade_box_y, upgrade_max_width, upgrade_total_height), 2)

                # Draw the upgrade text
                for i, line in enumerate(wrapped_upgrade_lines):
                    text_surface = font.render(line, True, (255, 255, 255))
                    text_x = upgrade_box_x + padding
                    text_y = upgrade_box_y + padding + i * font.get_height()
                    surface.blit(text_surface, (text_x, text_y))

    def get_ability_stats(self):
        if hasattr(self.ability, 'coeffs'):
            return f"Strength: {self.ability.coeffs['strength']}\nIntelligence: {self.ability.coeffs['intelligence']}\nSpeed: {self.ability.coeffs['speed']}"
        return ""
