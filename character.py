# ------------ parent class setup ------------
class Character:
    def __init__(self, name, health, weapon):
        self.name = name
        self.health = health
        self.weapon = weapon

    def attack(self, target):
        target.health -= self.weapon.damage
        #target.health = max(target.health, 0)
        print(f"{self.name} dealt {self.weapon.damage} damage to "
              f"{target.name} with {self.weapon.name}.")
    
    def equip(self, weapon):
        self.weapon = weapon
        print(f"{self.name} equipped a(n) {self.weapon.name}!")

    def drop(self):
        print(f"{self.name} dropped the {self.weapon.name}!")
        self.weapon = self.default_weapon
