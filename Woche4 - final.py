import random
import sys
import pygame

pygame.init()

window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Week 4: Functions - Modular Structure")

bg_color = (30, 30, 30)
player_color = (200, 50, 50)
obstacle_color = (150, 150, 150)
goal_color = (50, 200, 50)

player_x = 50
player_y = 500
player_hp = 100
normal_speed = 5
sprint_speed = 10
fall_speed = 4.0

obstacles = []
for i in range(8):
  obs_width = random.randint(30, 60)
  obs_height = random.randint(30, 60)
  obs_x = random.randint(150, 700)
  obs_y = random.randint(-600, -50)
  obstacles.append(pygame.Rect(obs_x, obs_y, obs_width, obs_height))

clock = pygame.time.Clock()

#-----------------------------
#         Functions           
#-----------------------------

def handle_player_movement(keys, x, hp):
  if keys[pygame.K_LSHIFT]:
    current_speed = sprint_speed
  else:
    current_speed = normal_speed

  if keys[pygame.K_LEFT]:
    x -= current_speed
  if keys[pygame.K_RIGHT]:
    x += current_speed

  if x < 0:
    x = 0

  return x


def update_obstacles(obstacles_list, player_rect, hp, current_fall_speed):
  for obs in obstacles_list:
    obs.y += current_fall_speed

    if obs.y > window_height:
      obs.y = random.randint(-300, -50)
      obs.x = random.randint(150, 700)
      current_fall_speed += 0.05

    if player_rect.colliderect(obs):
      damage = obs.height
      hp -= damage
      print(f"Hit! Took {damage} damage. HP left: {hp}")
      obs.y = random.randint(-300, -50)
      obs.x = random.randint(150, 700)

  return hp, current_fall_speed


def check_game_status(hp, x):
  if hp <= 0:
    print("Game Over!")
    pygame.quit()
    sys.exit()

  if x >= window_width - 50 - hp:
    print("You survived and reached the goal!")
    pygame.quit()
    sys.exit()

#-----------------------------
#         Main-Loop           
#-----------------------------

while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()

  keys = pygame.key.get_pressed()

  # 1. Player-Movement 
  player_x = handle_player_movement(keys, player_x, player_hp)

  player_rect = pygame.Rect(player_x, player_y, player_hp, 40)

  # 2. Obstacle Logic
  player_hp, fall_speed = update_obstacles(obstacles, player_rect, player_hp, fall_speed)

  # 3. Game Status
  check_game_status(player_hp, player_x)

  screen.fill(bg_color)

  pygame.draw.rect(screen, goal_color, (window_width - 50, 0, 50, window_height))
  pygame.draw.rect(screen, player_color, player_rect)

  for obs in obstacles:
    pygame.draw.rect(screen, obstacle_color, obs)

  pygame.display.flip()
  clock.tick(60)