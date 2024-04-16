from battle import Battle
from character import Hero, Enemy

class BattleField:
  def __init__(self, name: str, hero: Hero, enemy: Enemy) -> None:
    self.name = name
    self.hero = hero
    self.enemy = enemy
    self.battle = Battle(hero, enemy)
    
  def fight(self) -> None:
    while self.hero.health > 0 and self.enemy.health > 0:
      self.battle.fight()

    