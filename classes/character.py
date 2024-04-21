from .weapon import Weapon, fists
from .health_bar import HealthBar
from utils import type_text, grey

class Character:
    def __init__(self, name: str, health: int = 75, magic: int = 30, weapon: Weapon = fists) -> None:
        self.name = name
        self.health = health
        self.health_max = health
        self.magic = magic
        self.weapon = weapon
        self.is_alive = True
        self.color = grey
        self.hb_color = "grey"
        self.health_bar = HealthBar(self, self.health_max, is_colored=True, color=self.hb_color)
        self.food_available = 0

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        if target.health == 0:
            print(f"{target.name} died!")
            target.is_alive = False

    def tell_story(self) -> None:
        type_text(self.color, f"\n\n{self.backstory}\n\nPress any key to continue...".center(40, " "))
        input()