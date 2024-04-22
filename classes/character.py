from time import sleep
from utils import type_text, grey
from classes.health_bar import HealthBar
from classes.weapon import fists, Weapon
from utils.tally_food import tally_food

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
        # variable for keeping track of food types and amount
        self.food_available = {"apple": 0, "bread": 0, "golden_apple": 0, "steak": 0}
        self.food_count = tally_food(self)

    def __repr__(self):
        return f"{self.name}:  Health: {self.health} | Magic: {self.magic} | Food: {self.food_count} | Weapon: {self.weapon.name}"

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        if target.health == 0:
            print(f"{target.name} died!")
            target.is_alive = False

    def tell_story(self) -> None:
        type_text(self.color, self.backstory)
        sleep(1)
        print("\n\nPress any key to continue...")
        input()