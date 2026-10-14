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

    # B. Capture keyboard input and move the object
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_x -= 5

    # C. Draw the background
    # Important: The background must be redrawn every frame, otherwise the object will leave a "trail" behind it.
    screen.fill((30, 30, 30))

    # D. Draw the simple object (a rectangle)
    # pygame.draw.rect needs: (Where to draw?, Color, (x, y, width, height))
    pygame.draw.rect(screen, (200, 50, 50), (player_x, 200, 40, 40))

    # E. Update the screen to show the drawings
    pygame.display.flip()

    # F. Limit the framerate (to 60 frames per second)
    clock.tick(60)

# 5. Exit the program cleanly
pygame.quit()
sys.exit()