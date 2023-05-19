''' Dungeon fighting game
Made by Isaac Chai
Rewriten by Isaac Fu'''

import os
import subprocess # os.system is depriciated
import random
import time

class Colors:
    '''Colors class:reset all colors with colors.reset; two
sub classes fg for foreground
and bg for background; use as colors.subclass.colorname.
i.e. colors.fg.red or colors.bg.greenalso, the generic bold, disable,
underline, reverse, strike through,
and invisible work with the main class i.e. colors.bold'''
    reset = '\033[0m'
    bold = '\033[01m'
    disable = '\033[02m'
    underline = '\033[04m'
    reverse = '\033[07m'
    strikethrough = '\033[09m'
    invisible = '\033[08m'

    class Fg:
        '''Foreground colors'''
        black = '\033[30m'
        red = '\033[31m'
        green = '\033[32m'
        orange = '\033[33m'
        blue = '\033[34m'
        purple = '\033[35m'
        cyan = '\033[36m'
        lightgrey = '\033[37m'
        darkgrey = '\033[90m'
        lightred = '\033[91m'
        lightgreen = '\033[92m'
        yellow = '\033[93m'
        lightblue = '\033[94m'
        pink = '\033[95m'
        lightcyan = '\033[96m'

    class Bg:
        '''Background colors'''
        black = '\033[40m'
        red = '\033[41m'
        green = '\033[42m'
        orange = '\033[43m'
        blue = '\033[44m'
        purple = '\033[45m'
        cyan = '\033[46m'
        lightgrey = '\033[47m'

def wait():
    '''Waits until a user presses any key'''
    if os.name == "nt":
        subprocess.call("pause", shell=True)
    else:
        subprocess.call("/bin/bash -c 'read -s -n 1 -p \"Press any key to continue...\"'"\
                        , shell=True)
        print()

def clear():
    '''Clears the terminal'''
    if os.name == "nt":
        subprocess.call("cls", shell=True)
    else:
        subprocess.call("clear", shell=True)

class Character():
    '''Class for all characters to interact with the game'''
    def __init__(self, args):
        self.name = args[0]
        self.base_health = args[1]
        self.base_damage = args[2]
        self.health = args[1]
        self.level = args[3]
        self.base_armor = args[4]
        self.armor = args[4]

    def attack(self, target):
        '''Attacks another character'''
        self.armor = self.base_armor
        # Calculate damage
        if random.randint(1, 10) == 1:
            damage = self.base_damage * 2  # Critical hit
        else:
            damage = self.base_damage
        damage -= target.armor
        damage = max(damage, 0)  # Damage can't be negetive
        standardprint(self.name + " did " + str(damage) + f" damage to {target.name}!")
        target.health -= damage
        standardprint(f"{target.name} now has {str(target.health)}!")

    def block(self):
        '''Doubles armor to reduce damage'''
        self.armor = self.base_armor
        self.armor *= 2
        standardprint(f"{self.name} is blocking")

    def heal(self):
        '''Heals the character'''
        self.armor = self.base_armor
        heal = random.randint(int(0.05*self.base_health), int(0.2*self.base_health))
        self.health += heal
        standardprint(f"{self.name} regenerated {str(heal)} health points!")
        standardprint(f"{self.name} now has {str(self.health)} health points!")

def spawn_random_enemy(level):
    '''Spawns a random enemy'''
    enemies = ["Bandit", "Skeleton", "Orc"]
    name = random.choice(enemies)
    if name == "Bandit":
        base_health = random.randint(90, 110) * level
        base_damage = random.randint(10, 20) * level
        armor = random.randint(1, 5)
    elif name == "Skeleton":
        base_health = random.randint(30, 80) * level
        base_damage = random.randint(10, 20) * level
        armor = 0
    else:
        base_health = random.randint(30, 80) * level
        base_damage = random.randint(10, 20) * level
        armor = random.randint(5, 15) * level
    enemy = Character([name, base_health, base_damage, level, armor])
    return enemy

