import pygame
import utils.button
import utils.health_bar
from utils.enemy import Enemy

# Initialize the game
pygame.init()

# Set up the screen
screen = pygame.display.set_mode((800, 600))
surface = pygame.Surface((800, 600), pygame.SRCALPHA)

# Set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the player
player = pygame.Rect(50, 50, 50, 50)

# Set up the clock
clock = pygame.time.Clock()

# Run the game
running = True

# define the button
button = utils.button.Button(100, 100, 200, 100, (255, 0, 0, 100), '', lambda: print('Hello'))

# health bar
health_bar = utils.health_bar.HealthBar(10, 10, 200, 20, 100, "Darius")
damage_button = utils.button.Button(310, 100, 200, 50, (255, 0, 0, 100), 'Damage', lambda: health_bar.update_value(-10))
heal_button = utils.button.Button(310, 150, 200, 50, (255, 0, 0, 100), 'Heal', lambda: health_bar.update_value(10))

# Create an enemy with animations
sprite_paths = ['sprites/enemies/AMOGUS_1.png', 'sprites/enemies/AMOGUS_2.png', 'sprites/enemies/AMOGUS_3.png', 'sprites/enemies/AMOGUS_4.png']
death_sprite_paths = ['sprites/enemies/AMOGUS_death_1.png', 'sprites/enemies/AMOGUS_death_2.png']
enemy = Enemy(400, 350, 150, 150, 100, 100, "Amogus", sprite_paths, death_sprite_paths)
enemy_damage_button = utils.button.Button(310, 200, 200, 50, (255, 0, 0, 100), 'Damage Enemy', lambda: enemy.update_health(-10))
enemy_decrease_speed_button = utils.button.Button(310, 250, 200, 50, (255, 0, 0, 100), 'Decrease Speed', lambda: enemy.speed_bar.update_speed(-10, 1))

# Draw the game
def draw_game():
    button.draw(surface)
    health_bar.draw(screen)
    damage_button.draw(surface)
    heal_button.draw(surface)
    enemy.draw(screen)
    enemy_damage_button.draw(surface)
    enemy_decrease_speed_button.draw(surface)

while running:
    # Cap the frame rate
    clock.tick(60)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update the game
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5
    if keys[pygame.K_UP]:
        player.y -= 5
    if keys[pygame.K_DOWN]:
        player.y += 5

    # Update the speed bar based on time
    enemy.speed_bar.update_speed(1 / 5, 1)
    enemy.speed_bar.update()
    enemy.health_bar.update()

    # Draw the game
    screen.fill(BLACK)
    screen.blit(surface, (0, 0))
    draw_game()
    pygame.display.flip()

# Quit the game
pygame.quit()
