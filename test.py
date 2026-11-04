import sys
import pygame

# 1. Initialize Pygame
pygame.init()

# 2. Open the window
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Pygame Tutorial")

# Define colors (RGB: Red, Green, Blue)
bg_color = (30, 30, 30)       # Dark gray
player_color = (200, 50, 50)  # Red

# 3. Variables for the simple object (player)
player_x = 400
player_y = 300
player_width = 40.0
player_height = 40.0
speed = 5
hp = 100.0

# Create a clock to limit the framerate
clock = pygame.time.Clock()

# 4. The Main Game Loop
while True:
    # A. Handle events (Direct exit instead of running = False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # Einzelne Tastendrücke (verhindert das extreme "Dauerfeuer" in get_pressed)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_CAPSLOCK:
                hp = max(1, hp - 10)

    # B. Capture keyboard input and move the object
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    # DELETE verkleinert das Rechteck
    if keys[pygame.K_DELETE] and player_width and player_height:
        player_height -= 1
        player_width -= 1

    if player_width <= 0 or player_height <= 0:
        hp = 0

    
    hp = 100 - ((1600 - (player_height * player_width)) / 16)
    player_height = 40 - (100 - hp) * 0.4
    player_width = 40 - (100 - hp) * 0.4

    # C. Draw the background
    screen.fill(bg_color)

    # D. Draw the simple object (a rectangle)
    pygame.draw.rect(
        screen,
        player_color,
        pygame.draw.rect(screen, player_color, (player_x, player_y, player_width, player_height))
    )

    # E. Update the screen to show the drawings
    pygame.display.flip()

    # F. Limit the framerate (to 60 frames per second)
    clock.tick(60)
    print(f"HP: {hp:.1f}")