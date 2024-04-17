import os
from art import *
from utils.colors import *

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