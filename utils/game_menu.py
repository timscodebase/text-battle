import os
import random
from utils.colors import *
from classes.enemies import Zombie
from classes import Battle
from time import sleep

def eat(hero) -> None:
  if hero.food_available > 0:
    print('You eat')
    hero.health += 10
    print(f'Your health is now {hero.health}')
    hero.food_available -= 1
    print(f'Your food is now {hero.food_available}')
    sleep(1)
  else:
    print('You don\'t have any food\nTry to explore to find something to eat')
    sleep(1)

  game_menu(hero)

def explore(hero) -> None:
  found_food = random.choice([True, False, False])
  if found_food:
    print('You found food')
    sleep(1)
    hero.food_available += 1
    print(f'Your food is now {hero.food_available}')
    sleep(1)
  else:
    print('You found nothing')
    sleep(1)

  game_menu(hero)

def walk(hero) -> None:
  fight = random.choice([True, False, False])
  if fight:
    zombie_instance = Zombie(name='Zombie')  # Instantiate the Zombie class
    Battle(hero, zombie_instance).fight()
  else:
    print('You walk')
    sleep(1)

  game_menu(hero)


def game_menu(hero) -> None:
  os.system('clear')
  action = input('Choose your action:\n(1) Walk\n(2) Explore\n(3) Eat\n\n(Q) Quit:\n\n')
  
  if action not in ['1', '2', '3', 'Q', 'q']:
    print(red |'Invalid input')
    game_menu(hero)
  elif action == '1': # Walk
    walk(hero)
  elif action == '2': # Explore
    explore(hero)
  elif action == '3': # Eat
    eat(hero)
  elif action == 'q' or action == 'Q':
    quit()