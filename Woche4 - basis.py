# Defining the function
def calculate_damage(incoming_damage, armor_value):
    final_damage = incoming_damage - armor_value
    
    if final_damage < 0:
        final_damage = 0 # Armor fully blocked the attack
        
    return final_damage

# Calling the function
player_armor = 5
hit_1 = calculate_damage(20, player_armor)
hit_2 = calculate_damage(3, player_armor)

print("Damage taken from hit 1:", hit_1)
print("Damage taken from hit 2:", hit_2)
