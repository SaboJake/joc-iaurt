import pygame

from shop import shop_logic, shop_event_handler
from utils.stage import Stage

pygame.init()

from utils.status_bar import StatusBar
from utils.button import Button  # Import the Button class from utils
from inventory import inventory_logic, inventory_event_handler, set_equipment_slots
from ability_screen import ability_screen_logic, ability_screen_event_handler

background_image = pygame.image.load('sprites/backgrounds/stage_background.png')
game_menu_background = pygame.image.load('sprites/backgrounds/game_menu_background.png')

inventory_equipment_slots = {
    "helmet": (100, 200),
    "gloves": (100, 276),
    "weapon1": (176, 352),
    "weapon2": (100, 352),
    "armor": (400, 200),
    "legs": (400, 276),
    "boots": (400, 352),
}

shop_equipment_slots = {
    "helmet": (300, 200),
    "gloves": (300, 276),
    "weapon1": (376, 352),
    "weapon2": (300, 352),
    "armor": (600, 200),
    "legs": (600, 276),
    "boots": (600, 352),
}

def inventory_screen():
    status_bar.current_screen = "inventory"
    set_equipment_slots(inventory_equipment_slots)

def ability_screen():
    status_bar.current_screen = "ability"

def shop_screen():
    status_bar.current_screen = "shop"
    set_equipment_slots(shop_equipment_slots)

stage = None
stage_no = 0

def stage_screen():
    global stage, stage_no
    stage = Stage(stage_no)
    status_bar.current_screen = "stage"

# Initialize buttons
inventory_button = Button(10, 10, 150, 50, (0, 0, 255), 'Inventory', inventory_screen)
ability_button = Button(170, 10, 150, 50, (0, 0, 255), 'Abilities', ability_screen)
# Exit screen button
exit_button = Button(1200 - 150 - 10, 10, 150, 50, (255, 0, 0), 'Exit', lambda: exit_menu())
# Shop button
shop_button = Button(330, 200, 150, 50, (0, 0, 255), 'Shop', shop_screen)
# Next stage button
next_stage_button = Button(660, 200, 150, 50, (0, 0, 255), 'Next Stage', lambda: stage_screen())

def exit_menu():
    status_bar.current_screen = ""

screen = pygame.display.set_mode((1200, 900))
status_bar = StatusBar(screen, [inventory_button, ability_button])
status_bar.current_screen = ""
FPS = 60
BG_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

if __name__ == "__main__":
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            status_bar.handle_event(event)
            if status_bar.current_screen == "inventory":
                inventory_event_handler(event)
            elif status_bar.current_screen == "shop":
                shop_event_handler(event)
            elif status_bar.current_screen == "ability":
                ability_screen_event_handler(event)
            elif status_bar.current_screen == "stage":
                stage.stage_event_handler(event, screen)
        screen.fill(BG_COLOR)

        if status_bar.current_screen == "":
            screen.blit(game_menu_background, (0, 0))
            shop_button.draw(screen)
            next_stage_button.draw(screen)
            status_bar.draw()
        elif status_bar.current_screen == "inventory":
            inventory_logic()
            exit_button.draw(screen)
            status_bar.draw()
        elif status_bar.current_screen == "shop":
            shop_logic()
            exit_button.draw(screen)
            status_bar.draw()
        elif status_bar.current_screen == "ability":
            ability_screen_logic()
            exit_button.draw(screen)
            status_bar.draw()
        elif status_bar.current_screen == "stage":
            ret = stage.update()
            if ret == "victory":
                stage_no += 1
                print("Victory!!")
                status_bar.current_screen = ""
            elif ret == "defeat":
                print("Defeat!!")
                status_bar.current_screen = ""

            screen.blit(background_image, (0, 0))
            stage.draw(screen)

        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()