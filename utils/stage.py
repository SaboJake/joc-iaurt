import pygame

from utils.button import Button
from utils.enemy import Enemy
from units.unit import Unit
from units.friendly_unit import FriendlyUnit
from utils.stats import Stats
from abilities.slash_ability import SlashAbility

ally_X = [250, 150, 150]
ally_Y = [350, 200, 500]
ally_width = 150
ally_height = 150
ally_health_X = [100, 100, 100]
ally_health_Y = [10, 40, 70]

enemy_x = [600, 700, 700]
enemy_y = [350, 200, 500]
enemy_width = 150
enemy_height = 150
enemy_health_x = [750, 750, 750]
enemy_health_y = [10, 40, 70]

class Stage:
    def __init__(self, names_array, sprite_paths_array, death_sprite_paths_array):
        # add allies
        allies = []
        ally_units = []
        for i in range(len(names_array)):
            ally_units.append(FriendlyUnit(names_array[i], Stats(10, 10, 10, 50 + i * 5, 10), Stats(10, 10, 10, 50 + i * 5, 10)))
            ally_units[i].abilities.append(SlashAbility())

        # nu uita sa schimbi numele la enemy ca gen e doar unit cu tot cu bari si e stupid
        if len(names_array) == 2:
            for i in range(len(names_array)):
                allies.append(Enemy(ally_X[i + 1], ally_Y[i + 1], ally_width, ally_height, 100, ally_health_X[i], ally_health_Y[i], 100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i], ally_units[i]))

        else:
            for i in range(len(names_array)):
                allies.append(Enemy(ally_X[i], ally_Y[i], ally_width, ally_height, 100, ally_health_X[i], ally_health_Y[i], 100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i], ally_units[i]))

        # add enemies
        enemies = []
        enemy_units = []
        for i in range(len(names_array)):
            enemy_units.append(Unit(names_array[i], Stats(10, 10, 10, 25 + i * 5, 10), Stats(10, 10, 10, 25 + i * 5, 10)))
            enemy_units[i].abilities.append(SlashAbility())

        if len(names_array) == 2:
            for i in range(len(names_array)):
                enemies.append(Enemy(enemy_x[i + 1], enemy_y[i + 1], enemy_width, enemy_height, 100, enemy_health_x[i], enemy_health_y[i],100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i], enemy_units[i]))

        else:
            for i in range(len(names_array)):
                enemies.append(Enemy(enemy_x[i], enemy_y[i], enemy_width, enemy_height, 100, enemy_health_x[i], enemy_health_y[i], 100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i], enemy_units[i]))

        self.enemies = enemies
        self.allies = allies

        # Temporary buttons for testing
        enemy_buttons = []
        for i in range(len(enemies)):
            enemy_buttons.append(Button(enemy_x[i], enemy_y[i] - 100, 150, 50, (255, 0, 0, 100), f'Damage enemy {i}',
                                        lambda j=i: enemies[j].update_health(-10)))
        self.enemy_buttons = enemy_buttons

    def update(self):
        i = 0
        for ally in self.allies:
            i += 1

            # if speed bar is charged, attack
            if ally.speed_bar.target_value == ally.speed_bar.max_value:
                damage_value = ally.unit.abilities[0].hit(ally.unit, self.enemies[0].unit)
                print("ally " + str(i) + " damage " + str(damage_value))
                self.enemies[0].update_health(-damage_value)
                ally.speed_bar.update_value(-ally.speed_bar.max_value)
                if self.enemies[0].health_bar.target_value <= 0:
                    self.enemies.remove(self.enemies[0])

            # if ally is dead, remove it
            if ally.health_bar.target_value <= 0:
                self.allies.remove(ally)
                print("ally " + str(i) + " died")

            # update bars
            ally.speed_bar.update_speed(ally.unit.stats.speed / 50)
            ally.speed_bar.update()
            ally.health_bar.update()

        i = 0
        for enemy in self.enemies:
            i += 1

            # if speed bar is charged, attack
            if enemy.speed_bar.target_value == enemy.speed_bar.max_value:
                damage_value = enemy.unit.abilities[0].hit(enemy.unit, self.allies[0].unit)
                print("enemy " + str(i) + " damage " + str(damage_value))
                self.allies[0].update_health(-damage_value)
                enemy.speed_bar.update_value(-enemy.speed_bar.max_value)
                if self.allies[0].health_bar.target_value <= 0:
                    self.allies.remove(self.allies[0])

            # if enemy is dead, remove it
            if enemy.health_bar.target_value <= 0:
                self.enemies.remove(enemy)
                print("enemy " + str(i) + " died")

            enemy.speed_bar.update_speed(enemy.unit.stats.speed / 50) # speed coeff
            enemy.speed_bar.update()
            enemy.health_bar.update()

    def draw(self, surface):
        for enemy in self.enemies:
            enemy.draw(surface)

        for ally in self.allies:
            ally.draw(surface)

        # Temporary buttons for testing
        for button in self.enemy_buttons:
            button.draw(surface)

    def all_enemies_dead(self):
        return all(not enemy.alive for enemy in self.enemies)