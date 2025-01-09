import pygame


class DisplayEffect:
    def __init__(self, effect, x, y, width, height):
        self.effect = effect
        self.rect = pygame.Rect(x, y, width, height)
        self.color = (255, 0, 0)
        self.font = pygame.font.Font(None, 24)
        self.hover_font = pygame.font.Font(None, 36)

    def draw(self, surface):
        # Draw the effect rectangle
        pygame.draw.rect(surface, self.color, self.rect)

        # Draw the duration inside the rectangle
        duration_text = self.font.render(str(self.effect.duration), True, (255, 255, 255))
        text_rect = duration_text.get_rect(center=self.rect.center)
        surface.blit(duration_text, text_rect)

    def draw_hover_info(self, surface):
        # Create a surface for the hover info
        hover_surface = pygame.Surface((200, 100))
        hover_surface.fill((0, 0, 0))
        pygame.draw.rect(hover_surface, (255, 255, 255), hover_surface.get_rect(), 2)

        # Render the name and description
        name_text = self.hover_font.render(self.effect.name, True, (255, 255, 255))
        description_text = self.font.render(self.effect.description, True, (255, 255, 255))

        # Blit the text onto the hover surface
        hover_surface.blit(name_text, (10, 10))
        hover_surface.blit(description_text, (10, 50))

        # Blit the hover surface onto the main surface
        surface.blit(hover_surface, (self.rect.x + self.rect.width + 10, self.rect.y))