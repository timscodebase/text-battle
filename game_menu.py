import os
import random
from utils.colors import *
from classes.enemies import Enemy

def eat(hero) -> None:
  if hero.food_available > 0:
    print('You eat')
    hero.health += 10
    print(f'Your health is now {hero.health}')
    hero.food_available -= 1
  else:
    print('You don\'t have any food\nTry to explore to find something to eat')

  game_menu(hero)

def explore(hero) -> None:
  found_food = random.choice([True, False, False])
  if found_food:
    print('You found food')
    hero.food_available += 1
  else:
    print('You found nothing')

  game_menu(hero)

def walk(hero) -> None:
  fight = random.choice([True, False, False])
  if fight:
    # enemy = random.choice([Zombie, Dragon, Boss])()
    hero.battle(Enemy)
  else:
    print('You walk')


def game_menu(hero) -> None:
  action = input('Choose your action:\n(1) Walk\n(2) Explore\n(3) Eat\n\n(Q) Quit:\n\n')
  
  os.system('clear')
  
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