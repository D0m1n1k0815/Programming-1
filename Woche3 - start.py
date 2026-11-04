import pygame
import sys
import random # Required to randomize obstacle positions and sizes

pygame.init()

window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("First Pygame Tutorial")

bg_color = (30, 30, 30)     
player_color = (200, 50, 50) 

player_x = 400
player_y = 300
player_width = 40
player_height = 40
speed = 5
normal_speed = 5
sprint_speed = 10

player_hp = 100
damage_taken = 10


clock = pygame.time.Clock()

# 4. Variables for obstacles (Using a List for the 'for' loop)
obstacles = []
for i in range(8): 
    obs_width = random.randint(30, 60)
    obs_height = random.randint(30, 60)
    obs_x = random.randint(150, 700)
    obs_y = random.randint(-600, -50) # Start off-screen at the top
    # pygame.Rect creates a hitbox: (x, y, width, height)
    obstacles.append(pygame.Rect(obs_x, obs_y, obs_width, obs_height))

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        player_x -= speed

    if keys[pygame.K_RIGHT]:
        player_x += speed

    if keys[pygame.K_LSHIFT]:
        speed = sprint_speed
    else:
         speed = normal_speed

    #CREATE HITBOX: Combine player position and HP (width) into a Rect
    player_rect = pygame.Rect(player_x, player_y, player_hp, 40)

    #LOOP & CONDITIONS: Update and check all obstacles
    for obs in obstacles:
        obs.y += 4
        #add Code here

        #Collision Detection
        if player_rect.colliderect(obs):
            continue
            #add Code here



    screen.fill(bg_color)
        
    pygame.draw.rect(screen, player_color, (player_x, player_y, player_hp, 40))
    
    for obs in obstacles:
        pygame.draw.rect(screen, (150, 150, 150), obs)
    pygame.display.flip()

    clock.tick(60)