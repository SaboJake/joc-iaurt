import pygame

from abilities.basic_attack import BasicAttack
from abilities.ability_sprite import AbilitySprite

coeffs = {
    'strength': 1,
    'intelligence': 1,
    'speed': 1
}

class SkillTree:
    def __init__(self, player_unit):
        self.player_unit = player_unit

        self.rows = 5
        self.cols = 4

        self.grid = []
        for i in range(5):
            abilities_row = []
            for j in range(4):
                if (i == 0 and j == 0) or (i == 0 and j == 2) or (i == 1 and j == 0):
                    ability = BasicAttack(coeffs, "attack", "WHO CARES", 0, 0, "physical", 'sprites/abilities/slash.png')
                    abilities_row.append(AbilitySprite(0, 0, 50, 50, (255, 0, 0, 100), ability, 'sprites/abilities/slash.png'))
                else:
                    abilities_row.append(None)
            self.grid.append(abilities_row)

        self.selected_ability = None

    def draw(self, surface):
        for row in range(self.rows):
            for col in range(self.cols):
                x = col * 60 + 100
                y = row * 60 + 100
                pygame.draw.rect(surface, (255, 255, 255), (x, y, 50, 50), 2)

                if not self.grid[row][col] is None:
                    # if not self.grid[row][col].bought:
                    #     self.grid[row][col].gray_out(surface, x, y)
                    surface.blit(self.grid[row][col].image, (x, y))

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            col = (mouse_pos[0] - 100) // 60
            row = (mouse_pos[1] - 100) // 60
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
        else:
            print("Not enough skill points or ability already bought")
