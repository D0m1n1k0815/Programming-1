import random
import time

player_armor = 5
player_hp = 50

print("Start-HP =", player_hp, "| Armor =", player_armor)
print("-" * 40)

while player_hp > 0:
  incoming_damage = random.randint(10, 25)

  final_damage = incoming_damage - player_armor

  if final_damage < 0:
    final_damage = 0 

  player_hp -= final_damage

  if player_hp < 0:
    player_hp = 0

  print("Incoming damage:", incoming_damage," damage | Blocked with Armor:", player_armor, " | Damage recieved:", final_damage)
  print(f" Player HP:" ,player_hp)

  time.sleep(1)

print("Game Over!")