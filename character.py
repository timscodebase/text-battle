from colors import *
from health_bar import HealthBar
from weapon import Weapon, fists, obsidian_sword, iron_sword, short_bow

def warrior_backstory(name) -> str:
    return f"{name} was born to a family of nomadic warriors, who roamed the land in search of adventure and glory. {name}'s parents were both skilled fighters, and they taught {name} everything they knew about combat and survival from a young age. {name} was a quick learner, and {name} soon became adept at wielding a sword and shield.\n\nAs {name} grew older, {name} began to feel a sense of restlessness, a desire to explore the world beyond {name}'s family's camp. {name} heard stories of a land far to the east, a place of ancient magic and forgotten ruins. {name} knew that {name} had to see it for herself, to test {name}'s skills and prove {name}'s worth as a warrior.\n\nSo {name} bid farewell to {name}'s family and set out on {name}'s own, traveling across mountains and through dark forests. {name} fought off fierce beasts and bandits, using {name}'s sword and {name}'s wits to overcome any obstacle. {name} met other adventurers on the road, some of whom became {name}'s allies, while others proved to be deadly enemies.\n\nEventually, {name} arrived at the foot of a great mountain range, where {name} discovered an ancient temple hidden in the clouds. {name} spent months studying the ancient texts and artifacts within, learning spells and incantations that allowed {name} to harness the power of the elements themselves.\n\nNow, {name} travels the land as a non-binary Warrior, using {name}\'s skills to protect the innocent and fight against injustice wherever it may be found. {name}'s sword arm is strong, {name}'s spells are at the ready, and {name}'s heart is filled with a sense of purpose. {name} is a warrior, a seeker of knowledge and a defender of the weak. Zara will not rest until the land is safe from tyranny and all people can live in peace."

def wizard_backstory(name) -> str:
    return f"{name} was born to a family of powerful wizards, who taught {name} everything they knew about magic from a young age. {name} was a quick learner, and soon became adept at casting spells and manipulating the elements.\n\nAs {name} grew older, they began to feel a sense of restlessness, a desire to explore the world beyond their family's tower. They heard stories of a land far to the east, a place of ancient magic and forgotten ruins. {name} knew they had to see it for themselves, to test their skills and prove their worth as a wizard.\n\nSo {name} bid farewell to their family and set out on their own, traveling across mountains and through dark forests. They encountered fierce beasts and bandits, but using their magic, they were able to overcome any obstacle. They met other adventurers on the road, some of whom became their allies, while others proved to be deadly enemies.\n\nEventually, {name} arrived at the foot of a great mountain range, where they discovered an ancient library hidden in the clouds. They spent months studying the ancient texts and artifacts within, learning new spells and techniques that allowed them to harness the power of the elements themselves.\n\nNow, {name} travels the land as a non-binary Wizard, using their magic to protect the innocent and fight against injustice wherever it may be found. Their spellbook is filled with powerful incantations, and their staff is imbued with the power of the elements. {name} is a seeker of knowledge and a defender of the weak. They will not rest until the land is safe from tyranny and all people can live in peace."

def cleric_backstory(name) -> str:
    return f"{name} was born to a family of powerful wizards, who taught {name} everything they knew about magic from a young age. {name} was a quick learner, and soon became adept at casting spells and manipulating the elements.\n\nAs {name} grew older, they began to feel a sense of restlessness, a desire to explore the world beyond their family's tower. They heard stories of a land far to the east, a place of ancient magic and forgotten ruins. {name} knew they had to see it for themselves, to test their skills and prove their worth as a wizard.\n\nSo {name} bid farewell to their family and set out on their own, traveling across mountains and through dark forests. They encountered fierce beasts and bandits, but using their magic, they were able to overcome any obstacle. They met other adventurers on the road, some of whom became their allies, while others proved to be deadly enemies.\n\nEventually, {name} arrived at the foot of a great mountain range, where they discovered an ancient library hidden in the clouds. They spent months studying the ancient texts and artifacts within, learning new spells and techniques that allowed them to harness the power of the elements themselves.\n\nNow, {name} travels the land as a non-binary Wizard, using their magic to protect the innocent and fight against injustice wherever it may be found. Their spellbook is filled with powerful incantations, and their staff is imbued with the power of the elements. {name} is a seeker of knowledge and a defender of the weak. They will not rest until the land is safe from tyranny and all people can live in peace."

