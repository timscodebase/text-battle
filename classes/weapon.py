class Weapon:
  def __init__(self, name: str, type: str, damage: int, value: int) -> None:
    self.name = name
    self.type = type
    self.damage = damage
    self.value = value

iron_sword = Weapon(name="Iron sword", type="sharp", damage=10, value=10)
iron_axe = Weapon(name="Iron axe", type="sharp", damage=5, value=5)
obsidian_sword = Weapon(name="Obsidian sword", type="sharp", damage=15, value=20)
obsidian_axe = Weapon(name="Obsidian axe", type="sharp", damage=10, value=10)

short_bow = Weapon(name="Short bow", type="piercing", damage=5, value=5)
long_bow = Weapon(name="Long bow", type="piercing", damage=10, value=10)

fists = Weapon(name="Fists", type="blunt", damage=1, value=0)