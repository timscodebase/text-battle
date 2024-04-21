from classes.character import Character
from classes import Weapon, fists
from utils import green, wizard_backstory

class Wizard(Character):
    def __init__(self, name: str, health: int = 75, magic: int = 30, weapon: Weapon = fists) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)

        self.backstory = wizard_backstory(self.name)
        self.color = green
        self.hb_color = "green"

    def fireball(self, target) -> None:
        self.magic -= 10
        target.health -= 10
        print(f"{self.name} threw a fireball at {target.name}!")

    def heal(self, target) -> None:
        if self.magic < 10:
            print(f"{self.name} doesn't have enough magic to heal!")
        else:
            self.magic -= 10
            target.health += 10
            print(f"{self.name} healed {target.name}!")
