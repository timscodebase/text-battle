from classes.weapon import Weapon, fists

class Character:
    def __init__(self, name: str, health: int, magic: int, weapon: Weapon = fists,) -> None:
        self.name = name
        self.health = health
        self.magic = magic
        self.health_max = health
        self.is_alive = True

        self.weapon = weapon

    def battle(self, target) -> None:
        target.health -= self.weapon.damage
        target.health = max(target.health, 0)
        target.health_bar.update()
        if target.health == 0:
            print(f"{target.name} died!")
            target.is_alive = False