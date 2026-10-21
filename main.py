# Import the Pygame library for game development and the sys module to exit the program cleanly
import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Open the window
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("First Pygame Tutorial")

# 3. Variables for the simple object (player)
player_x = 100

# Create a clock to limit the framerate
clock = pygame.time.Clock()

# 4. The Main Game Loop
while True:

        # A. Handle events (Direct exit instead of running = False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # B. Capture keyboard input and move the object
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_x -= 5

    # C. Draw the background
    screen.fill((30, 30, 30))

    # D. Draw the simple object (a rectangle)
    pygame.draw.rect(screen, (200, 50, 50), (player_x, 200, 40, 40))

    # E. Update the screen to show the drawings
    pygame.display.flip()

    # F. Limit the framerate (to 60 frames per second)
    clock.tick(60)