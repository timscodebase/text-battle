from classes.character import Character
from utils import thief_backstory

class Thief(Character):
    def __init__(self, name: str, health: int = 75, magic: int = 30) -> None:
        super().__init__(name=name, health=health, magic=magic)
        
        self.color = "purple"
        self.backstory = thief_backstory(self.name)

    def steal(self, target, item) -> None:
        if self.food_available < 1:
            print(f"{self.name} doesn't have any food to steal!")
        else:
            print(f"You stole {item.name}  from {target.name} !")
