# There is a no Block Scope in Python!

game_level = 10
enemies = ["Skeleton","Zombie","Alien"]

def create_enemy():
    if game_level< 5:
        new_enemy = enemies[0]

    print(new_enemy)

create_enemy()