import pygame
import sys
import random

pygame.init()

window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Week 3: Conditions and Loops - Final Solution")

bg_color = (30, 30, 30)
player_color = (200, 50, 50)
obstacle_color = (150, 150, 150)
goal_color = (50, 200, 50)   

player_x = 50 
player_y = 500
player_hp = 100
normal_speed = 5
sprint_speed = 10
speed = normal_speed

fall_speed = 4.0 

obstacles = []
for i in range(8): 
    obs_width = random.randint(30, 60)
    obs_height = random.randint(30, 60)
    obs_x = random.randint(150, 700)
    obs_y = random.randint(-600, -50)
    obstacles.append(pygame.Rect(obs_x, obs_y, obs_width, obs_height))

clock = pygame.time.Clock()

while True:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LSHIFT]:
        speed = sprint_speed
    else:
        speed = normal_speed

    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed

    if player_x < 0:
        player_x = 0

    player_rect = pygame.Rect(player_x, player_y, player_hp, 40)

    for obs in obstacles:
        obs.y += fall_speed
        
        if obs.y > window_height:
            obs.y = random.randint(-300, -50)
            obs.x = random.randint(150, 700)
            fall_speed += 0.1 

        if player_rect.colliderect(obs):
            damage = obs.height 
            player_hp -= damage
            
            print(f"Hit! Took {damage} damage. HP left: {player_hp}")
            obs.y = random.randint(-300, -50)
            obs.x = random.randint(150, 700)

    if player_hp <= 0:
        print("Game Over!")
        pygame.quit()
        sys.exit()

    if player_x >= window_width - 50 - player_hp:
        print("You survived and reached the goal!")
        pygame.quit()
        sys.exit()

    screen.fill(bg_color)
    
    pygame.draw.rect(screen, goal_color, (window_width - 50, 0, 50, window_height))
    pygame.draw.rect(screen, player_color, player_rect)

    for obs in obstacles:
        pygame.draw.rect(screen, obstacle_color, obs)

    pygame.display.flip()
    clock.tick(60)