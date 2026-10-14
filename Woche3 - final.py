import pygame
import sys
import random # Required to randomize obstacle positions and sizes

# 1. Initialize Pygame
pygame.init()

# 2. Open the window
window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Week 3: Conditions and Loops - Final Solution")

# Define colors 
bg_color = (30, 30, 30)
player_color = (200, 50, 50)
obstacle_color = (150, 150, 150) # Gray
goal_color = (50, 200, 50)       # Green

# 3. Variables for the player
player_x = 50 
player_y = 500 # Moved to the bottom to dodge falling objects
player_hp = 100
player_name = "Student"

normal_speed = 5
sprint_speed = 10
speed = normal_speed

# CHALLENGE 3: Variable for dynamic difficulty
fall_speed = 4.0 

# 4. Variables for obstacles (Using a List for the 'for' loop)
obstacles = []
for i in range(8): 
    obs_width = random.randint(30, 60)
    obs_height = random.randint(30, 60)
    obs_x = random.randint(150, 700)
    obs_y = random.randint(-600, -50) # Start off-screen at the top
    # pygame.Rect creates a hitbox: (x, y, width, height)
    obstacles.append(pygame.Rect(obs_x, obs_y, obs_width, obs_height))

clock = pygame.time.Clock()

# 5. The Main Game Loop
while True:
    
    # A. Handle events (Direct exit instead of running = False)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # B. Capture keyboard input and move the player
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LSHIFT]:
        speed = sprint_speed
    else:
        speed = normal_speed

    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed

    # C. CONDITION: Screen Boundaries (Keep player inside the window)
    # Left boundary
    if player_x < 0:
        player_x = 0
        
    # CHALLENGE 1: Right boundary 
    # Since player width is bound to player_hp, we subtract player_hp from window_width
    if player_x > window_width - player_hp:
        player_x = window_width - player_hp

    # D. CREATE HITBOX: Combine player position and HP (width) into a Rect
    player_rect = pygame.Rect(player_x, player_y, player_hp, 40)

    # E. LOOP & CONDITIONS: Update and check all obstacles
    for obs in obstacles:
        # CHALLENGE 3: Use the dynamic fall_speed instead of a fixed number
        obs.y += int(fall_speed) 
        
        # Condition 1: Reset obstacle to the top if it falls off the screen
        if obs.y > window_height:
            obs.y = random.randint(-300, -50)
            obs.x = random.randint(150, 700)
            # CHALLENGE 3: Increase the speed slightly every time an obstacle is dodged
            fall_speed += 0.1 

        # Condition 2: Collision Detection
        if player_rect.colliderect(obs):
            # CHALLENGE 2: Damage equals size. 
            # Instead of a fixed 20, we use the height of the specific obstacle
            damage = obs.height 
            player_hp -= damage
            
            print(f"Hit! Took {damage} damage. HP left: {player_hp}")
            obs.y = random.randint(-300, -50) # Reset this specific obstacle

    # F. CONDITIONS: Win and Loss states (Direct Exit)
    if player_hp <= 0:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if player_x >= window_width - 50: # Reached the green goal area
        print("You survived and reached the goal!")
        pygame.quit()
        sys.exit()

    # G. Draw everything
    screen.fill(bg_color)
    
    pygame.draw.rect(screen, goal_color, (window_width - 50, 0, 50, window_height))
    pygame.draw.rect(screen, player_color, player_rect)

    for obs in obstacles:
        pygame.draw.rect(screen, obstacle_color, obs)

    pygame.display.flip()
    clock.tick(60)