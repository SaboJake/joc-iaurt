import math
import random

import pygame

from abilities.ability_sprite import AbilitySprite
from abilities.basic_attack import BasicAttack
from abilities.basic_heal import BasicHeal
from units.player_unit import PlayerUnit
from utils.button import Button
from utils.display_unit import DisplayUnit
from units.unit import Unit
from units.friendly_unit import FriendlyUnit
from utils.stats import Stats
from abilities.slash_ability import SlashAbility

from globals import player_unit

ally_X = [300, 200, 200]
ally_Y = [400, 250, 550]
ally_width = 150
ally_height = 150
ally_health_X = [100, 100, 100]
ally_health_Y = [10, 60, 110]

enemy_x = [750, 850, 850]
enemy_y = [400, 250, 550]
enemy_width = 150
enemy_height = 150
enemy_health_x = [900, 900, 900]
enemy_health_y = [10, 60, 110]

ABILITY_WIDTH = 50
ABILITY_HEIGHT = 50

coeffs = {
    'strength': 1,
    'intelligence': 1,
    'speed': 1
}

sprite_paths = ['sprites/enemies/AMOGUS_1.png']#, 'sprites/enemies/AMOGUS_2.png', 'sprites/enemies/AMOGUS_3.png', 'sprites/enemies/AMOGUS_4.png']
death_sprite_paths = ['sprites/enemies/AMOGUS_death_1.png', 'sprites/enemies/AMOGUS_death_2.png']
names_array = ["Amogus"]#, "Amogus", "Amogus"]
clas_array = ["am"]#, "og", "us"]
sprite_paths_array = [sprite_paths, sprite_paths, sprite_paths]
death_sprite_paths_array = [death_sprite_paths, death_sprite_paths, death_sprite_paths]

