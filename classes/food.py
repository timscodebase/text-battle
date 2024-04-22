class Food:
  def __init__(self, name: str, value: int) -> None:
    self.name = name
    self.value = value

  def eat(self, hero) -> None:
    hero.health += self.value
    hero.food_available[self.name] = hero.food_available.get(self.name, 0) - 1


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