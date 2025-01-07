import pygame
pygame.init()

from utils.status_bar import StatusBar
from utils.button import Button  # Import the Button class from utils
from inventory import inventory_logic, inventory_event_handler

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