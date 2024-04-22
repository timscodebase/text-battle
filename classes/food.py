class Food:
  def __init__(self, name: str, value: int) -> None:
    self.name = name
    self.value = value

  def eat(self, hero) -> None:
    # create a list of food options based on food available if amount > 0
    food_options = []
    for food in hero.food_available:
      if hero.food_available.get(food, 0):
        food_options.append(food)
    print(f"Food options: {food_options}")
    # if there are no food options, return
    if len(food_options) == 0:
      print("You don't have any food to eat")
      return
    # hero.health += self.value
    # hero.food_available[self.name] = hero.food_available.get(self.name, 0) - 1


class Apple(Food):
  def __init__(self) -> None:
    super().__init__(name="apple", value=5)

class Bread(Food):
  def __init__(self) -> None:
    super().__init__(name="bread", value=10)

class Steak(Food):
  def __init__(self) -> None:
    super().__init__(name="steak", value=20)

class GoldenApple(Food):
  def __init__(self) -> None:
    super().__init__(name="golden apple", value=50)