import os
from battle import Battle
from character import Hero, Enemy, Wizard, Boss
from hero_setup_menu import hero_setup_menu
from welcome import welcome

winner = None
game_over = False

welcome()
hero = hero_setup_menu()
hero.tell_story()
enemy = Enemy(name="Evil Cat", health=100, magic=0)

battle = Battle(hero, enemy)


while game_over == False:
  winner = battle.fight()
  print(f"The winner is {winner.name}!")

  input()

