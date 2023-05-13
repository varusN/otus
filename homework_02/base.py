from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):

    def __init__(self,weight,fuel,fuel_consumption):
        self.weight = None
        self.fuel = None
        self.fuel_consumption = None
        self.started = None


    def start(self,started,fuel):
        if started != 1:
            try:
                fuel > 0
            else:
                started = 1
            except LowFuelError:
                pass


    def move(self,dist):
        fuel = self.fuel
        fuel_consumption = self.fuel_consumption
        try:
            dist <= fuel/fuel_consumption
        except NotEnoughFuel:
            print()
        fuel -= dist * fuel_consumption
        return fuel

