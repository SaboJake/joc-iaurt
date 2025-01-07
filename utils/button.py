import pygame

class Button():
    def __init__(self, x, y, width, height, color, text='', action=None, hover_action=None, leave_action=None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action
        self.hover_action = hover_action
        self.leave_action = leave_action
        self.clicked = False
        self.hovering = False

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, (self.x + self.width / 2 - text_surface.get_width() / 2,
                                    self.y + self.height / 2 - text_surface.get_height() / 2))

        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if not self.hovering and self.hover_action:
                self.hover_action()
            self.hovering = True

            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        else:
            if self.hovering and self.leave_action:
                self.leave_action()
            self.hovering = False

        if self.clicked and pygame.mouse.get_pressed()[0] == 0:
            self.click()
            self.clicked = False

    def click(self):
        if self.action:
            self.action()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.action()