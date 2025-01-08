import pygame
import textwrap

from abilities.basic_attack import BasicAttack
from abilities.ability_sprite import AbilitySprite

# Define constants
SLOT_SIZE = 40
GRID_OFFSET_X = 100
GRID_OFFSET_Y = 100
GRID_SPACING = 75

PLAYER_INFO_X = 400
PLAYER_INFO_Y = 100
PLAYER_INFO_BOX_WIDTH = 200
PLAYER_INFO_BOX_HEIGHT = 600

coeffs = {
    'strength': 1,
    'intelligence': 1,
    'speed': 1
}

class SkillTree:
    def __init__(self, player_unit, ability_pool):
        self.player_unit = player_unit

        self.rows = 5
        self.cols = 4

        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        # add abilities to the grid
        ability = BasicAttack(coeffs, "attack", "WHO CARES", 0, 0, "physical", 'sprites/abilities/slash.png')
        self.grid[0][0] = AbilitySprite(GRID_OFFSET_X + 0 * GRID_SPACING + SLOT_SIZE / 2, GRID_OFFSET_Y + 0 * GRID_SPACING + SLOT_SIZE / 2, SLOT_SIZE, SLOT_SIZE, ability)
        self.grid[0][1] = AbilitySprite(GRID_OFFSET_X + 1 * GRID_SPACING + SLOT_SIZE / 2, GRID_OFFSET_Y + 0 * GRID_SPACING + SLOT_SIZE / 2, SLOT_SIZE, SLOT_SIZE, ability)
        self.grid[1][0] = AbilitySprite(GRID_OFFSET_X + 0 * GRID_SPACING + SLOT_SIZE / 2, GRID_OFFSET_Y + 1 * GRID_SPACING + SLOT_SIZE / 2, SLOT_SIZE, SLOT_SIZE, ability)

        self.ability_pool = ability_pool

    def draw(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * GRID_SPACING + GRID_OFFSET_X
                y = row * GRID_SPACING + GRID_OFFSET_Y

                if not self.grid[row][col] is None:
                    # pygame.draw.rect(surface, (255, 255, 255), (x, y, SLOT_SIZE, SLOT_SIZE), 2)
                    surface.blit(self.grid[row][col].image, (x, y))
                    if not self.grid[row][col].bought:
                        self.grid[row][col].gray_out(surface, x, y)

                    # self.grid[row][col].show_info(surface)

        self.draw_player_info(surface)

    def draw_player_info(self, surface):
        font = pygame.font.Font(None, 36)
        player_info = f"{self.player_unit.name}\nLevel {self.player_unit.level}"
        lines = player_info.split('\n')

        # Draw the black box with a white outline
        pygame.draw.rect(surface, (0, 0, 0),
                         (PLAYER_INFO_X, PLAYER_INFO_Y, PLAYER_INFO_BOX_WIDTH, PLAYER_INFO_BOX_HEIGHT))
        pygame.draw.rect(surface, (255, 255, 255),
                         (PLAYER_INFO_X, PLAYER_INFO_Y, PLAYER_INFO_BOX_WIDTH, PLAYER_INFO_BOX_HEIGHT), 2)

        # Draw the text centered
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, (255, 255, 255))
            text_x = PLAYER_INFO_X + (PLAYER_INFO_BOX_WIDTH - text_surface.get_width()) // 2
            text_y = PLAYER_INFO_Y + 10 + i * font.get_height()
            surface.blit(text_surface, (text_x, text_y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            col = (mouse_pos[0] - GRID_OFFSET_X) // GRID_SPACING
            row = (mouse_pos[1] - GRID_OFFSET_Y) // GRID_SPACING
            if 0 <= row < self.rows and 0 <= col < self.cols:
                self.selected_ability = self.grid[row][col]
                if self.selected_ability:
                    self.buy_ability(self.selected_ability)

    def buy_ability(self, ability_sprite):
        if not ability_sprite.bought and self.player_unit.skill_points >= 1:
            ability_sprite.bought = True
            self.player_unit.skill_points -= 1
            self.player_unit.abilities.append(ability_sprite.ability)
            print(f"Bought ability: {ability_sprite.ability.name}")
            new_x, new_y = self.ability_pool.get_next_item_center()
            new = AbilitySprite(new_x, new_y, SLOT_SIZE, SLOT_SIZE, ability_sprite.ability)
            self.ability_pool.abilities.append(new)
        else:
            print("Not enough skill points or ability already bought")

