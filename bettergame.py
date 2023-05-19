import os
import random

def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

class Character():
    def __init__(self, name, level, base_health, base_damage, armor):
        self.level = level
        self.base_health = base_health
        self.base_damage = base_damage
        self.armor = armor
        self.health = self.base_health
        self.name = name

    def attack(self, target):
        # Calculate damage
        if random.randint(1, 20) == 1:
            damage = self.base_damage * 2  # Critical hit
        else:
            damage = self.base_damage
        damage -= target.armor
        damage = max(damage, 0)  # Damage can't be negetive
        print(self.name + " did " + str(damage) + " damage!")
        target.health -= damage
        print(target.name + "'s remaining health: " + str(target.health) + ".")

    def block(self):
        self.armor *= 2
        print(f"{self.name} is blocking")
        return self.armor

    def heal(self):
        heal = random.randint(
            int(0.05*self.base_health), int(0.2*self.base_health))
        self.health += heal
        print(self.name + " regenerated " + str(heal) + " health! " + self.name + " has " + str(self.health) + " health left!")
        return self.health

def spawn_random_enemy(level):
    enemies = ["Bandit", "Skeleton", "Orc"]
    name = random.choice(enemies)
    base_health = random.randint(30, 80) * level
    base_damage = random.randint(10, 20) * level
    armor = random.randint(5, 15) * level
    char = Character(name, level, base_health, base_damage, armor)
    enemy = Enemy(char, name, level, base_health, base_damage, armor)
    return char, enemy

class Enemy():
    def __init__(self, char, name, level, base_health, base_damage, armor):
        self.char = char
        self.base_health = base_health
        self.base_damage = base_damage
        self.base_armor = armor
        self.armor = armor
        self.name = name
        self.level = level
        self.health = base_health
    
    def enemy_move(self, target):
        move = random.randint(1, 3)
        self.armor = self.base_armor
        if move == 1:
            self.char.attack(target)
        elif move == 2:
            self.health = self.char.heal()
        elif move == 3:
            self.armor = self.char.block()

class Player():
    def __init__(self, char):
        self.char = char
        self.base_health = 100
        self.base_damage = 15
        self.armor = 8
        self.level = 1
        self.health = self.base_health
        self.name = "Player"

    def level_up(self):
        self.level += 1
        print("You leveled up! Choose an attribute to upgrade: (1) Base health \
(+20), (2) Base damage (+3), (3) Armor (+2)")
        choice = input()
        if choice == "1":
            self.base_health += 20
        elif choice == "2":
            self.base_damage += 3
        elif choice == "3":
            self.armor += 2
    
    def player_move(self, target):
        print("Choose an action:")
        print("1. Attack")
        print("2. Heal")
        print("3. Block")
        # Prompt player for an action
        choice = input("Enter your choice: ")
        try:
            choice_int = int(choice)
            if choice_int == 1:
                self.char.attack(target)
            elif choice_int == 2:
                self.health = self.char.heal()
            elif choice_int == 3:
                self.armor = self.char.block()
            else:
                print("Invalid option")
        except:
            print("Invalid option.")


def main():
    # Main game loop
    running = True
    print("Welcome to the dungeon fighting game!")
    char = Character("Player", 1, 100, 15, 8)
    player = Player(char)
    while running:
        print(f"You are on level {player.level}")
        input("Press enter to continue...")
        clear()

        # Spawn a random enemy
        enemy_tuple = spawn_random_enemy(player.level)
        enemy = enemy_tuple[1]
        enemy_char = enemy_tuple[0]
        print(f"A {enemy.name} has appeared!")

        while enemy_char.health > 0 or player.health > 0:
            player.player_move(enemy)
            enemy.enemy_move(player)

        if enemy_char.health > 0:
            # Enemy defeated the player
            # Handle game over condition
            print("You have been defeated. Game over!")
            running = False
            break

main()