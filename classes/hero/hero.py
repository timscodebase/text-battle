from classes import Character, HealthBar, Weapon, fists
from utils import blue

class Hero(Character):
    def __init__(self,
                 name: str,
                 health: int = 75,
                 magic: int = 30,
                 weapon: Weapon = fists,
                 ) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)

        self.food_available = 0
        self.default_weapon = self.weapon
        self.color = blue
        self.health_bar = HealthBar(self, color="blue")
        self.backstory = None

    def equip(self, weapon) -> None:
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self) -> None:
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon

    def eat(self, food) -> None:
        self.health += food.value

    def grab_food(self, food) -> None:
        self.food_available += 1
        print(f"{self.name} grabbed a(n) {food.name}!")

    def punch(self, target) -> None:
        if self.weapon.type != "blunt":
            print("You can't punch with a sharp weapon.  Use your fists or look for something blunt!")
        else:
            target.health -= 5

    def tell_story(self) -> None:
        print(self.color | f"\n\n{self.backstory}\n\nPress any key to continue...".center(40, " "))
        input()
