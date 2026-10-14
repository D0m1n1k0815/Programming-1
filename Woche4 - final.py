import pygame
import sys
import random

# ==========================================
# FUNCTION DEFINITIONS
# ==========================================

# CHALLENGE 1: The Spawner Function
# Creates and returns a new obstacle with random properties
def create_new_obstacle():
    obs_width = random.randint(30, 60)
    obs_height = random.randint(30, 60)
    obs_x = random.randint(150, 700)
    obs_y = random.randint(-600, -50)
    return pygame.Rect(obs_x, obs_y, obs_width, obs_height)

# REFACTORING: Update Logic Function
# Handles movement, screen boundaries, and collisions for all obstacles
def update_obstacles(obs_list, player_hitbox, current_hp, current_speed, screen_height):
    for obs in obs_list:
        obs.y += int(current_speed)
        
        # Condition 1: Reset if off-screen
        if obs.y > screen_height:
            new_obs = create_new_obstacle()
            obs.update(new_obs) # Update existing rect with new random values
            current_speed += 0.1 # Dynamic difficulty increase

        # Condition 2: Collision check
        if player_hitbox.colliderect(obs):
            damage = obs.height 
            current_hp -= damage
            print(f"Hit! Took {damage} damage. HP left: {current_hp}")
            
            # Reset this specific obstacle
            new_obs = create_new_obstacle()
            obs.update(new_obs)
            
    # Return the modified values so the main loop can use them
    return current_hp, current_speed

# CHALLENGE 2: The Renderer Function
# Handles all drawing commands to keep the main loop clean
def draw_game(surface, player_rect, obs_list, screen_width, screen_height):
    bg_color = (30, 30, 30)
    player_color = (200, 50, 50)
    obstacle_color = (150, 150, 150)
    goal_color = (50, 200, 50)
    
    surface.fill(bg_color)
    
    # Draw Goal Line
    pygame.draw.rect(surface, goal_color, (screen_width - 50, 0, 50, screen_height))
    # Draw Player
    pygame.draw.rect(surface, player_color, player_rect)
    # Draw Obstacles
    for obs in obs_list:
        pygame.draw.rect(surface, obstacle_color, obs)

# CHALLENGE 3: Power-Up Function
# Heals the player but ensures HP does not exceed 100
def apply_powerup(current_hp):
    current_hp += 20
    if current_hp > 100:
        current_hp = 100
    print(f"Healed! HP is now: {current_hp}")
    return current_hp


# ==========================================
# MAIN PROGRAM SETUP
# ==========================================

pygame.init()

window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Week 4: Functions - Final Solution")

player_x = 50 
player_y = 500
player_hp = 100

normal_speed = 5
sprint_speed = 10
speed = normal_speed
fall_speed = 4.0 

# Initialize obstacles using our new spawner function
obstacles = []
for i in range(8): 
    obstacles.append(create_new_obstacle())

clock = pygame.time.Clock()

# ==========================================
# MAIN GAME LOOP
# ==========================================
while True:
    
    # A. Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        # Handle one-time key presses (like drinking a health potion)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_h:
                player_hp = apply_powerup(player_hp)

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

    # C. Screen Boundaries
    if player_x < 0:
        player_x = 0
    if player_x > window_width - player_hp:
        player_x = window_width - player_hp

    # D. Update Hitboxes
    player_rect = pygame.Rect(player_x, player_y, player_hp, 40)

    # E. Use our new logic function for obstacles
    player_hp, fall_speed = update_obstacles(obstacles, player_rect, player_hp, fall_speed, window_height)

    # F. Win and Loss states
    if player_hp <= 0:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if player_x >= window_width - 50:
        print("You survived and reached the goal!")
        pygame.quit()
        sys.exit()

    # G. Use our new rendering function
    draw_game(screen, player_rect, obstacles, window_width, window_height)

    pygame.display.flip()
    clock.tick(60)