import random
import time

player_armor = 5
player_hp = 50

print("Start-HP =", player_hp, "| Armor =", player_armor)
print("-" * 40)

def take_damage(current_hp, incoming_damage, armor):
  final_damage = incoming_damage - armor

  if final_damage < 0:
    final_damage = 0

  current_hp -= final_damage

  if current_hp < 0:
    current_hp = 0

  print("Incoming damage:", incoming_damage, " damage | Blocked with Armor:", armor, " | Damage recieved:", final_damage,)
  print(" Player HP:", current_hp)

  return current_hp


while player_hp > 0:
  incoming_damage = random.randint(10, 25)

  player_hp = take_damage(player_hp, incoming_damage, player_armor)

  time.sleep(1)

print("Game Over!")