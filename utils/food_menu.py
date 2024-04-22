from .colors import red

def food_menu(hero):
  food_options = []
  for food in hero.food_available:
    if hero.food_available.get(food, 0):
      food_options.append(food)

  if len(food_options) == 0:
    print('You don\'t have any food to eat')
    return
  print(f'Food options: {food_options}')