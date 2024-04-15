# from main import game_over
from character import Warrior, Wizard, Cleric, Thief

def quit():
  print('Goodbye!')
  global game_over
  game_over = True

def hero_setup_menu() -> None:
  name = input('Name your hero\n\n')
  action = input('Choose your action:\n(1) Warrior\n(2) Wizard\n(3) Cleric\n(4) Thief\n\n(Q) Quit:\n\n')
  hero = None

  if action in ['1', '2', '3', '4']:
    if action == '1':
      hero = Warrior(name=name)
    elif action == '2':
      hero = Wizard(name=name)
    elif action == '3':
      hero = Cleric(name=name)
    elif action == '4':
      hero = Thief(name=name)
    else:
      quit()

  return hero