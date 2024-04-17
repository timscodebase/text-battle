from .hero import Hero
from classes import HealthBar, Weapon, fists, short_bow
from utils import brown, thief_backstory

class Thief(Hero):
    def __init__(self, name: str, health: int = 100, magic: int = 15, weapon: Weapon = short_bow) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.weapon = fists
        self.backstory = thief_backstory(self.name)
        self.color = brown
        self.health_bar = HealthBar(self, color="brown")

    def steal(self, target, item) -> None:
        if self.food_available < 1:
            print(f"{self.name} doesn't have any food to steal!")
        else:
            print(f"You stole {item.name}  from {target.name} !")
