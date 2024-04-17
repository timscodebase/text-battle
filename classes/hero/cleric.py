from .hero import Hero
from classes import HealthBar, Weapon, fists
from utils import cleric_backstory, purple


class Cleric(Hero):
    def __init__(self, name: str, health: int = 100, magic: int = 30, weapon: Weapon = fists) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.weapon = fists
        self.backstory = cleric_backstory(self.name)
        self.color = purple
        self.health_bar = HealthBar(self, color=str(self.color))

    def heal(self, target) -> None:
        if self.magic < 10:
            print(f"{self.name} doesn't have enough magic to heal!")
        else:
            self.magic -= 10
            target.health += 20
            print(f"{self.name} healed {target.name}!")


            print(f"{self.name} punched at {target.name}!")
