from .hero import Hero
from classes import HealthBar, Weapon, fists, obsidian_sword
from utils import grey, warrior_backstory

class Warrior(Hero):
    def __init__(self, name: str, health: int = 100, magic: int = 10, weapon: Weapon = obsidian_sword) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.weapon = fists
        self.backstory = warrior_backstory(self.name)
        self.color = grey
        self.health_bar = HealthBar(self, color="grey")

    def jab(self, target) -> None:
        if self.weapon.type != "sharp":
            print("You can't jab with a blunt weapon.  Look for something sharp!")
        else:
            target.health -= 8
            print(f"{self.name} jabbed at {target.name}!")
