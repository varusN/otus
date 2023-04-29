from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel

class Vehicle(ABC):
    weight = None
    started = None
    fuel = None
    fuel_consumption = None


    def __init__(self,weight,fuel,fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self,started):
        try:
            started == 1
        except LowFuelError:
            print()

    def move(self,dist):
        fuel = self.fuel
        fuel_consumption = self.fuel_consumption
        try:
            dist <= fuel/fuel_consumption
        except NotEnoughFuel:
            print()
        fuel -= dist * fuel_consumption
        return fuel

