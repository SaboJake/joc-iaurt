import pygame

class StatusBar:
    def __init__(self, screen, buttons):
        self.screen = screen
        self.buttons = buttons
        self.current_screen = None
        self.current_screen_event = None

    def draw(self):
        for button in self.buttons:
            button.draw(self.screen)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for button in self.buttons:
                if button.rect.collidepoint(mouse_pos):
                    # self.current_screen = button.action
                    button.click()