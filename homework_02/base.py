from abc import ABC


class Vehicle(ABC):
    weight = None
    started = None
    fuel = None
    fuel_consumption = None


    def __init__(self,weight,fuel,fuel_consumption):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption


    def start(self):
        try:
            started == 1
        except exceptions.LowFuelError:
            print()


    def move(self):
        try:
            move >= fuel/fuel_consumption and fuel -= move*fuel_consumption
        except exceptions.NotEnoughFuel:

        return fuel -= move*fuel_consumption

