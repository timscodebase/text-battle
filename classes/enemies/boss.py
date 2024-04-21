from classes.character import Character
from classes.weapon import Weapon, iron_sword, obsidian_sword

class Boss(Character):
    def __init__(self, name: str, health: int = 100, magic: int = 50, weapon: Weapon = iron_sword) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)

        self.weapon = obsidian_sword