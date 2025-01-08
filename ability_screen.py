import pygame

from abilities.ability import Ability
from abilities.ability_sprite import AbilitySprite
from ability_screen_utils.ability_wheel import AbilityWheel
from ability_screen_utils.ability_pool import AbilityPool
from ability_screen_utils.skill_tree import SkillTree

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

def ability_screen_logic():
    global selected_ability, ability_wheel, ability_pool, screen
    skill_tree.draw(screen)
    ability_wheel.draw(screen)
    ability_pool.draw(screen)
    if selected_ability:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(selected_ability.image, (mouse_x - SLOT_SIZE // 2, mouse_y - SLOT_SIZE // 2))

def ability_screen_event_handler(event):
    global selected_ability, ability_wheel, ability_pool, running
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
                ability_wheel.slots[wheel_index] = selected_ability
                selected_ability = None
            else:
                selected_ability = None

running = True
selected_ability = None
ability_wheel = AbilityWheel((1000, 175), WHEEL_RADIUS, 8, SLOT_SIZE)
abilities = [AbilitySprite(0, 0, SLOT_SIZE, SLOT_SIZE, Ability(f"Ability {i+1}", "Description", 0, 0, "self", 'sprites/abilities/slash.png')) for i in range(5)]
ability_pool = AbilityPool((POOL_OFFSET_X, POOL_OFFSET_Y), abilities, SLOT_SIZE)

from globals import player_unit

skill_tree = SkillTree(player_unit)

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