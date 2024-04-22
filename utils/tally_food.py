def tally_food(hero) -> int:
  food_count = 0
  for food in hero.food_available:
    food_count += hero.food_available[food]
  return food_count