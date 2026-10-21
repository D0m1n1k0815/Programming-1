import pygame
import sys

# 1. Initialize Pygame
pygame.init()

# 2. Open the window
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Pygame Tutorial")

# Define colors (RGB: Red, Green, Blue)
bg_color = (30, 30, 30)      # Dark gray
player_color = (200, 50, 50) # Red

# 3. Variables for the simple object (player)
player_x = 400
player_y = 300
player_width = 40
player_height = 40
speed = 5


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
        player_x -= speed

    # C. Draw the background
    # Important: The background must be redrawn every frame, otherwise the object will leave a "trail" behind it.
    screen.fill(bg_color)

    # D. Draw the simple object (a rectangle)
    # pygame.draw.rect needs: (Where to draw?, Color, (x, y, width, height))
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))

    # E. Update the screen to show the drawings
    pygame.display.flip()

    # F. Limit the framerate (to 60 frames per second)
    clock.tick(60)