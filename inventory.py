import pygame

from items.display_item import DisplayItem
from items.item import Item
from units.friendly_unit import FriendlyUnit
from utils.stats import Stats
from utils.button import Button
from globals import friendly_units


# Add sample unit to friendly_units
unit_stats1 = Stats(10, 10, 10, 10, 10)
unit_stats2 = Stats(5, 5, 5, 5, 5)
unit = FriendlyUnit("Player", "Guardian", unit_stats1, unit_stats1)
friendly_units["Player"] = unit
friendly_units["Ally1"] = FriendlyUnit("Ally1", "Combat Medic", unit_stats2, unit_stats2)

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 900
SLOT_SIZE = 64
GRID_ROWS, GRID_COLS = 6, 6
BG_COLOR = (50, 50, 50)
SLOT_COLOR = (100, 100, 100)
ITEM_COLOR = (200, 50, 50)
FPS = 60

# Offset values to move the inventory
OFFSET_X = 800
OFFSET_Y = 100

# Equipment slots
equipment_slots = {
    "helmet": (100, 200),
    "gloves": (100, 276),
    "weapon1": (176, 352),
    "weapon2": (100, 352),
    "armor": (400, 200),
    "legs": (400, 276),
    "boots": (400, 352),
}

def set_equipment_slots(slots):
    global equipment_slots
    equipment_slots = slots

set_equipment_slots(equipment_slots)

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Inventory System")
clock = pygame.time.Clock()

# Inventory setup
inventory = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
selected_item = None  # Holds the selected item
selected_item_pos = None  # Original position of the selected item

def set_selected_item(item):
    global selected_item
    selected_item = item

def get_selected_item():
    global selected_item
    return selected_item

# Fill some slots with items (example data)
sample_stats = Stats(10, 10, 10, 10, 10)
tricou = DisplayItem(Item("Tricou", "Tricou funny", "armor", sample_stats, 0, 0), "sprites/items/tricou_gucci.png")

inventory[0][0] = tricou
inventory[1][1] = tricou
inventory[2][2] = tricou

# Equipment setup
equipment = {slot: None for slot in equipment_slots}

def draw_inventory(surface, inventory, selected_item):
    """Draw the inventory grid and items."""
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            # Draw slot
            x, y = col * SLOT_SIZE + OFFSET_X, row * SLOT_SIZE + OFFSET_Y
            pygame.draw.rect(surface, SLOT_COLOR, (x, y, SLOT_SIZE, SLOT_SIZE), 2)

            # Draw item
            if inventory[row][col]:
                item_sprite = pygame.image.load(inventory[row][col].sprite)
                item_sprite = pygame.transform.scale(item_sprite, (SLOT_SIZE, SLOT_SIZE))
                surface.blit(item_sprite, (x, y))

# Initialize equipment for each unit
unit_equipment = {
    "Player": {slot: None for slot in equipment_slots},
    "Ally1": {slot: None for slot in equipment_slots}
}

def draw_equipment_background(surface, x, y, width, height):
    """Draw the background for the equipment slots."""
    pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height))
    pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height), 2)

def draw_equipment(surface, equipment):
    """Draw the equipment slots and items."""
    for slot, (x, y) in equipment_slots.items():
        # Draw slot
        pygame.draw.rect(surface, SLOT_COLOR, (x, y, SLOT_SIZE, SLOT_SIZE), 2)

        # Draw item
        if equipment[slot]:
            item_sprite = pygame.image.load(equipment[slot].sprite)
            item_sprite = pygame.transform.scale(item_sprite, (SLOT_SIZE, SLOT_SIZE))
            surface.blit(item_sprite, (x, y))

def draw_unit_info(surface, unit, x, y):
    """Draw the unit's name, level, and class above the equipment slots."""
    font = pygame.font.Font(None, 36)
    text = f"{unit.name}\nLvl. {unit.level} {unit.clas}"
    lines = text.split('\n')
    for i, line in enumerate(lines):
        text_surface = font.render(line, True, (255, 255, 255))
        surface.blit(text_surface, (x, y + i * font.get_height()))

def draw_item_info(surface, item, pos):
    """Draw the item information window."""
    font = pygame.font.Font(None, 24)
    info_text = f"{item.name}"
    stats = item.stats
    stats_info = [
        f"Vitality: {stats.vitality}" if stats.vitality != 0 else "",
        f"Strength: {stats.strength}" if stats.strength != 0 else "",
        f"Intelligence: {stats.intelligence}" if stats.intelligence != 0 else "",
        f"Speed: {stats.speed}" if stats.speed != 0 else "",
        f"Focus: {stats.focus}" if stats.focus != 0 else "",
        f"Elemental Piercing: {stats.elemental_piercing}" if stats.elemental_piercing != 0 else "",
        f"Physical Piercing: {stats.physical_piercing}" if stats.physical_piercing != 0 else "",
        f"Elemental Defence: {stats.elemental_defence}" if stats.elemental_defence != 0 else "",
        f"Physical Defence: {stats.physical_defence}" if stats.physical_defence != 0 else "",
    ]
    stats_info = [line for line in stats_info if line]  # Remove empty lines
    info_lines = [info_text] + [""] + stats_info + [""] + [item.description]
    x, y = pos
    padding = 5
    width = max(font.size(line)[0] for line in info_lines) + 2 * padding
    height = len(info_lines) * font.get_height() + 2 * padding

    # Draw background
    pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height))
    pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height), 1)

    # Draw text
    for i, line in enumerate(info_lines):
        text_surface = font.render(line, True, (255, 255, 255))
        surface.blit(text_surface, (x + padding, y + padding + i * font.get_height()))

