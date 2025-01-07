import pygame
pygame.init()

from utils.status_bar import StatusBar
from inventory import inventory_logic, inventory_event_handler

class Button:
    def __init__(self, x, y, width, height, color, text='', action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.text = text
        self.action = action

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, self.rect)
        font = pygame.font.Font(None, 36)
        text_surface = font.render(self.text, True, (255, 255, 255))
        surface.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2,
                                    self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def click(self):
        if self.action:
            self.action()

def inventory_screen():
    status_bar.current_screen = "inventory"

def another_screen():
    status_bar.current_screen = "another"

# Initialize buttons
inventory_button = Button(10, 10, 150, 50, (0, 0, 255), 'Inventory', inventory_screen)
another_button = Button(170, 10, 150, 50, (0, 0, 255), 'Another', another_screen)

screen = pygame.display.set_mode((1200, 900))
status_bar = StatusBar(screen, [inventory_button, another_button])
FPS = 60
BG_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        status_bar.handle_event(event)
        if status_bar.current_screen == "inventory":
            inventory_event_handler(event)
    screen.fill(BG_COLOR)
    if status_bar.current_screen == "inventory":
        inventory_logic()
    status_bar.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()