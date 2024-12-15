import pygame
import utils.button
import utils.health_bar

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
damage_button = utils.button.Button(310, 100, 200, 50, (255, 0, 0, 100), 'Damage', lambda: health_bar.update_health(-10))
heal_button = utils.button.Button(310, 150, 200, 50, (255, 0, 0, 100), 'Heal', lambda: health_bar.update_health(10))

# Draw the game
def draw_game():
    button.draw(surface)
    health_bar.draw(screen)
    damage_button.draw(surface)
    heal_button.draw(surface)

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

    # Draw the game
    screen.fill(BLACK)
    screen.blit(surface, (0, 0))
    draw_game()
    pygame.display.flip()

# Quit the game
pygame.quit()
