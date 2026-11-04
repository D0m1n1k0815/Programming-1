import random
import pygame

clock = pygame.time.Clock()


obstacles = []
for i in range(8): 
    obs_width = random.randint(30, 60)
    obs_height = random.randint(30, 60)
    obs_x = random.randint(150, 700)
    obs_y = random.randint(-600, -50) # Start off-screen at the top
    # pygame.Rect creates a hitbox: (x, y, width, height)
    obstacles.append(pygame.Rect(obs_x, obs_y, obs_width, obs_height))

while True:
    for obs in obstacles:
        obs.y += 10
        print(obs.y, end=" ")
    print()

    clock.tick(1)