class Stage:
    def __init__(self, stage_no):
        # if stage_no == 0:
            # add stage enemies and so on

        # add allies
        allies = []
        ally_units = []
        for i in range(len(names_array)):
            # first unit is the player
            if i == 0:
                ally_units.append(player_unit)
            else:
                ally_units.append(FriendlyUnit(names_array[i], clas_array[i], Stats(10, 10, 10, 25 + (3 - i) * 5, 10), Stats(10, 10, 10, 25 + (3 - i) * 5, 10)))
                ally_units[i].abilities.append(BasicAttack(coeffs, "attack", "WHO CARES", 0, 0, "physical", 'sprites/abilities/slash.png'))
                ally_units[i].abilities.append(BasicHeal(coeffs, "heal", "WHO CARES", 0, 0, "physical", 'sprites/abilities/heal.png'))


        if len(names_array) == 2:
            for i in range(len(names_array)):
                allies.append(DisplayUnit(ally_X[i + 1], ally_Y[i + 1], ally_width, ally_height, ally_health_X[i], ally_health_Y[i], 100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i], ally_units[i]))

        else:
            for i in range(len(names_array)):
                allies.append(DisplayUnit(ally_X[i], ally_Y[i], ally_width, ally_height, ally_health_X[i], ally_health_Y[i], 100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i], ally_units[i]))

        # add enemies
        enemies = []
        enemy_units = []
        for i in range(len(names_array)):
            enemy_units.append(Unit(names_array[i], Stats(10, 10, 10, 25 + i * 5, 10), Stats(10, 10, 10, 25 + i * 5, 10)))
            enemy_units[i].abilities.append(BasicAttack(coeffs, "WHO", "CARES", 0, 0, "physical", 'sprites/abilities/slash.png'))
            enemy_units[i].abilities.append(BasicHeal(coeffs, "WHO", "CARES", 0, 0, "physical", 'sprites/abilities/heal.png'))

        if len(names_array) == 2:
            for i in range(len(names_array)):
                enemies.append(DisplayUnit(enemy_x[i + 1], enemy_y[i + 1], enemy_width, enemy_height, enemy_health_x[i], enemy_health_y[i],100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i], enemy_units[i]))

        else:
            for i in range(len(names_array)):
                enemies.append(DisplayUnit(enemy_x[i], enemy_y[i], enemy_width, enemy_height, enemy_health_x[i], enemy_health_y[i], 100, names_array[i], sprite_paths_array[i], death_sprite_paths_array[i], enemy_units[i]))

        self.enemies = enemies
        self.allies = allies

        self.delay = 0
        self.choosing_ability = False
        self.end_turn_button = Button(575, 750, 50, 50, (255, 0, 0, 100), 'End Turn', lambda: self.end_turn())

        self.selected_enemy = None
        self.selected_ally = None
        self.selected_ability = None

        self.ability_sprites = pygame.sprite.Group()

    def end_turn(self):
        self.choosing_ability = False
        self.selected_enemy = None
        self.selected_ally = None
        self.selected_ability = None
        self.ability_sprites.empty()

    def stage_event_handler(self, event, surface):
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if self.choosing_ability:
                for sprite in self.ability_sprites:
                    if hasattr(sprite, 'ability') and sprite.rect.collidepoint(mouse_pos):
                        self.use_ability(sprite.ability)
                        return

                for enemy in self.enemies:
                    if enemy.rect.collidepoint(mouse_pos):
                        self.selected_enemy = enemy
                        self.selected_ally = None
                        self.display_abilities(surface)
                        return

                for ally in self.allies:
                    if ally.rect.collidepoint(mouse_pos):
                        self.selected_ally = ally
                        self.selected_enemy = None
                        self.display_abilities(surface)
                        return

    def display_abilities(self, surface):
        # display the abilities of the first ally
        self.ability_sprites.empty()

        radius = 100
        for i in range(8):
            ability = player_unit.abilities[i]
            angle = 2 * math.pi * i / 8
            x = y = 0
            if self.selected_enemy is not None:
                x = self.selected_enemy.rect.x + self.selected_enemy.rect.width / 2 + math.cos(angle) * radius
                y = self.selected_enemy.rect.y + self.selected_enemy.rect.height / 2 + math.sin(angle) * radius
            elif self.selected_ally is not None:
                x = self.selected_ally.rect.x + self.selected_ally.rect.width / 2 + math.cos(angle) * radius
                y = self.selected_ally.rect.y + self.selected_ally.rect.height / 2 + math.sin(angle) * radius

            if ability is not None:
                sprite = AbilitySprite(x, y, ABILITY_WIDTH, ABILITY_HEIGHT, ability)
                self.ability_sprites.add(sprite)
            else:
                gray_circle = pygame.sprite.Sprite()
                gray_circle.image = pygame.Surface((ABILITY_WIDTH, ABILITY_HEIGHT), pygame.SRCALPHA)
                pygame.draw.circle(gray_circle.image, (200, 200, 200), (ABILITY_WIDTH // 2, ABILITY_HEIGHT // 2), ABILITY_WIDTH // 2)
                gray_circle.rect = gray_circle.image.get_rect(center=(x, y))
                self.ability_sprites.add(gray_circle)

    def use_ability(self, ability):
        self.selected_ability = ability
        if self.selected_enemy is not None:
            if ability.target != "enemy":
                return
            damage_value = self.selected_ability.use(self.allies[0].unit, self.selected_enemy.unit)
            print("used ability on enemy, damage:", damage_value)
            self.selected_enemy.update_health(-damage_value)
            if self.selected_enemy.health_bar.target_value <= 0:
                self.enemies.remove(self.selected_enemy)
        elif self.selected_ally is not None:
            if ability.target == "enemy":
                return
            if ability.target == "self" and self.selected_ally != self.allies[0]:
                return
            heal_value = self.selected_ability.use(self.allies[0].unit, self.selected_ally.unit)
            print("used ability on ally, heal:", heal_value)
            self.selected_ally.update_health(heal_value)

        self.choosing_ability = False
        self.selected_enemy = None
        self.selected_ally = None
        self.selected_ability = None
        self.ability_sprites.empty()

        self.delay = 90

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

        else:
            # random attack ability
            ability = ally.unit.abilities[random.randint(0, len(ally.unit.abilities) - 1)]
            while ability.target != "enemy":
                ability = ally.unit.abilities[random.randint(0, len(ally.unit.abilities) - 1)]

            # random target
            target = self.enemies[random.randint(0, len(self.enemies) - 1)]
            damage_value = ability.use(ally.unit, target.unit)
            print("ally " + str(ally) + " damage " + str(damage_value))
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
                ally.unit.update_stats()

                # wait for the player (first friendly unit) to choose an ability
                if i == 1:
                    self.choosing_ability = True
                    return

                # ally ai
                self.ally_action(ally)

                ally.unit.apply_effects()

                ally.speed_bar.update_value(-ally.speed_bar.max_value)
                self.delay = 90
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
                enemy.unit.update_stats()

                # enemy ai
                self.enemy_action(enemy)

                enemy.unit.apply_effects()

                enemy.speed_bar.update_value(-enemy.speed_bar.max_value)
                self.delay = 90
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

        if self.choosing_ability and hasattr(self, 'ability_sprites'):
            self.ability_sprites.draw(surface)

        # show ability info when hovering
        mouse_pos = pygame.mouse.get_pos()
        if self.choosing_ability and hasattr(self, 'ability_sprites'):
            for i, sprite in enumerate(self.ability_sprites):
                if player_unit.abilities[i] is None:
                    continue
                if sprite.rect.collidepoint(mouse_pos):
                    self.ability_sprites.sprites()[i].show_info(surface)
                    break

    def all_enemies_dead(self):
        return all(not enemy.alive for enemy in self.enemies)

    def player_dead(self):
        # if a unit dies, it is removed from its list, so if the fist unit is not the player, he died
        return not self.allies[0].unit.is_player()