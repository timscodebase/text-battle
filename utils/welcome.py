import os
from art import text2art
from utils.colors import green

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