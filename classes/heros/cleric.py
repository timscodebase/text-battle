from classes.character import Character
from utils import cleric_backstory

class Cleric(Character):
  def __init__(self, name: str, health: int = 75, magic: int = 30) -> None:
    super().__init__(name=name, health=health, magic=magic)

    self.color = "blue"
    self.backstory = cleric_backstory(self.name)

  def heal(self, target) -> None:
    if self.magic < 10:
      print(f"{self.name} doesn't have enough magic to heal!")
    else:
      self.magic -= 10
      target.health += 20
      print(f"{self.name} healed {target.name}!")