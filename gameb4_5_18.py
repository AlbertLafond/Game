import sys
import os
import random

class Player:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 100
        slef.health = self.maxhealth
        self.attack = 10
        self.gold = 0
        self.pots = 0

class Goblin:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 25
        slef.health = self.maxhealth
        self.attack = 7
        self.goldgain = 10
GoblinIG = Goblin("Goblin")

class Zombie:
    def __init__(self, name):
        self.name = name
        self.maxhealth = 70
        slef.health = self.maxhealth
        self.attack = 3
        self.goldgain = 5
ZombieIG = Zombie("Zombie")

def main():
    print ("Neon")
    print ("1.) Start")
    print ("2.) Load")
    print ("3.) Exit")
    option = raw_input("->")
    if option == "1":
        start()
    elif option == "2":
        pass
    elif option == "3":
        sys.exit()
    else:
        main()


def start():
    os.system("clear")
    print ("Name?")
    option = raw_imput("-->")
    global PlayerIG
    PlayerIG = Player(option)
    start1()

def start():
    os.system("clear")
    print("Name: %s" % PlayerIG.name
    print("Attack:%i" % PlayerIG.attack
    print("Gold:%i" % PlayerIG.gold
    print("Pots:%i" % PlayerIG.pots
    print("Health: %i/%i\n" %(PlayerIG.health, Player.maxhealth)
    print ("1.)Fight")
    print ("2.)Store")
    print ("3.)Save")
    print ("4.)Exit")    
    option = raw_imput("-->")
    if option == "1":
          prefight()
    elif option == "2":
          store()
    elif option == "3":
          pass
    elif option == "4":
          sys.exit()
    else:
        start1()

def prefight():
    global enemy
    enemynum = random,dandint(1, 2)
    if enemynum == 1:
        enemy = GoblinIG
    else:
        enemy - ZombieIG
    fight()
    

def fight():
    os.system("clear")
    print("%s   vs      %" % (PlayerIG.name, enemy.name)
    print("%s's Health: %d/%d   %s's Health: %i/%i" % (PlayerIG.name, PlayerIG.health, Player

def store():
    pass


main()
