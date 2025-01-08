import pygame
pygame.init()

from items.display_item import DisplayItem
from items.item import Item
from utils.stats import Stats
from utils.button import Button
from inventory import draw_inventory, draw_money, delete_button, inventory_event_handler, inventory_logic, SLOT_SIZE, \
    OFFSET_X, OFFSET_Y, GRID_ROWS, GRID_COLS, BG_COLOR, money, inventory, selected_item, draw_equipment_background, \
    draw_item_info_logic, draw_item_following_mouse, draw_delete_logic, draw_equipment, unit_equipment, current_unit, \
    set_equipment_slots, draw_item_info, delete_button_pos, DELETE_BUTTON_WIDTH, DELETE_BUTTON_HEIGHT, draw_message, \
    get_selected_item, set_selected_item

for_sale = []

sample_stats = Stats(10, 10, 10, 10, 10)
tricou = DisplayItem(Item("Tricou", "Tricou funny", "armor", sample_stats, 20, 10), "sprites/items/tricou_gucci.png")

for_sale.append(tricou)
for_sale.append(tricou)

EQUIPMENT_SLOTS = {
    "helmet": (300, 200),
    "gloves": (300, 276),
    "weapon1": (376, 352),
    "weapon2": (300, 352),
    "armor": (600, 200),
    "legs": (600, 276),
    "boots": (600, 352),
}

set_equipment_slots(EQUIPMENT_SLOTS)

def draw_items_for_sale(surface, items, pos):
    """Draw the items for sale."""
    x, y = pos
    for item in items:
        item_sprite = pygame.image.load(item.sprite)
        item_sprite = pygame.transform.scale(item_sprite, (SLOT_SIZE, SLOT_SIZE))
        surface.blit(item_sprite, (x, y))
        y += SLOT_SIZE + 10  # Add some space between items


def draw_item_info_with_cost(surface, item, pos):
    """Draw the item information window."""
    font = pygame.font.Font(None, 24)
    info_text = f"{item.name}"
    info_price = f"{item.price} RON"
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
    info_lines = [info_price] + [""] + [info_text] + [""] + stats_info + [""] + [item.description]
    x, y = pos
    padding = 5
    width = max(font.size(line)[0] for line in info_lines) + 2 * padding
    height = len(info_lines) * font.get_height() + 2 * padding

    # Draw background
    pygame.draw.rect(surface, (0, 0, 0), (x, y, width, height))
    pygame.draw.rect(surface, (255, 255, 255), (x, y, width, height), 1)

    # Draw text
    for i, line in enumerate(info_lines):
        color = (255, 255, 0) if i == 0 else (255, 255, 255)  # Make the first line (info_price) yellow
        text_surface = font.render(line, True, color)
        surface.blit(text_surface, (x + padding, y + padding + i * font.get_height()))

sell_message = None

def sell_selected_item():
    global money, sell_message
    if get_selected_item():
        sell_price = get_selected_item().item.price // 2  # Example: sell for half the price
        money += sell_price
        print(f"Sold {get_selected_item().item.name} for {sell_price} RON")
        set_selected_item(None)
        sell_message = None

def display_sell_message():
    global sell_message
    if get_selected_item():
        sell_message = "Sell for " + str(get_selected_item().item.sell_price) + " RON"

def clear_sell_message():
    global sell_message
    sell_message = None

sell_button = Button(
    delete_button_pos[0] - DELETE_BUTTON_WIDTH - 10, delete_button_pos[1], DELETE_BUTTON_WIDTH, DELETE_BUTTON_HEIGHT,
    (255, 255, 0), 'Sell', lambda: sell_selected_item(), display_sell_message, clear_sell_message
)

from inventory import get_selected_item, set_selected_item

def shop_logic():
    global sell_message
    screen.fill(BG_COLOR)
    draw_inventory(screen, inventory, get_selected_item())
    draw_money(screen, money, (OFFSET_X, OFFSET_Y + GRID_ROWS * SLOT_SIZE + 10))
    delete_button.draw(screen)
    sell_button.draw(screen)

    equipment_bg_x, equipment_bg_y = 250, 150
    equipment_bg_width, equipment_bg_height = 500, 300
    draw_equipment_background(screen, equipment_bg_x, equipment_bg_y, equipment_bg_width, equipment_bg_height)

    # Draw the equipment slots for the current unit
    draw_equipment(screen, unit_equipment[current_unit])

    # Draw items for sale below the equipment
    draw_items_for_sale(screen, for_sale, (50, equipment_bg_y + equipment_bg_height + 50))

    draw_item_info_logic()
    draw_item_following_mouse()
    draw_delete_logic()

    if sell_message:
        draw_message(screen, sell_message, (255, 255, 0), pygame.mouse.get_pos())


def shop_event_handler(event):
    global money
    inventory_event_handler(event)
    delete_button.handle_event(event)
    sell_button.handle_event(event)

    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        y_start = 150 + 300 + 50  # equipment_bg_y + equipment_bg_height + 50
        for index, item in enumerate(for_sale):
            item_rect = pygame.Rect(50, y_start + index * (SLOT_SIZE + 10), SLOT_SIZE, SLOT_SIZE)
            if item_rect.collidepoint(mouse_pos):
                if money >= item.item.price and not get_selected_item():
                    money -= item.item.price
                    set_selected_item(DisplayItem(item.item, item.sprite))
                    print(f"Purchased {item.item.name} for {item.item.price} RON")
                else:
                    print("Cannot purchase item")

def shop_item_info_logic():
    mouse_pos = pygame.mouse.get_pos()
    y_start = 150 + 300 + 50  # equipment_bg_y + equipment_bg_height + 50
    for index, item in enumerate(for_sale):
        item_rect = pygame.Rect(50, y_start + index * (SLOT_SIZE + 10), SLOT_SIZE, SLOT_SIZE)
        if item_rect.collidepoint(mouse_pos):
            draw_item_info_with_cost(screen, item.item, mouse_pos)

running = True
clock = pygame.time.Clock()
FPS = 60
screen = pygame.display.set_mode((1200, 900))

if __name__ == "__main__":
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            shop_event_handler(event)
        shop_logic()
        shop_item_info_logic()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()