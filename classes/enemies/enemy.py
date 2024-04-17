from classes import Character
from classes import HealthBar, Weapon, fists

class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int = 20,
                 magic: int = 10,
                 weapon: Weapon = fists
                 ) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.weapon = weapon

        self.health_bar = HealthBar(self, color="red")
