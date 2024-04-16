import os
from battle import Battle
from character import Hero, Enemy, Wizard, Boss
from game_menu import game_menu
from hero_setup_menu import hero_setup_menu
from welcome import welcome

# Global variables 
winner = None
game_over = False


# Game Setup
welcome()
hero = hero_setup_menu()

os.system("clear")
hero.tell_story()

enemy = Enemy(name="Evil Cat", health=100, magic=0)
battle = Battle(hero, enemy)

def text_adv() -> None:
  # Game Loop
  global game_over
  while game_over == False:
    os.system("clear")
    game_menu(hero)
    input()

if __name__ == '__main__':
  text_adv()

