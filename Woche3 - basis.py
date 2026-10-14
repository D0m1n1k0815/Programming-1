import random

player_hp = 50
turn = 1

# Loop: Repeat as long as the condition is True
while player_hp > 0:
    print("Turn:", turn, "| HP:", player_hp)
    
    # Generate random damage between 0 and 20
    damage = random.randint(0, 20)
    
    # Condition: Check the amount of damage
    if damage > 15:
        print("Critical hit! Lost", damage, "HP.")
    elif damage > 0:
        print("Normal hit. Lost", damage, "HP.")
    else:
        print("Dodged!")
        
    player_hp -= damage
    turn += 1

print("Game Over. You survived", turn, "turns.")