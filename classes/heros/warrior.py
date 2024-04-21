from classes.character import Character
from classes import Weapon, obsidian_sword
from utils import grey, warrior_backstory

class Warrior(Character):
    def __init__(self, name: str, health: int = 100, magic: int = 10, weapon: Weapon = obsidian_sword) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)

        self.color = grey
        self.hb_color = "grey"
        self.backstory = warrior_backstory(self.name)

    def jab(self, target) -> None:
        if self.weapon.type != "sharp":
            print("You can't jab with a blunt weapon.  Look for something sharp!")
        else:
            target.health -= 8
            print(f"{self.name} jabbed at {target.name}!")
