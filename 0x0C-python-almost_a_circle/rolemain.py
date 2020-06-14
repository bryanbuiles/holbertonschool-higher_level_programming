#!/usr/bin/python3
""" 0-main """
from theholbychampion import Basechampion
from theholbychampion import Battle

if __name__ == "__main__":

     
    # Create 2 Warriors
    Name1 = input(str("Ingrese el nombre del primer heroe: "))
    Name2 = input(str("Ingrese el nombre del segundo heroe: "))
    paul = Basechampion(Name1, "human","male", health=50,attack=20, defense=10)
    sam = Basechampion(Name2, "human", "female",health=50,attack=20, defense=10)
 
    # Create Battle object
    battle = Battle(paul, sam)
 
    # Initiate Battle
    battle.startFight()
 