import os
from colors import *

def game_menu(character):
  action = input('Choose your action:\n(1) Walk\n(2) Explore\n(3) Eat\n\n(Q) Quit:\n\n')
  
  if action not in ['1', '2', '3', 'Q', 'q']:
    os.system('clear')
    print(red |'Invalid input')
    game_menu(character)
  elif action == '1':
    print('You walk')
  elif action == '2':
    print('You explore')
  elif action == '3':
    print('You eat')
  elif action == 'q' or action == 'Q':
    quit()