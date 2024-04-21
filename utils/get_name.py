import os

def get_name() -> str:
  name = input('Name your hero\n\n')
  # if name empty string
  while name == '':
    os.system("clear")
    name = input('Name your hero\n\n')
    get_name()

  return name
