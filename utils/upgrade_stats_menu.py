import pygame
from utils.button import Button

from globals import player_unit

# Constants for the stats box
STATS_BOX_X = 400
STATS_BOX_Y = 550
STATS_BOX_WIDTH = 350
STATS_BOX_HEIGHT = 200
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 25
BUTTON_PADDING = 10

upgrade_buttons = {
    'vitality': Button(STATS_BOX_X + BUTTON_PADDING, STATS_BOX_Y + BUTTON_PADDING, BUTTON_WIDTH, BUTTON_HEIGHT, (0, 255, 0), 'Upgrade', lambda: upgrade_stat('vitality')),
    'strength': Button(STATS_BOX_X + BUTTON_PADDING, STATS_BOX_Y + 2 * BUTTON_PADDING + BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, (0, 255, 0), 'Upgrade', lambda: upgrade_stat('strength')),
    'intelligence': Button(STATS_BOX_X + BUTTON_PADDING, STATS_BOX_Y + 3 * BUTTON_PADDING + 2 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, (0, 255, 0), 'Upgrade', lambda: upgrade_stat('intelligence')),
    'speed': Button(STATS_BOX_X + BUTTON_PADDING, STATS_BOX_Y + 4 * BUTTON_PADDING + 3 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, (0, 255, 0), 'Upgrade', lambda: upgrade_stat('speed')),
    'focus': Button(STATS_BOX_X + BUTTON_PADDING, STATS_BOX_Y + 5 * BUTTON_PADDING + 4 * BUTTON_HEIGHT, BUTTON_WIDTH, BUTTON_HEIGHT, (0, 255, 0), 'Upgrade', lambda: upgrade_stat('focus'))
}

def draw_stats_box(surface):
    font = pygame.font.Font(None, 40)
    stats = player_unit.base_stats
    stats_info = [
        f"Vitality: {stats.vitality}",
        f"Strength: {stats.strength}",
        f"Intelligence: {stats.intelligence}",
        f"Speed: {stats.speed}",
        f"Focus: {stats.focus}"
    ]

    pygame.draw.rect(surface, (0, 0, 0), (STATS_BOX_X, STATS_BOX_Y, STATS_BOX_WIDTH, STATS_BOX_HEIGHT))
    pygame.draw.rect(surface, (255, 255, 255), (STATS_BOX_X, STATS_BOX_Y, STATS_BOX_WIDTH, STATS_BOX_HEIGHT), 2)

    for i, line in enumerate(stats_info):
        text_surface = font.render(line, True, (255, 255, 255))
        text_x = STATS_BOX_X + BUTTON_PADDING + BUTTON_WIDTH + BUTTON_PADDING
        text_y = STATS_BOX_Y + BUTTON_PADDING + i * (font.get_height() + BUTTON_PADDING)
        surface.blit(text_surface, (text_x, text_y))
        button_y = text_y + (font.get_height() - BUTTON_HEIGHT) // 2
        upgrade_buttons[list(upgrade_buttons.keys())[i]].rect.y = button_y
        upgrade_buttons[list(upgrade_buttons.keys())[i]].y = button_y
        upgrade_buttons[list(upgrade_buttons.keys())[i]].draw(surface)


def upgrade_stat(stat):
    if player_unit.stat_points > 0:
        setattr(player_unit.base_stats, stat, getattr(player_unit.base_stats, stat) + 1)
        player_unit.stat_points -= 1
        player_unit.update_stats()