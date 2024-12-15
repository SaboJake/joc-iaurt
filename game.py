import pygame
import utils.button

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

# Draw the game
def draw_game():
    button.draw(surface)

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
