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


    def start(self,started):
        try:
            started == 1
        except exceptions.LowFuelError:
            print()

    def move(self,dist):
        try:
            dist <= fuel/fuel_consumption
        except exceptions.NotEnoughFuel:
            print()
        fuel -= dist * fuel_consumption
        return fuel

