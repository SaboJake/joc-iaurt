import pygame
import math

from abilities.ability import Ability
from abilities.ability_sprite import AbilitySprite
from ability_screen_utils.ability_wheel import AbilityWheel
from ability_screen_utils.ability_pool import AbilityPool
from ability_screen_utils.skill_tree import SkillTree
from utils.upgrade_stats_menu import draw_stats_box

from globals import player_unit

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 1200, 900
SLOT_SIZE = 40
WHEEL_RADIUS = 100
POOL_OFFSET_X, POOL_OFFSET_Y = 850, 350
BG_COLOR = (50, 50, 50)
FPS = 60

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Ability Wheel and Pool")
clock = pygame.time.Clock()

def update_save_data_abilities(save_data):
    global ability_pool, ability_wheel, skill_tree
    skill_tree.update_save_data(save_data)
    ability_pool.update_save_data(save_data)
    ability_wheel.update_save_data(save_data)

def get_save_data_abilities(save_data):
    global ability_pool, ability_wheel, skill_tree
    skill_tree.get_save_data(save_data)
    ability_pool.get_save_data(save_data)
    ability_wheel.get_save_data(save_data)
    # Update the player unit's abilities
    player_unit.abilities = [None] * len(ability_wheel.slots)
    for i, ability in enumerate(ability_wheel.slots):
        if ability:
            player_unit.abilities[i] = ability.ability

def ability_screen_logic():
    global selected_ability, ability_wheel, ability_pool, screen, message, message_display_time
    skill_tree.draw(screen)
    ability_wheel.draw(screen)
    ability_pool.draw(screen)
    draw_stats_box(screen)
    if selected_ability:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(selected_ability.image, (mouse_x - SLOT_SIZE // 2, mouse_y - SLOT_SIZE // 2))

    for ability in ability_pool.abilities:
        ability.show_info(screen)

    for line in skill_tree.grid:
        for ability in line:
            if ability:
                ability.show_info(screen)

    for slot in ability_wheel.slots:
        if slot:
            slot.show_info(screen)

    if message and pygame.time.get_ticks() - message_display_time < MESSAGE_DURATION:
        display_message(screen, message)
    else:
        message = ""

def count_ability_in_wheel(ability):
    return sum(1 for slot in ability_wheel.slots if slot and slot.ability == ability)

# Add this to the global variables
message = ""
message_display_time = 0
MESSAGE_DURATION = 2000  # Duration in milliseconds

# Add this function to display the message
def display_message(screen, message):
    if message:
        font = pygame.font.Font(None, 36)
        text = font.render(message, True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 50))
        screen.blit(text, text_rect)

# Modify the ability_screen_event_handler function
def ability_screen_event_handler(event):
    global selected_ability, ability_wheel, ability_pool, running, message, message_display_time
    skill_tree.handle_event(event)
    if event.type == pygame.QUIT:
        running = False
    elif event.type == pygame.MOUSEBUTTONDOWN:
        mouse_pos = pygame.mouse.get_pos()
        if selected_ability is None:
            pool_index = ability_pool.get_ability_at_pos(mouse_pos)
            if pool_index is not None:
                selected_ability = ability_pool.abilities[pool_index]
            else:
                wheel_index = ability_wheel.get_slot_at_pos(mouse_pos)
                if wheel_index is not None and ability_wheel.slots[wheel_index]:
                    ability_wheel.slots[wheel_index] = None
        else:
            wheel_index = ability_wheel.get_slot_at_pos(mouse_pos)
            if wheel_index is not None:
                if count_ability_in_wheel(selected_ability.ability) < selected_ability.ability.max_equipped:
                    angle_step = 360 / ability_wheel.num_slots
                    angle = angle_step * wheel_index
                    x = ability_wheel.center[0] + ability_wheel.radius * math.cos(math.radians(angle))
                    y = ability_wheel.center[1] + ability_wheel.radius * math.sin(math.radians(angle))
                    selected_ability.x = x
                    selected_ability.y = y
                    ability_wheel.slots[wheel_index] = AbilitySprite(selected_ability.x, selected_ability.y, SLOT_SIZE, SLOT_SIZE, selected_ability.ability)
                    player_unit.abilities[wheel_index] = selected_ability.ability
                else:
                    message = f"This ability can only be equipped"
                    if selected_ability.ability.max_equipped == 1:
                        message += " once"
                    else:
                        message += f" {selected_ability.ability.max_equipped} times"
                    message_display_time = pygame.time.get_ticks()
                selected_ability = None
            else:
                selected_ability = None

running = True
selected_ability = None
ability_wheel = AbilityWheel((1000, 175), WHEEL_RADIUS, 8, SLOT_SIZE)
# Initialize abilities
slash1 = Ability("Slash", "A basic slash", 0, 0, "self", 'sprites/abilities/slash.png')
slash2 = Ability("Slash", "A basic slash", 0, 0, "self", 'sprites/abilities/slash.png')

# Create AbilitySprites for the slashes
slash_sprite1 = AbilitySprite(POOL_OFFSET_X + SLOT_SIZE // 2, POOL_OFFSET_Y + SLOT_SIZE // 2, SLOT_SIZE, SLOT_SIZE, slash1)
slash_sprite2 = AbilitySprite(POOL_OFFSET_X + SLOT_SIZE // 2 + SLOT_SIZE + 10, POOL_OFFSET_Y + SLOT_SIZE // 2, SLOT_SIZE, SLOT_SIZE, slash2)

abilities =[slash_sprite1, slash_sprite2]

# Add the slashes to the abilities list
ability_pool = AbilityPool((POOL_OFFSET_X, POOL_OFFSET_Y), abilities, SLOT_SIZE)

skill_tree = SkillTree(player_unit, ability_pool)

def main():
    while running:
        screen.fill(BG_COLOR)
        for event in pygame.event.get():
            ability_screen_event_handler(event)
        ability_screen_logic()

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()