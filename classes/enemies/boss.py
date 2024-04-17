from .enemy import Enemy
from classes import HealthBar, Weapon, iron_sword, obsidian_sword

class Boss(Enemy):
    def __init__(self, name: str, health: int = 100, magic: int = 50, weapon: Weapon = iron_sword) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.health_bar = HealthBar(self, color="yellow")
        self.weapon = obsidian_sword