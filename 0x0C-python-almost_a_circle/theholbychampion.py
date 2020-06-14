#!/usr/bin/python3
""" Base.py """
import random
import math
import time

class Basechampion:

    def __init__(self, name="hero", race="Human",gender="Male", level=1, exptonextlevel=100,  currentexp=0, totalexp=0, health=0,attack=0, defense=0, magic=0, speed=0, stat_points=0):
        self.name = name
        self.race = race
        self.gender = gender
        self.level = level
        self.exptonextlevel = exptonextlevel
        self.currentexp = currentexp
        self.totalexp = totalexp
        self.health = health
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.speed = speed
        self.stat_points = stat_points
        
    @property
    def name(self):
        """ Getter for width
        """
        return self.__name

    @name.setter
    def name(self, value):
        """ setter for width """
        self.__name = value
        
    @property
    def race(self):
        """ Getter for width
        """
        return self.__race

    @race.setter
    def race(self, value):
        """ setter for width """
        self.__race = value
        
    @property
    def gender(self):
        """ Getter for width
        """
        return self.__gender

    @gender.setter
    def gender(self, value):
        """ setter for width """
        self.__gender = value
        
    def level_up(self):
        self.totalexp = self.currentexp + self.totalexp
        if self.currentexp >= self.exptonextlevel:
            self.level += self.level
            self.currentexp = 0
            self.exptonextlevel = self.exptonextlevel * 1.5
            print("the warrior {} level up to: {} ".format(self.name, self.level))
        
    def ataque(self):
            # Randomly calculate the attack amount
        # random() returns a value from 0.0 to 1.0
        attkAmt = self.attack * (random.random() + .5)
 
        return attkAmt
 
    def block(self):
 
        # Randomly calculate how much of the attack was blocked
        blockAmt = self.defense * (random.random() + .5)
 
        return blockAmt
    
class Battle:
    
    def __init__(self, warrior1, warrior2):
        self.warrior1 = warrior1
        self.warrior2 = warrior2
        
    def startFight(self):
        

        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.getAttackResult(self.warrior1, self.warrior2) == "Game Over":
                print("Game Over")
                break

            if self.getAttackResult(self.warrior2, self.warrior1) == "Game Over":
                print("Game Over")
                break
    
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.ataque()
 
        warriorBBlockAmt = warriorB.block()
 
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
        if damage2WarriorB < 0:
            damage2WarriorB = 0
 
        warriorB.health = warriorB.health - damage2WarriorB
 
        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2WarriorB))
 
        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))
        time.sleep(5)
        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))
            warriorA.currentexp = 110
            warriorB.currentexp = (warriorB.currentexp * -0.5)
            warriorA.level_up()
            warriorB.level_up()
            return "Game Over"
        else:
            return "Fight Again"
        
