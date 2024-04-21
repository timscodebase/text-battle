from classes.character import Character
from classes.weapon import Weapon, fists

class Zombie(Character):
    def __init__(self,
                 name: str,
                 health: int = 30,
                 magic: int = 10,
                 weapon: Weapon = fists,
                 ) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)

        self.color = "red"
