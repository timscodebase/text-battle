import os
from classes import Battle
from classes import fists
from classes.enemies import Zombie
from utils.game_menu import game_menu
from utils.hero_setup_menu import hero_setup_menu
from welcome import welcome

# Global variables 
winner = None
game_over = False

# Game Setup
welcome()
hero = hero_setup_menu()  
zombie = Zombie("Zombie", health=30, magic=10, weapon=fists)


os.system("clear")
hero.tell_story()

def text_adv() -> None:
  # Game Loop
  global game_over
  while game_over == False:
    os.system("clear")
    game_menu(hero)
    input()

if __name__ == '__main__':
  text_adv()