def draw_message(surface, message, colour, pos):
    """Draw an error message window."""
    font = pygame.font.Font(None, 24)
    x, y = pos
    padding = 5
    width = font.size(message)[0] + 2 * padding
    height = font.get_height() + 2 * padding

    # Draw background
    pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height))
    pygame.draw.rect(surface, colour, (x, y, width, height), 1)

    # Draw text
    text_surface = font.render(message, True, (255, 255, 255))
    surface.blit(text_surface, (x + padding, y + padding))

def get_slot_at_mouse(pos):
    """Get the inventory slot index at a mouse position."""
    x, y = pos
    col, row = (x - OFFSET_X) // SLOT_SIZE, (y - OFFSET_Y) // SLOT_SIZE
    if 0 <= col < GRID_COLS and 0 <= row < GRID_ROWS:
        return row, col
    return None

def get_equipment_slot_at_mouse(pos):
    """Get the equipment slot at a mouse position."""
    x, y = pos
    for slot, (slot_x, slot_y) in equipment_slots.items():
        if slot_x <= x < slot_x + SLOT_SIZE and slot_y <= y < slot_y + SLOT_SIZE:
            return slot
    return None

def draw_player_stats(surface, player):
    """Draw the player's stats in the middle of the screen."""
    font = pygame.font.Font(None, 36)
    stats = player.base_stats
    stats_info = [
        f"Vitality: {stats.vitality}",
        f"Strength: {stats.strength}",
        f"Intelligence: {stats.intelligence}",
        f"Speed: {stats.speed}",
        f"Focus: {stats.focus}",
    ]
    x, y = 650, 200
    padding = 10
    for i, line in enumerate(stats_info):
        text_surface = font.render(line, True, (255, 255, 255))
        surface.blit(text_surface, (x - text_surface.get_width() // 2, y + i * (font.get_height() + padding)))

# Constants for buttons
BUTTON_WIDTH, BUTTON_HEIGHT = 150, 50
BUTTON_COLOR = (0, 0, 255)
BUTTON_TEXT_COLOR = (255, 255, 255)
BUTTON_OFFSET_Y = 450

# Define button positions
player_button_pos = (100, BUTTON_OFFSET_Y)
ally1_button_pos = (300, BUTTON_OFFSET_Y)

DELETE_BUTTON_WIDTH, DELETE_BUTTON_HEIGHT = SLOT_SIZE, SLOT_SIZE
DELETE_BUTTON_COLOR = (255, 0, 0)
# Define button position
delete_button_pos = (OFFSET_X + (GRID_COLS - 1) * SLOT_SIZE, OFFSET_Y + GRID_ROWS * SLOT_SIZE + 10)

def delete_selected_item():
    global selected_item, selected_item_pos
    if selected_item:
        selected_item = None
        selected_item_pos = None
        print("Deleted selected item")

delete_message = None

def display_delete_message():
    global delete_message
    delete_message = "Delete item"

def clear_delete_message():
    global delete_message
    delete_message = None

# Initialize delete button with hover and leave actions
delete_button = Button(
    delete_button_pos[0], delete_button_pos[1], DELETE_BUTTON_WIDTH, DELETE_BUTTON_HEIGHT,
    DELETE_BUTTON_COLOR, 'X', lambda: delete_selected_item(), display_delete_message, clear_delete_message
)

# Initialize buttons using the Button class from utils
player_button = Button(player_button_pos[0], player_button_pos[1], BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, 'Player', lambda: set_current_unit("Player"))
ally1_button = Button(ally1_button_pos[0], ally1_button_pos[1], BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR, 'Ally1', lambda: set_current_unit("Ally1"))

def set_current_unit(unit_name):
    global current_unit
    current_unit = unit_name

from globals import money

running = True
error_message = None
error_message_pos = None
error_message_timer = 0

def regular_slot_logic(slot):
    global selected_item, selected_item_pos
    row, col = slot
    if selected_item is None:
        # Pick up item
        if inventory[row][col]:
            selected_item = inventory[row][col]
            selected_item_pos = (row, col)
            inventory[row][col] = None
            print("Selected item:", selected_item)
    else:
        # Place item
        if inventory[row][col] is None:
            inventory[row][col] = selected_item
            selected_item = None
            selected_item_pos = None
            print("Placed item in slot:", slot)
        else:
            # Swap items
            tmp = inventory[row][col]
            inventory[row][col] = selected_item
            selected_item = tmp
            print("Swapped items:", slot)

def display_error_message():
    global error_message
    if error_message and pygame.time.get_ticks() - error_message_timer < 1000:  # Display for 1 second
        draw_message(screen, error_message, (255, 0, 0), error_message_pos)
    else:
        error_message = None

def inventory_event_handler(event):
    global running, current_unit, selected_item, selected_item_pos, error_message, error_message_pos, error_message_timer
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        slot = get_slot_at_mouse(mouse_pos)
        equipment_slot = get_equipment_slot_at_mouse(mouse_pos)
        print("Slot:", slot, "Equipment Slot:", equipment_slot)
        print("Selected item:", selected_item)
        if slot:
            regular_slot_logic(slot)
        elif equipment_slot:
            if selected_item is None:
                # Pick up item
                if unit_equipment[current_unit][equipment_slot]:
                    selected_item = unit_equipment[current_unit][equipment_slot]
                    unit_equipment[current_unit][equipment_slot] = None
                    friendly_units.get(current_unit).remove_item(selected_item.item)
                    print("Selected item:", selected_item)
            else:
                # Check if equipment slot matches item slot
                if selected_item.item.slot != equipment_slot:
                    error_message = "Incorrect slot"
                    error_message_pos = mouse_pos
                    error_message_timer = pygame.time.get_ticks()
                    print("Cannot equip item in this slot!")
                    return
                # Place item
                if unit_equipment[current_unit][equipment_slot] is None:
                    unit_equipment[current_unit][equipment_slot] = selected_item
                    friendly_units.get(current_unit).add_item(selected_item.item)
                    selected_item = None
                    print("Placed item in equipment slot:", equipment_slot)
                else:
                    # Swap items
                    tmp = unit_equipment[current_unit][equipment_slot]
                    friendly_units.get(current_unit).remove_item(tmp.item)
                    unit_equipment[current_unit][equipment_slot] = selected_item
                    selected_item = tmp
                    friendly_units.get(current_unit).add_item(selected_item.item)
                    print("Swapped items in equipment slot:", equipment_slot)
    player_button.handle_event(event)
    ally1_button.handle_event(event)
    delete_button.handle_event(event)

def draw_money(surface, money, pos):
    """Draw the current money on the screen."""
    font = pygame.font.Font(None, 36)
    text_surface = font.render(f"Money: {money}", True, (255, 255, 0))
    surface.blit(text_surface, pos)

def draw_item_info_logic():
    mouse_pos = pygame.mouse.get_pos()
    slot = get_slot_at_mouse(mouse_pos)
    equipment_slot = get_equipment_slot_at_mouse(mouse_pos)
    if slot and selected_item is None:
        row, col = slot
        if inventory[row][col]:
            draw_item_info(screen, inventory[row][col].item, mouse_pos)
    elif equipment_slot and selected_item is None:
        if unit_equipment[current_unit][equipment_slot]:
            draw_item_info(screen, unit_equipment[current_unit][equipment_slot].item, mouse_pos)

def draw_item_following_mouse():
    global selected_item
    if selected_item:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        item_sprite = pygame.image.load(selected_item.sprite)
        item_sprite = pygame.transform.scale(item_sprite, (SLOT_SIZE, SLOT_SIZE))
        screen.blit(item_sprite, (mouse_x - SLOT_SIZE // 2, mouse_y - SLOT_SIZE // 2))

def draw_delete_logic():
    global delete_message
    if delete_message:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        draw_message(screen, delete_message, (255, 0, 0), (mouse_x - 30, mouse_y))

def inventory_logic():
    global running, current_unit, selected_item, selected_item_pos, error_message, error_message_pos, error_message_timer

    # Draw the inventory grid
    draw_inventory(screen, inventory, selected_item)

    # Draw money value
    draw_money(screen, money, (OFFSET_X, OFFSET_Y + GRID_ROWS * SLOT_SIZE + 10))

    # Draw buttons
    player_button.draw(screen)
    ally1_button.draw(screen)
    delete_button.draw(screen)

    equipment_bg_x, equipment_bg_y = 50, 150
    equipment_bg_width, equipment_bg_height = 500, 300
    draw_equipment_background(screen, equipment_bg_x, equipment_bg_y, equipment_bg_width, equipment_bg_height)

    # Draw unit info above the equipment slots
    draw_unit_info(screen, friendly_units.get(current_unit), equipment_bg_x + 10, equipment_bg_y - 50)

    # Draw the equipment slots for the current unit
    draw_equipment(screen, unit_equipment[current_unit])

    # Draw player stats for the current unit
    draw_player_stats(screen, friendly_units.get(current_unit))

    # Draw money value
    draw_money(screen, money, (OFFSET_X, OFFSET_Y + GRID_ROWS * SLOT_SIZE + 10))
    # Draw item info if hovering over an item and no item is selected
    draw_item_info_logic()

    # Draw the selected item following the mouse
    draw_item_following_mouse()

    # Draw error message if exists
    display_error_message()
    # Draw delete message if hovering over the delete button
    draw_delete_logic()

current_unit = "Player"

if __name__ == "__main__":
    while running:
        screen.fill(BG_COLOR)

        for event in pygame.event.get():
            inventory_event_handler(event)
        inventory_logic()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()