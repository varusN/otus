"""
создайте класс `Plane`, наследник `Vehicle`
"""
from homework_02.exceptions import CargoOverload
from homework_02.base import Vehicle

class Plane(Vehicle):

    def __init__(self,max_cargo,cargo):
        super().__init__(max_cargo)
        self.cargo = cargo


    def load_cargo(self):
        cargo = self.cargo
        max_cargo = self.cargo
        cargo += self.cargo
        try:
            cargo <= max_cargo
        except CargoOverload:
            pass

    def remove_all_cargo(self):
        old_cargo = self.cargo
        self.cargo = None
        return old_cargo
