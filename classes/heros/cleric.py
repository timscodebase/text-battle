from classes import Weapon, fists
from classes.character import Character
from utils import cleric_backstory, blue

class Cleric(Character):
  def __init__(self, name: str, health: int = 100, magic: int = 10, weapon: Weapon = fists) -> None:
    super().__init__(name=name, health=health, magic=magic, weapon=weapon)

    self.color = blue
    self.hb_color = "blue"
    self.backstory = cleric_backstory(self.name)

  def heal(self, target) -> None:
    if self.magic < 10:
      print(f"{self.name} doesn't have enough magic to heal!")
    else:
      self.magic -= 10
      target.health += 20
      print(f"{self.name} healed {target.name}!")