def player_move(char, target):
    '''Input for player to make a move'''
    standardprint("Choose an action:")
    print("1. Attack")
    print("2. Heal")
    print("3. Block")
    # Prompt player for an action
    choice = standardinput("Enter your choice: ")
    if choice == "1":
        char.attack(target)
    elif choice == "2":
        char.heal()
    elif choice == "3":
        char.block()
    else:
        standardprint("Invalid option")
        player_move(char, target)

def auto_move(char, target):
    '''Automatically make a move'''
    move = random.randint(1, 3)
    if move == 1:
        char.attack(target)
    elif move == 2:
        char.heal()
    elif move == 3:
        char.block()

def level_up(char):
    '''Levels up a character'''
    char.level += 1
    choice = input("You leveled up! Choose an attribute to upgrade: (1) Base health \
(+20), (2) Base damage (+3), (3) Armor (+2): ")
    if choice == "1":
        char.base_health += 20
    elif choice == "2":
        char.base_damage += 3
    elif choice == "3":
        char.base_armor += 2
    else:
        print("Invalid option.")
        level_up(char)

def print_enemy(name):
    '''Prints an enemy with only ascii text!'''
    if os.name == "nt":
        subprocess.call("color", shell=True)
    if name == "Orc":
        print(f"""\x1B[0m \
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;236m.\x1B[38;5;187m%\x1B[38;5;241m*\x1B[38;5;234m.\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;065m*\x1B[38;5;239m,\x1B[38;5;239m,\x1B[38;5;238m,\x1B[38;5;237m,\x1B[38;5;233m \x1B[38;5;241m*\x1B[38;5;187m%\x1B[38;5;236m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;101m/\x1B[38;5;150m#\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;065m/\x1B[38;5;065m/\x1B[38;5;065m*\x1B[38;5;144m(\x1B[38;5;059m*\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;237m,\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;239m*\x1B[38;5;233m \x1B[38;5;239m*\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;234m.\x1B[38;5;232m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m/\x1B[38;5;095m/\x1B[38;5;237m,\x1B[38;5;232m \x1B[38;5;237m,\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;064m*\x1B[38;5;022m,\x1B[38;5;239m*\x1B[38;5;237m,\x1B[38;5;022m.\x1B[38;5;022m.\x1B[38;5;022m.\x1B[38;5;237m,\x1B[38;5;238m,\x1B[38;5;233m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m,\x1B[38;5;095m/\x1B[38;5;137m(\x1B[38;5;101m/\x1B[38;5;094m*\x1B[38;5;094m*\x1B[38;5;235m.\x1B[38;5;235m.\x1B[38;5;237m,\x1B[38;5;065m*\x1B[38;5;065m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;065m/\x1B[38;5;239m*\x1B[38;5;236m.\x1B[38;5;234m.\x1B[38;5;236m.\x1B[38;5;058m,\x1B[38;5;234m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;232m \x1B[38;5;058m,\x1B[38;5;003m*\x1B[38;5;094m*\x1B[38;5;094m*\x1B[38;5;094m*\x1B[38;5;094m*\x1B[38;5;094m*\x1B[38;5;058m,\x1B[38;5;236m.\x1B[38;5;233m \x1B[38;5;236m.\x1B[38;5;239m,\x1B[38;5;239m,\x1B[38;5;239m,\x1B[38;5;239m,\x1B[38;5;238m,\x1B[38;5;234m.\x1B[38;5;237m,\x1B[38;5;065m/\x1B[38;5;003m*\x1B[38;5;094m*\x1B[38;5;094m*\x1B[38;5;058m,\x1B[38;5;234m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;238m,\x1B[38;5;058m,\x1B[38;5;058m,\x1B[38;5;058m,\x1B[38;5;058m,\x1B[38;5;240m*\x1B[38;5;065m/\x1B[38;5;065m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;003m*\x1B[38;5;058m*\x1B[38;5;058m,\x1B[38;5;239m*\x1B[38;5;238m,\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;239m,\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;065m*\x1B[38;5;237m,\x1B[38;5;065m*\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;065m*\x1B[38;5;065m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;065m*\x1B[38;5;233m \x1B[38;5;236m.\x1B[38;5;065m*\x1B[38;5;065m/\x1B[38;5;071m/\x1B[38;5;065m*\x1B[38;5;235m.\x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;016m \x1B[38;5;239m,\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;065m*\x1B[38;5;239m*\x1B[38;5;235m.\x1B[38;5;232m \x1B[38;5;237m,\x1B[38;5;239m*\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;239m*\x1B[38;5;237m,\x1B[38;5;233m \x1B[38;5;235m.\x1B[38;5;240m*\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;065m*\x1B[38;5;240m*\x1B[38;5;234m.\x1B[38;5;016m 
\x1B[0m \x1B[38;5;016m \x1B[38;5;239m,\x1B[38;5;107m(\x1B[38;5;144m#\x1B[38;5;101m/\x1B[38;5;058m*\x1B[38;5;237m,\x1B[38;5;232m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;232m \x1B[38;5;236m.\x1B[38;5;239m,\x1B[38;5;065m*\x1B[38;5;065m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;071m/\x1B[38;5;065m*\x1B[38;5;238m,\x1B[38;5;239m,\x1B[38;5;065m/\x1B[38;5;071m(\x1B[38;5;071m/\x1B[38;5;065m/\x1B[38;5;239m*\x1B[38;5;233m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;239m*\x1B[38;5;094m*\x1B[38;5;101m*\x1B[38;5;065m/\x1B[38;5;065m/\x1B[38;5;065m/\x1B[38;5;237m,\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;234m.\x1B[38;5;065m/\x1B[38;5;238m,\x1B[38;5;236m.\x1B[38;5;236m.\x1B[38;5;236m.\x1B[38;5;238m,\x1B[38;5;065m/\x1B[38;5;234m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;236m.\x1B[38;5;236m.\x1B[38;5;236m.\x1B[38;5;235m.\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;233m \x1B[38;5;239m*\x1B[38;5;234m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;234m.\x1B[38;5;239m*\x1B[38;5;233m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[0m \
{Colors.Fg.lightgrey}""")
    if name == "Skeleton":
        print(f"""\x1B[38;5;m \
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;241m*\x1B[38;5;145m#\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;241m*\x1B[38;5;145m#\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;241m*\x1B[38;5;145m#\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;007m%\x1B[38;5;015m@\x1B[38;5;015m@\x1B[38;5;015m@\x1B[38;5;015m@\x1B[38;5;015m@\x1B[38;5;015m@\x1B[38;5;245m(\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;242m/\x1B[38;5;007m%\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;124m,\x1B[38;5;217m%\x1B[38;5;015m@\x1B[38;5;224m&\x1B[38;5;009m*\x1B[38;5;224m&\x1B[38;5;015m@\x1B[38;5;245m(\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;239m,\x1B[38;5;244m(\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;245m(\x1B[38;5;247m#\x1B[38;5;236m.\x1B[38;5;015m@\x1B[38;5;236m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;242m/\x1B[38;5;241m*\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;095m*\x1B[38;5;173m(\x1B[38;5;166m*\x1B[38;5;166m*\x1B[38;5;233m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;016m \x1B[38;5;242m/\x1B[38;5;015m@\x1B[38;5;255m@\x1B[38;5;234m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;007m%\x1B[38;5;242m/\x1B[38;5;059m*\x1B[38;5;255m@\x1B[38;5;145m#\x1B[38;5;234m.\x1B[38;5;247m#\x1B[38;5;253m&\x1B[38;5;244m(\x1B[38;5;232m \x1B[38;5;174m#\x1B[38;5;216m%\x1B[38;5;167m(\x1B[38;5;088m,\x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;052m.\x1B[38;5;001m,\x1B[38;5;016m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;145m#\x1B[38;5;015m@\x1B[38;5;254m@\x1B[38;5;247m(\x1B[38;5;232m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;238m,\x1B[38;5;250m%\x1B[38;5;015m@\x1B[38;5;236m.\x1B[38;5;247m#\x1B[38;5;015m@\x1B[38;5;007m%\x1B[38;5;232m \x1B[38;5;130m*\x1B[38;5;166m*\x1B[38;5;052m.\x1B[38;5;239m*\x1B[38;5;015m@\x1B[38;5;254m@\x1B[38;5;254m@\x1B[38;5;241m*\x1B[38;5;016m \x1B[38;5;016m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;234m.\x1B[38;5;145m#\x1B[38;5;255m@\x1B[38;5;059m*\x1B[38;5;239m,\x1B[38;5;244m(\x1B[38;5;232m \x1B[38;5;130m*\x1B[38;5;166m*\x1B[38;5;052m.\x1B[38;5;238m,\x1B[38;5;188m&\x1B[38;5;249m#\x1B[38;5;145m#\x1B[38;5;239m,\x1B[38;5;016m \x1B[38;5;016m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;235m.\x1B[38;5;248m#\x1B[38;5;233m \x1B[38;5;088m,\x1B[38;5;166m*\x1B[38;5;166m*\x1B[38;5;166m*\x1B[38;5;166m*\x1B[38;5;166m*\x1B[38;5;052m.\x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;016m \x1B[38;5;252m&\x1B[38;5;015m@\x1B[38;5;015m@\x1B[38;5;015m@\x1B[38;5;015m@\x1B[38;5;250m%\x1B[38;5;237m,\x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;016m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;236m.\x1B[38;5;015m@\x1B[38;5;236m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;232m \x1B[38;5;247m(\x1B[38;5;237m,\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;016m \x1B[38;5;234m.\x1B[38;5;145m#\x1B[38;5;234m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;235m.\x1B[38;5;248m#\x1B[38;5;233m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;059m*\x1B[38;5;252m&\x1B[38;5;016m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;145m#\x1B[38;5;244m/\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;007m%\x1B[38;5;252m&\x1B[38;5;145m#\x1B[38;5;245m(\x1B[38;5;016m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;233m \x1B[38;5;188m&\x1B[38;5;251m%\x1B[38;5;145m#\x1B[38;5;243m/\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m {Colors.Fg.lightgrey}""")
    if name == "Bandit":
        print(f"""\x1B[0m \
\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m/\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;m/\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m,\x1B[38;5;m(\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;179m#\x1B[38;5;m/\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m,\x1B[38;5;m(\x1B[38;5;179m#\x1B[38;5;180m%\x1B[38;5;180m%\x1B[38;5;217m%\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;m%\x1B[38;5;m*\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m*\x1B[38;5;m#\x1B[38;5;216m%\x1B[38;5;217m%\x1B[38;5;217m%\x1B[38;5;137m(\x1B[38;5;239m,\x1B[38;5;241m*\x1B[38;5;144m#\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;144m#\x1B[38;5;241m*\x1B[38;5;m.\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m*\x1B[38;5;m#\x1B[38;5;216m%\x1B[38;5;217m%\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;223m&\x1B[38;5;m%\x1B[38;5;m*\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m,\x1B[38;5;131m*\x1B[38;5;131m*\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;m*\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m*\x1B[38;5;247m#\x1B[38;5;248m#\x1B[38;5;250m%\x1B[38;5;248m#\x1B[38;5;131m/\x1B[38;5;131m*\x1B[38;5;131m*\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;138m(\x1B[38;5;250m%\x1B[38;5;m/\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m,\x1B[38;5;095m/\x1B[38;5;101m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;131m/\x1B[38;5;131m*\x1B[38;5;131m*\x1B[38;5;131m*\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;131m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;m*\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m*\x1B[38;5;m*\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m*\x1B[38;5;095m/\x1B[38;5;101m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;m/\x1B[38;5;m,\x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m*\x1B[38;5;m*\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m*\x1B[38;5;m*\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m*\x1B[38;5;095m/\x1B[38;5;101m/\x1B[38;5;137m/\x1B[38;5;101m/\x1B[38;5;095m/\x1B[38;5;095m/\x1B[38;5;101m/\x1B[38;5;137m/\x1B[38;5;101m/\x1B[38;5;095m/\x1B[38;5;101m/\x1B[38;5;101m/\x1B[38;5;m/\x1B[38;5;m,\x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m*\x1B[38;5;m*\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;238m,\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m*\x1B[38;5;095m/\x1B[38;5;101m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;m/\x1B[38;5;m,\x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m,\x1B[38;5;m,\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;238m,\x1B[38;5;241m*\x1B[38;5;102m(\x1B[38;5;247m(\x1B[38;5;247m(\x1B[38;5;247m#\x1B[38;5;248m#\x1B[38;5;250m%\x1B[38;5;247m#\x1B[38;5;240m*\x1B[38;5;235m.\x1B[38;5;235m.\x1B[38;5;235m.\x1B[38;5;236m.\x1B[38;5;237m,\x1B[38;5;238m,\x1B[38;5;236m,\x1B[38;5;235m.\x1B[38;5;235m.\x1B[38;5;235m.\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;237m,\x1B[38;5;241m*\x1B[38;5;246m(\x1B[38;5;247m(\x1B[38;5;247m(\x1B[38;5;247m(\x1B[38;5;247m(
\x1B[0m \x1B[38;5;m \x1B[38;5;m*\x1B[38;5;m#\x1B[38;5;007m%\x1B[38;5;007m%\x1B[38;5;007m%\x1B[38;5;144m#\x1B[38;5;101m/\x1B[38;5;095m/\x1B[38;5;101m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;137m/\x1B[38;5;m/\x1B[38;5;m,\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m/\x1B[38;5;m%\x1B[38;5;007m%\x1B[38;5;007m%\x1B[38;5;007m%\x1B[38;5;007m%
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m,\x1B[38;5;m/\x1B[38;5;m/\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m/\x1B[38;5;m(\x1B[38;5;m,\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m,\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m,\x1B[38;5;m,\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m 
\x1B[0m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m.\x1B[38;5;m,\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m,\x1B[38;5;m,\x1B[38;5;m.\x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \x1B[38;5;m \
{Colors.Fg.lightgrey}""")

