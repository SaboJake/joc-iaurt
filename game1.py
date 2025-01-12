import random

import pygame

from encounters.encounter_list import encounters
from end_battle_screen import EndBattleScreen
from globals import player_unit, money, add_money, get_money, set_save_data, get_save_data, set_money
from items.display_item import DisplayItem
from items.item import Item
from save import save_variables, load_variables
from shop import shop_logic, shop_event_handler
from utils.stage import Stage
from utils.stats import Stats
from globals import save_data

pygame.init()

from utils.status_bar import StatusBar
from utils.button import Button
from inventory import inventory_logic, inventory_event_handler, set_equipment_slots, update_save_data_inventory, \
    get_save_data_inventory
from ability_screen import ability_screen_logic, ability_screen_event_handler, update_save_data_abilities, \
    get_save_data_abilities

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

def save():
    new_save_data = {}
    new_save_data["money"] = get_money()
    new_save_data["stage_no"] = stage_no
    update_save_data_inventory(new_save_data)
    update_save_data_abilities(new_save_data)
    save_variables(new_save_data, "save_data")
    set_save_data(new_save_data)

def load():
    global stage_no
    set_save_data(load_variables("save_data"))
    set_money(get_save_data()["money"])
    stage_no = get_save_data()["stage_no"]
    get_save_data_inventory(get_save_data())
    get_save_data_abilities(get_save_data())

# Initialize buttons
inventory_button = Button(10, 10, 150, 50, (0, 0, 255), 'Inventory', inventory_screen)
ability_button = Button(170, 10, 150, 50, (0, 0, 255), 'Abilities', ability_screen)
save_button = Button(330, 10, 150, 50, (0, 0, 255), 'Save', save)
load_button = Button(490, 10, 150, 50, (0, 0, 255), 'Load', load)
# Exit screen button
exit_button = Button(1200 - 150 - 10, 10, 150, 50, (255, 0, 0), 'Exit', lambda: exit_menu())
# Shop button
shop_button = Button(330, 200, 150, 50, (0, 0, 255), 'Shop', shop_screen)
# Next stage button
next_stage_button = Button(660, 200, 150, 50, (0, 0, 255), 'Next Stage', lambda: stage_screen())

def exit_menu():
    status_bar.current_screen = ""

screen = pygame.display.set_mode((1200, 900))
status_bar = StatusBar(screen, [inventory_button, ability_button, save_button, load_button])
status_bar.current_screen = ""
FPS = 60
BG_COLOR = (0, 0, 0)
clock = pygame.time.Clock()

# Battle end screen for testing
sample_stats = Stats(10, 10, 10, 10, 10)
tricou1 = DisplayItem(Item("Tricou", "Tricou funny", "armor", sample_stats, 0, 0), "sprites/items/tricou_gucci.png")
tricou2 = DisplayItem(Item("Tricou", "Tricou funny", "armor", sample_stats, 0, 0), "sprites/items/tricou_gucci.png")

end_battle_screen = None

def set_end_battle_screen():
    global end_battle_screen, stage_no, money

    encounters[stage_no].perform_drops()
    end_battle_screen = EndBattleScreen(screen, [], encounters[stage_no].xp, encounters[stage_no].money, encounters[stage_no].dropped_items)
    player_unit.gain_xp(encounters[stage_no].xp)
    # add_money(encounters[stage_no].money)
    money += encounters[stage_no].money
    end_battle_screen.xp_bar.update_value(encounters[stage_no].xp)

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
            elif status_bar.current_screen == "end_battle":
                end_battle_screen.end_battle_handle_event(event)
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
                set_end_battle_screen()
                stage_no += 1
                print("Victory!!")
                status_bar.current_screen = "end_battle"
            elif ret == "defeat":
                print("Defeat!!")
                status_bar.current_screen = ""

            screen.blit(background_image, (0, 0))
            stage.draw(screen)
        elif status_bar.current_screen == "end_battle":
            end_battle_screen.end_battle_screen_logic()
            exit_button.draw(screen)
            status_bar.draw()
        pygame.display.flip()
        clock.tick(FPS)

pygame.quit()