import pygame
from inventory import draw_inventory, draw_item_info_logic, draw_item_following_mouse, draw_delete_logic, \
    inventory_event_handler, delete_button, get_slot_at_mouse, set_selected_item, get_selected_item, SLOT_SIZE, \
    draw_item_info, get_inventory
from inventory import selected_item
from utils.bar import Bar
from globals import player_unit
from constants import level_requirements

OFFSET_X = 500
OFFSET_Y = 100

class EndBattleScreen:
    def __init__(self, surface, friendly_units, xp, money, items):
        self.friendly_units = friendly_units
        self.xp = xp
        self.money = money
        self.items = items
        self.surface = surface
        self.item_positions = []
        self.xp_bar = Bar(OFFSET_X, OFFSET_Y + 300, 200, 20, level_requirements[player_unit.level + 1] - level_requirements[player_unit.level], (100, 100, 100), (200, 200, 200))
        self.xp_bar.real_value =  self.xp_bar.target_value = self.xp_bar.current_value = player_unit.xp - level_requirements[player_unit.level]
        self.target_xp = 0

    def display_rewards(self):
        font = pygame.font.Font(None, 36)
        # Display "You won!" message
        you_won_text = "You won!"
        you_won_surface = font.render(you_won_text, True, (255, 255, 0))
        self.surface.blit(you_won_surface, (OFFSET_X, OFFSET_Y))

        # Display rewards
        rewards_text = "Rewards:"
        rewards_surface = font.render(rewards_text, True, (255, 255, 255))
        self.surface.blit(rewards_surface, (OFFSET_X, OFFSET_Y + 50))

        # Display items
        x, y = OFFSET_X, OFFSET_Y + 100
        self.item_positions = []
        for item in self.items:
            item_sprite = pygame.image.load(item.sprite)
            item_sprite = pygame.transform.scale(item_sprite, (SLOT_SIZE, SLOT_SIZE))
            self.surface.blit(item_sprite, (x, y))
            self.item_positions.append((item, pygame.Rect(x, y, SLOT_SIZE, SLOT_SIZE)))
            y += SLOT_SIZE + 10  # Add some space between items

        # Display money
        money_text = f"Money: {self.money}"
        money_surface = font.render(money_text, True, (255, 255, 255))
        self.surface.blit(money_surface, (OFFSET_X, y + 20))

        # Display XP earned
        xp_text = f"XP earned: {self.xp}"
        xp_surface = font.render(xp_text, True, (255, 255, 255))
        self.surface.blit(xp_surface, (OFFSET_X, y + 60))

    def draw_item_info_rewards(self):
        mouse_pos = pygame.mouse.get_pos()
        for item, rect in self.item_positions:
            if rect.collidepoint(mouse_pos):
                draw_item_info(self.surface, item.item, mouse_pos)
                break

    def end_battle_screen_logic(self):
        self.display_rewards()
        draw_inventory(self.surface, get_inventory(), selected_item)
        delete_button.draw(self.surface)
        draw_item_info_logic()
        draw_item_following_mouse()
        draw_delete_logic()
        self.draw_item_info_rewards()
        self.xp_bar.update()
        self.xp_bar.draw(self.surface)
        # if the player leveled up
        if self.xp_bar.current_value == self.xp_bar.max_value:
            self.xp_bar = Bar(OFFSET_X, OFFSET_Y + 300, 200, 20, level_requirements[player_unit.level + 1] - level_requirements[player_unit.level], (100, 100, 100), (200, 200, 200))
            self.xp_bar.target_value = player_unit.xp - level_requirements[player_unit.level]
            self.xp_bar.current_value = self.xp_bar.real_value = 0

    def end_battle_handle_event(self, event):
        inventory_event_handler(event)
        delete_button.handle_event(event)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            y_start = OFFSET_Y + 100  # Starting y position for items
            for index, item in enumerate(self.items):
                item_rect = pygame.Rect(OFFSET_X, y_start + index * (SLOT_SIZE + 10), SLOT_SIZE, SLOT_SIZE)
                if item_rect.collidepoint(mouse_pos):
                    set_selected_item(item)
                    self.items.remove(item)
                    break