def thief_backstory(name) -> str:
    return f"{name} was born to a family of powerful wizards, who taught {name} everything they knew about magic from a young age. {name} was a quick learner, and soon became adept at casting spells and manipulating the elements.\n\nAs {name} grew older, they began to feel a sense of restlessness, a desire to explore the world beyond their family's tower. They heard stories of a land far to the east, a place of ancient magic and forgotten ruins. {name} knew they had to see it for themselves, to test their skills and prove their worth as a wizard.\n\nSo {name} bid farewell to their family and set out on their own, traveling across mountains and through dark forests. They encountered fierce beasts and bandits, but using their magic, they were able to overcome any obstacle. They met other adventurers on the road, some of whom became their allies, while others proved to be deadly enemies.\n\nEventually, {name} arrived at the foot of a great mountain range, where they discovered an ancient library hidden in the clouds. They spent months studying the ancient texts and artifacts within, learning new spells and techniques that allowed them to harness the power of the elements themselves.\n\nNow, {name} travels the land as a non-binary Wizard, using their magic to protect the innocent and fight against injustice wherever it may be found. Their spellbook is filled with powerful incantations, and their staff is imbued with the power of the elements. {name} is a seeker of knowledge and a defender of the weak. They will not rest until the land is safe from tyranny and all people can live in peace."

class Character:
    def __init__(self, name: str, health: int, magic: int, weapon: Weapon = fists,) -> None:
        self.name = name
        self.health = health
        self.magic = magic
        self.health_max = health
        self.is_alive = True

        self.weapon = weapon

    def attack(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        if target.health == 0:
            print(f"{target.name} died!")
            target.is_alive = False

# ------------ Heros ------------
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
        print(self.color | f"\n\n{self.backstory}\n\nPress any key to continue...")
        input()

class Warrior(Hero):
    def __init__(self, name: str, health: int = 100, magic: int = 10, weapon: Weapon = obsidian_sword) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.weapon = fists
        self.backstory = warrior_backstory(self.name)
        self.color = grey
        self.health_bar = HealthBar(self, color="grey")

    def jab(self, target) -> None:
        if self.weapon.type != "sharp":
            print("You can't jab with a blunt weapon.  Look for something sharp!")
        else:
            target.health -= 8
            print(f"{self.name} jabbed at {target.name}!")

class Wizard(Hero):
    def __init__(self, name: str, health: int = 75, magic: int = 30, weapon: Weapon = fists) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.weapon = fists
        self.backstory = wizard_backstory(self.name)
        self.color = green
        self.health_bar = HealthBar(self, color="green")

    def fireball(self, target) -> None:
        self.magic -= 10
        target.health -= 10
        print(f"{self.name} threw a fireball at {target.name}!")

    def heal(self, target) -> None:
        if self.magic < 10:
            print(f"{self.name} doesn't have enough magic to heal!")
        else:
            self.magic -= 10
            target.health += 10
            print(f"{self.name} healed {target.name}!")

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

class Cleric(Hero):
    def __init__(self, name: str, health: int = 100, magic: int = 30, weapon: Weapon = fists) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.weapon = fists
        self.backstory = cleric_backstory(self.name)
        self.color = purple
        self.health_bar = HealthBar(self, color=str(self.color))

    def heal(self, target) -> None:
        if self.magic < 10:
            print(f"{self.name} doesn't have enough magic to heal!")
        else:
            self.magic -= 10
            target.health += 20
            print(f"{self.name} healed {target.name}!")


            print(f"{self.name} punched at {target.name}!")

# ------------ Enemies ------------
class Enemy(Character):
    def __init__(self,
                 name: str,
                 health: int = 50,
                 magic: int = 20,
                 weapon: Weapon = iron_sword
                 ) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.weapon = weapon

        self.health_bar = HealthBar(self, color="red")

class Zombie(Enemy):
    def __init__(self, name: str, health: int, magic: int, weapon: Weapon) -> None:
        super().__init__(name=name, health=health, magic=magic)
        self.health_bar = HealthBar(self, color="green2")

class Dragon(Enemy):
    def __init__(self, name: str, health: int, magic: int) -> None:
        super().__init__(name=name, health=health, magic=magic)
        self.health_bar = HealthBar(self, color="blue3")

class Boss(Enemy):
    def __init__(self, name: str, health: int, magic: int, weapon: Weapon) -> None:
        super().__init__(name=name, health=health, magic=magic, weapon=weapon)
        self.health_bar = HealthBar(self, color="yellow")
        self.weapon = obsidian_sword