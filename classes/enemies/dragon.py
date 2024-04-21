from classes.character import Character
from classes.weapon import  Weapon, fists

class Dragon(Character):
    def __init__(self, name: str, health: int = 50, magic: int = 20, weapon: Weapon = fists) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)

        self.color="blue3"
