import random

import pygame

from abilities.basic_attack import BasicAttack
from abilities.basic_heal import BasicHeal
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

coeffs = {
    'strength': 1,
    'intelligence': 1,
    'speed': 1
}

class Stage:
    def __init__(self, names_array, sprite_paths_array, death_sprite_paths_array):
        # add allies
        allies = []
        ally_units = []
        for i in range(len(names_array)):
            ally_units.append(FriendlyUnit(names_array[i], Stats(10, 10, 10, 25 + i * 6, 10), Stats(10, 10, 10, 25 + i * 5, 10)))
            ally_units[i].abilities.append(BasicAttack(coeffs, "WHO", "CARES", 0, 0, "physical"))
            ally_units[i].abilities.append(BasicHeal(coeffs, "WHO", "CARES", 0, 0, "physical"))

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
            enemy_units[i].abilities.append(BasicAttack(coeffs, "WHO", "CARES", 0, 0, "physical"))
            enemy_units[i].abilities.append(BasicHeal(coeffs, "WHO", "CARES", 0, 0, "physical"))

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

        self.delay = 0
        self.choosing_ability = False
        self.end_turn_button = Button(475, 650, 50, 50, (255, 0, 0, 100), 'End Turn', lambda: setattr(self, 'choosing_ability', False))

    def ally_action(self, ally):

        # if other allies are low on health, help them
        target = None
        for j in range(len(self.allies)):
            if self.allies[j] != ally and self.allies[j].health_bar.target_value < self.allies[j].health_bar.max_value / 2:
                target = self.allies[j]
                break

        if target is not None:
            # found a target, heal it
            # random heal ability
            ability = ally.unit.abilities[random.randint(0, len(ally.unit.abilities) - 1)]
            while ability.target != "ally":
                ability = ally.unit.abilities[random.randint(0, len(ally.unit.abilities) - 1)]

            heal_value = ability.use(ally.unit, target.unit)
            print("ally " + str(ally) + " heal " + str(heal_value))
            target.update_health(heal_value)

        else:
            # random attack ability
            ability = ally.unit.abilities[random.randint(0, len(ally.unit.abilities) - 1)]
            while ability.target != "enemy":
                ability = ally.unit.abilities[random.randint(0, len(ally.unit.abilities) - 1)]

            # random target
            target = self.enemies[random.randint(0, len(self.enemies) - 1)]
            damage_value = ability.use(ally.unit, target.unit)
            print("ally " + str(ally) + " damage " + str(damage_value))
            target.update_health(-damage_value)
            if target.health_bar.target_value <= 0:
                self.enemies.remove(target)

    def enemy_action(self, enemy):

        # if other enemies are low on health, help them (50% chance)
        target = None
        for j in range(len(self.enemies)):
            if self.enemies[j] != enemy and self.enemies[j].health_bar.target_value < self.enemies[j].health_bar.max_value / 2 and random.randint(0, 1) == 0:
                target = self.enemies[j]
                break

        # found a target, heal it
        if target is not None:
            ability = enemy.unit.abilities[random.randint(0, len(enemy.unit.abilities) - 1)]
            while ability.target != "ally":
                ability = enemy.unit.abilities[random.randint(0, len(enemy.unit.abilities) - 1)]

            heal_value = ability.use(enemy.unit, target.unit)
            print("enemy " + str(enemy) + " heal " + str(heal_value))
            target.update_health(heal_value)

        else:
            # random attack ability
            ability = enemy.unit.abilities[random.randint(0, len(enemy.unit.abilities) - 1)]
            while ability.target != "enemy":
                ability = enemy.unit.abilities[random.randint(0, len(enemy.unit.abilities) - 1)]

            # random target
            target = self.allies[random.randint(0, len(self.allies) - 1)]
            damage_value = ability.use(enemy.unit, target.unit)
            print("ally " + str(enemy) + " damage " + str(damage_value))
            target.update_health(-damage_value)
            if target.health_bar.target_value <= 0:
                self.allies.remove(target)

    def update(self):
        for ally in self.allies:
            ally.speed_bar.update()
            ally.health_bar.update()

        for enemy in self.enemies:
            enemy.speed_bar.update()
            enemy.health_bar.update()

        # wait for the player to choose an ability
        if self.choosing_ability:
            return

        for ally in self.allies:
            if ally.speed_bar.target_value == ally.speed_bar.max_value:
                ally.speed_bar.update_speed(-ally.speed_bar.max_value)

        # delay after an attack
        if self.delay > 0:
            self.delay -= 1
            return

        i = 0
        for ally in self.allies:
            i += 1

            # update speed bar
            ally.speed_bar.update_speed(ally.unit.stats.speed / 50)

            # if speed bar is charged, attack
            if ally.speed_bar.target_value == ally.speed_bar.max_value:

                # wait for the player (first friendly unit) to choose an ability
                if i == 1:
                    self.choosing_ability = True
                    # temporary ability
                    damage_value = ally.unit.abilities[0].use(ally.unit, self.enemies[0].unit)
                    print("ally " + str(i) + " damage " + str(damage_value))
                    self.enemies[0].update_health(-damage_value)
                    if self.enemies[0].health_bar.target_value <= 0:
                        self.enemies.remove(self.enemies[0])
                    self.delay = 60
                    return

                # ally ai
                self.ally_action(ally)

                ally.speed_bar.update_value(-ally.speed_bar.max_value)
                self.delay = 60
                return

            # if ally is dead, remove it
            if ally.health_bar.target_value <= 0:
                self.allies.remove(ally)
                print("ally " + str(i) + " died")

        i = 0
        for enemy in self.enemies:
            i += 1

            enemy.speed_bar.update_speed(enemy.unit.stats.speed / 50) # speed coeff

            # if speed bar is charged, attack
            if enemy.speed_bar.target_value == enemy.speed_bar.max_value:

                # enemy ai
                self.enemy_action(enemy)

                enemy.speed_bar.update_value(-enemy.speed_bar.max_value)
                self.delay = 60
                return

            # if enemy is dead, remove it
            if enemy.health_bar.target_value <= 0:
                self.enemies.remove(enemy)
                print("enemy " + str(i) + " died")

    def draw(self, surface):
        for enemy in self.enemies:
            enemy.draw(surface)

        for ally in self.allies:
            ally.draw(surface)

        self.end_turn_button.draw(surface)

        # Temporary buttons for testing
        for button in self.enemy_buttons:
            button.draw(surface)

    def all_enemies_dead(self):
        return all(not enemy.alive for enemy in self.enemies)