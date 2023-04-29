"""
создайте класс `Plane`, наследник `Vehicle`
"""

class Plane(Vehicle):
    cargo = null
    max_cargo = null


    def __init__(self,max_cargo):
        self.max_cargo = max_cargo


    def load_cargo(self):
        cargo += self.cargo
        try:
            cargo <= max_cargo
        else exceptions.CargoOverload:
            print()

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = null
        return old_cargo
