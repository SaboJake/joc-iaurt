import pygame

from items.display_item import DisplayItem
from items.item import Item
from utils.stats import Stats

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SLOT_SIZE = 64
GRID_ROWS, GRID_COLS = 4, 6
BG_COLOR = (50, 50, 50)
SLOT_COLOR = (100, 100, 100)
ITEM_COLOR = (200, 50, 50)
FPS = 60

# Initialize screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Inventory System")
clock = pygame.time.Clock()

# Inventory setup
inventory = [[None for _ in range(GRID_COLS)] for _ in range(GRID_ROWS)]
selected_item = None  # Holds the selected item
selected_item_pos = None  # Original position of the selected item

# Fill some slots with items (example data)
sample_stats = Stats(10, 10, 10, 10, 10)
tricou = DisplayItem(Item("Tricou", "Tricou funny", sample_stats, 0, 0), "sprites/items/tricou_gucci.png")

inventory[0][0] = tricou
inventory[1][1] = tricou
inventory[2][2] = tricou

def draw_inventory(surface, inventory, selected_item):
    """Draw the inventory grid and items."""
    for row in range(GRID_ROWS):
        for col in range(GRID_COLS):
            # Draw slot
            x, y = col * SLOT_SIZE, row * SLOT_SIZE
            pygame.draw.rect(surface, SLOT_COLOR, (x, y, SLOT_SIZE, SLOT_SIZE), 2)

            # Draw item
            if inventory[row][col]:
                item_sprite = pygame.image.load(inventory[row][col].sprite)
                item_sprite = pygame.transform.scale(item_sprite, (SLOT_SIZE, SLOT_SIZE))
                surface.blit(item_sprite, (x, y))

    # Draw the selected item following the mouse
    if selected_item:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        item_sprite = pygame.image.load(selected_item.sprite)
        item_sprite = pygame.transform.scale(item_sprite, (SLOT_SIZE, SLOT_SIZE))
        surface.blit(item_sprite, (mouse_x - SLOT_SIZE // 2, mouse_y - SLOT_SIZE // 2))

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

def get_slot_at_mouse(pos):
    """Get the inventory slot index at a mouse position."""
    x, y = pos
    col, row = x // SLOT_SIZE, y // SLOT_SIZE
    if 0 <= col < GRID_COLS and 0 <= row < GRID_ROWS:
        return row, col
    return None

running = True
while running:
    screen.fill(BG_COLOR)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            slot = get_slot_at_mouse(mouse_pos)
            print("Slot:", slot)
            if slot:
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

    # Draw the inventory grid
    draw_inventory(screen, inventory, selected_item)

    # Draw item info if hovering over an item and no item is selected
    mouse_pos = pygame.mouse.get_pos()
    slot = get_slot_at_mouse(mouse_pos)
    if slot and selected_item is None:
        row, col = slot
        if inventory[row][col]:
            draw_item_info(screen, inventory[row][col].item, mouse_pos)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()