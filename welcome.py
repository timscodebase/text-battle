import os
from art import *
from colors import *
# from utils import create_character, greet

HERO = "Papi"

TITLE = text2art(f'''
  Welcome to
  {HERO}'s Text
  Adventure!
''')

def welcome():
  os.system('clear')
  print(green | TITLE)

  input('Press any key to continue...\n\n')