from .enemy import Enemy
from classes import HealthBar, Weapon, fists

class Dragon(Enemy):
    def __init__(self, name: str, health: int = 50, magic: int = 20, weapon: Weapon = fists) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.health_bar = HealthBar(self, color="blue3")
