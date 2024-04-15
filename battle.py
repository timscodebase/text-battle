import os
from character import Hero, Enemy

class Battle:
  def __init__(self, hero: Hero, enemy: Enemy) -> None:
    self.hero = hero
    self.enemy = enemy
    self.battle_completed = False
    self.winner = None

  def fight(self) -> None:
    while self.battle_completed == False:
      os.system("clear")
      print(f"{self.hero.name} vs. {self.enemy.name}")
      print(self.battle_completed == False)
      self.hero.health_bar.draw()
      self.enemy.health_bar.draw()
      input()

      if self.hero.health <= 0 or self.enemy.health <= 0:
        if self.hero.health <= 0:
          self.winner = self.enemy
        
        elif self.enemy.health <= 0:
          self.winner = self.hero
        
        self.battle_completed = True
        return self.winner
        
      self.hero.attack(self.enemy)
      self.enemy.attack(self.hero)