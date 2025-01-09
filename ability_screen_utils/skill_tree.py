import pygame
import textwrap

from abilities.apply_effect_ability import ApplyEffectAbility
from abilities.basic_attack import BasicAttack
from abilities.ability_sprite import AbilitySprite
from effects.effect_list import Wound
from globals import player_unit

# Define constants
SLOT_SIZE = 40
GRID_OFFSET_X = 100
GRID_OFFSET_Y = 100
GRID_SPACING = 75

PLAYER_INFO_X = 400
PLAYER_INFO_Y = 100
PLAYER_INFO_BOX_WIDTH = 350
PLAYER_INFO_BOX_HEIGHT = 400

coeffs = {
    'strength': 1,
    'intelligence': 1,
    'speed': 1
}

wound_coeffs = {
    'strength': 0.3,
}

wound_effect = Wound("Wound", "Deal damage over time", 3, "physical", True, wound_coeffs, player_unit)

def draw_ability(ability_sprite, surface, x, y):
    surface.blit(ability_sprite.image, (x, y))
    if not ability_sprite.bought:
        ability_sprite.gray_out(surface, x, y)


def draw_prereq(ability_sprite, surface, x, y):
    for prereq in ability_sprite.prereqs:
        color = (255, 255, 0) if prereq.bought else (150, 150, 150)
        pygame.draw.line(surface, color, ability_sprite.rect.center, prereq.rect.center, 4)


class SkillTree:
    def __init__(self, player_unit, ability_pool):
        self.player_unit = player_unit

        self.rows = 5
        self.cols = 4

        self.grid = [[None for _ in range(self.cols)] for _ in range(self.rows)]

        # add abilities to the grid
        ability = BasicAttack(coeffs, "attack", "WHO CARES", 0, 0, "physical", 'sprites/abilities/slash.png')
        wound_ability = ApplyEffectAbility(wound_effect, "Wound", "Applies wound effect", 0, 0, "physical", 'sprites/abilities/slash.png')
        self.grid[0][0] = AbilitySprite(GRID_OFFSET_X + 0 * GRID_SPACING + SLOT_SIZE / 2, GRID_OFFSET_Y + 0 * GRID_SPACING + SLOT_SIZE / 2, SLOT_SIZE, SLOT_SIZE, ability)
        self.grid[0][1] = AbilitySprite(GRID_OFFSET_X + 1 * GRID_SPACING + SLOT_SIZE / 2, GRID_OFFSET_Y + 0 * GRID_SPACING + SLOT_SIZE / 2, SLOT_SIZE, SLOT_SIZE, ability)
        self.grid[1][0] = AbilitySprite(GRID_OFFSET_X + 0 * GRID_SPACING + SLOT_SIZE / 2, GRID_OFFSET_Y + 1 * GRID_SPACING + SLOT_SIZE / 2, SLOT_SIZE, SLOT_SIZE, wound_ability,
                                        prereqs=[self.grid[0][0]])

        self.ability_pool = ability_pool

    def draw_util(self, surface, action):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * GRID_SPACING + GRID_OFFSET_X
                y = row * GRID_SPACING + GRID_OFFSET_Y

                if not self.grid[row][col] is None:
                    action(self.grid[row][col], surface, x, y)

    def draw(self, surface):
        self.draw_util(surface, draw_prereq)
        self.draw_util(surface, draw_ability)

        self.draw_player_info(surface)

    def draw_player_info(self, surface):
        font = pygame.font.Font(None, 36)
        player_info = f"{self.player_unit.name}\nLevel {self.player_unit.level}\nSkill Points: {self.player_unit.skill_points}\nStat points: {self.player_unit.stat_points}"
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

    def buy_ability(self, ability_sprite: AbilitySprite):
        if self.player_unit.skill_points < 1:
            print("Not enough skill points")
            return

        for prereq in ability_sprite.prereqs:
            if not prereq.bought:
                print("Prereqs not met")
                return

        if not ability_sprite.bought:
            ability_sprite.bought = True
            self.player_unit.skill_points -= 1
            self.player_unit.abilities.append(ability_sprite.ability)
            print(f"Bought ability: {ability_sprite.ability.name}")
            new_x, new_y = self.ability_pool.get_next_item_center()
            new = AbilitySprite(new_x, new_y, SLOT_SIZE, SLOT_SIZE, ability_sprite.ability)
            self.ability_pool.abilities.append(new)
            ability_sprite.ability.level += 1
        else:
            if not ability_sprite.ability.ability_upgrade():
                print("Max level reached")
                return
            self.player_unit.skill_points -= 1
            print(f"Upgraded ability: {ability_sprite.ability.name}")

