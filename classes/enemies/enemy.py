from classes.character import Character
from classes.weapon import Weapon, fists

class Enemy(Character):
    def __init__(self,
                 name: str = "Enemy",
                 health: int = 20,
                 magic: int = 10,
                 weapon: Weapon = fists
                 ) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        
        self.color = "red"
