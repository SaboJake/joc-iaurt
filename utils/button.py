import pygame

class Button():
    def __init__(self, x, y, width, height, color, text='', action=None, hover_action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action
        self.hover_action = hover_action
        self.clicked = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        pygame.draw.rect(surface, self.color, self.rect)
        text_surface = font.render(self.text, True, (255, 255, 255))
        if len(self.color) == 4:
            text_surface.set_alpha(self.color[3])
        surface.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2, self.y + self.height / 2 - text_surface.get_height() / 2))

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
            if self.hover_action:
                self.hover_action()
        
        if self.clicked and pygame.mouse.get_pressed()[0] == 0:
            self.click()
            self.clicked = False
            

    def click(self):
        if self.action:
            self.action()