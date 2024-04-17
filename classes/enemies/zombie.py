from .enemy import Enemy
from classes import HealthBar, Weapon, fists

class Zombie(Enemy):
    def __init__(self, name: str, health: int = 20, magic: int = 0, weapon: Weapon = fists) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.health_bar = HealthBar(self, color="green2")
