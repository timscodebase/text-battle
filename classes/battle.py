import os
from classes.character import Character
from classes.enemies import Enemy
from time import sleep

class Battle:
  def __init__(self, hero: Character, enemy: Enemy) -> None:
    self.hero = hero
    self.enemy = enemy
    self.battle_completed = False
    self.winner = None

  def fight(self) -> None:
    while not self.battle_completed:
      os.system("clear")
      print(f"{self.hero.name} vs. {self.enemy.name}")
      self.hero.health_bar.draw()
      self.enemy.health_bar.draw()

      if self.is_battle_over():
        self.determine_winner()
        break

      self.hero.attack(self.enemy)
      self.enemy.attack(self.hero)
      sleep(0.5)

  def is_battle_over(self) -> bool:
    return self.hero.health <= 0 or self.enemy.health <= 0

  def determine_winner(self) -> None:
    if self.hero.health <= 0:
      self.winner = self.enemy
    else:
      self.winner = self.hero
    self.battle_completed = True
