# ------------ class setup ------------
class Weapon:
    def __init__(self, name, weapon_type, damage, value):
        self.name = name
        self.weapon_type = weapon_type
        self.damage = damage
        self.value = value

    def attack(self):
        print(f"{self.name} gir {self.damage} i skade")