def betterprint(text, char, start, end):
    '''Prints the text with a delay'''
    if char == "":
        betterprint(text, text[0], start, end)
    else:
        print("\r", end="")
        if len(char) == len(text):
            print(text, end="")
            time.sleep(end)
        else:
            print(char, end="")
            time.sleep(start)
            betterprint(text, f"{char}{text[len(char)]}", start, end)

def standardprint(text):
    '''Standardize betterprint'''
    betterprint(text, "", 0.01, 0.03)
    print()

def standardinput(text):
    '''Standardize betterprint for input'''
    betterprint(text, "", 0.01, 0.03)
    print("\r", end="")
    return input(text)

def main():
    '''Main game loop'''
    running = True
    standardprint("Welcome to the dungeon fighting game!")
    while True:
        stats = standardinput("Choose your stats, (1) more raw power but can die easily (2) balanced (3) better defence: ")
        if stats == "1" or stats == "2" or stats == "3":
            character_name = standardinput("Choose a name for the character: ")
            if stats == "1":
                player = Character([character_name, 50, 20, 1, 0])
                break
            elif stats == "2":
                player = Character([character_name, 100, 15, 1, 8])
                break
            elif stats == "3":
                player = Character([character_name, 150, 10, 1, 16])
                break
        else:
            standardprint("Invalid choice! Please enter your choice again.")


    while running:
        standardprint(f"You are on level {player.level}")
        wait()
        clear()

        # Spawn a random enemy
        enemy = spawn_random_enemy(player.level)
        standardprint(f"A {enemy.name} has appeared!")

        while True:
            print_enemy(enemy.name)
            player_move(player, enemy)
            if enemy.health < 0:
                # Player defeated the enemy
                # Start again
                standardprint(f"You have defeated the {enemy.name}! You gain one level!")
                level_up(player)
                wait()
                break
            wait()
            auto_move(enemy, player)
            if player.health < 0:
                # Enemy defeated the player
                # Handle game over condition
                standardprint("You have been defeated. Game over!")
                running = False
                break
            wait()
            clear()

try:
    main()
except KeyboardInterrupt:
    clear()
    standardprint("Exited the game.")
