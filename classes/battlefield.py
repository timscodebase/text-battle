from classes import Battle
from classes.character import Character

class BattleField:
  def __init__(self, name: str, hero: Character, enemy: Character) -> None:
    self.name = name
    self.hero = hero
    self.enemy = enemy
    self.battle = Battle(hero, enemy)
    
  def fight(self) -> None:
    while self.hero.health > 0 and self.enemy.health > 0:
      self.battle.fight()

    