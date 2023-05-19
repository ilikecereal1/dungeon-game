print("Hello World!")
import os
import random


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def spawn_random_enemy(level):
    enemies = [Bandit, Skeleton, Orc]
    enemy_class = random.choice(enemies)
    base_health = random.randint(30, 80) * level
    base_damage = random.randint(10, 20) * level
    armor = random.randint(5, 15) * level
    enemy = enemy_class(level, base_health, base_damage, armor)
    return enemy


class Character():
    def __init__(self, level, base_health, base_damage, armor):
        self.level = level
        self.base_health = base_health
        self.base_damage = base_damage
        self.armor = armor
        self.health = self.base_health
        self.critical_chance = 5

    def attack(self, target):
        # Calculate damage
        if random.randint(1, 100) <= self.critical_chance:
            damage = self.base_damage * 2  # Critical hit
        else:
            damage = self.base_damage
        damage -= target.armor
        damage = max(damage, 0)  # Damage can't be negetive

        if target.health <= 0:
            print(f"{target.__class__.__name__} died!")
            return True

        return False

    def block(self):
        self.armor *= 2
        print(f"{self.__class__,__name__} is blocking")

    def heal(self):
        self.health = random.randint(
            int(0.05*self.base_health), int(0.2*self.base_health))
        self.health += self.health
        return self.health


class Bandit(Character):
    def __init__(self, level, base_health, base_damage, armor):
        super().__init__(level, base_health, base_damage, armor)
        base_health = 50
        base_damage = 30
        armor = 25


class Skeleton(Character):
    def __init__(self,  level, base_health, base_damage, armor):
        super().__init__(level, base_health, base_damage, armor)
        self.base_health = 30
        self.base_damage = 50
        self.armor = 0


class Orc(Character):
    def __init__(self, level, base_health, base_damage, armor):
        super().__init__(level, base_health, base_damage, armor)
        self.base_health = 80
        self.base_damage = 15
        self.armor = 40


class Player(Character):
    def __init__(self, level=1, base_health=100, base_damage=15, armor=8):
        super().__init__(level, base_health, base_damage, armor)
        self.base_health = 100
        self.base_damage = 15
        self.armor = 8
        self.level = 1

    def level_up(self):
        print("You leveled up! Choose an attribute to upgrade: (1) Base health \
(+20), (2) Base damage (+3), (3) Armor (+2)")
        choice = input()
        if choice == "1":
            self.base_health += 20
        elif choice == "2":
            self.base_damage += 3
        elif choice == "3":
            self.armor += 2


def player_move(char, target):
    print("Choose an action:")
    print("1. Attack")
    print("2. Heal")
    print("3. Block")
    # Prompt player for an action
    choice = input("Enter your choice: ")
    if choice.isnumeric():
        choice_int = int(choice)
        if choice_int == 1:
            char.attack(target)
        elif choice_int == 2:
            char.heal()
        elif choice_int == 3:
            char.block()
        else:
            print("Invalid option.")
            input("Press enter to continue...")
            player_move(char, target)
    else:
        print("Invalid option.")
        input("Press enter to continue...")
        player_move(char, target)
    
    return choice


def enemy_move(enemy, target):
    move = random.randint(1, 3)
    if move == 1:
        enemy.attack(target)
    elif move == 2:
        enemy.heal()
    elif move == 3:
        enemy.block()


def main():
    # Main game loop
    running = True
    print("Welcome to the dungeon fighting game!")
    char = Character()
    player = Player(char)
    while running:
        print(f"You are on level {player.level}")
        input("Press enter to continue...")
        clear()

        # Spawn a random enemy
        enemy = spawn_random_enemy(player.level)
        print(f"A {enemy.__class__.__name__} has appeared!")

        while enemy.health > 0 or player.health > 0:
            if enemy.attack(player):
                # Enemy defeated the player
                # Handle game over condition
                print("You have been defeated. Game over!")
                running = False
                break 
                
            elif choice2 == "1":
                # Attack
                if player.attack(enemy):
                    pass
                    # Player defeated the enemy
                    # Update game state, level up player, etc.
                        
            elif choice == "2":
                # Heal
                healed_amount = player.heal()
                print(f"You healed for {healed_amount} health.")
                if enemy.attack(player):
                    # Enemy defeared the player
                    # Handle game over condition
                    print("You have been defeated. Game over!")
                    running = False
                    break
            elif choice == "3":
                # Block
                player.block()
                if enemy.attack(player):
                    # Enemy defeated the player
                    # Handle game over condition
                    print("You have been defeated. Game over!")
                    running = False
                    break


main()