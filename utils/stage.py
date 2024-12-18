import pygame

from utils.button import Button
from utils.enemy import Enemy

enemy_x = [600, 700, 700]
enemy_y = [350, 200, 500]
enemy_width = 150
enemy_height = 150
enemy_health_x = [750, 750, 750]
enemy_health_y = [10, 40, 70]

class Stage:
    def __init__(self, names_array, sprite_paths_array, death_sprite_paths_array):
        enemies = []

        if len(names_array) == 2:
            for i in range(len(names_array)):
                enemies.append(Enemy(enemy_x[i + 1], enemy_y[i + 1], enemy_width, enemy_height, 100, enemy_health_x[i], enemy_health_y[i],100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i]))

        else:
            for i in range(len(names_array)):
                enemies.append(Enemy(enemy_x[i], enemy_y[i], enemy_width, enemy_height, 100, enemy_health_x[i], enemy_health_y[i], 100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i]))

        self.enemies = enemies

        # Temporary buttons for testing
        enemy_buttons = []
        for i in range(len(enemies)):
            enemy_buttons.append(Button(enemy_x[i], enemy_y[i] - 100, 150, 50, (255, 0, 0, 100), f'Damage enemy {i}',
                                        lambda j=i: enemies[j].update_health(-10)))
        self.enemy_buttons = enemy_buttons

    def update(self):
        for enemy in self.enemies:
            enemy.speed_bar.update()
            enemy.health_bar.update()

    def draw(self, surface):
        for enemy in self.enemies:
            enemy.draw(surface)

        # Temporary buttons for testing
        for button in self.enemy_buttons:
            button.draw(surface)

    def all_enemies_dead(self):
        return all(not enemy.alive for enemy in self.enemies)