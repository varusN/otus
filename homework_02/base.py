from abc import ABC
from homework_02.exceptions import LowFuelError, NotEnoughFuel


class Vehicle(ABC):
    def __init__(self, weight, fuel, fuel_consumption, started):
        self.weight = weight
        self.fuel = fuel
        self.fuel_consumption = fuel_consumption
        self.started = started

    def start(self, started, fuel):
        if started != 1:
            try:
                fuel > 0
            except LowFuelError:
                pass
            else:
                self.started = 1

    def move(self, dist):
        fuel = self.fuel
        fuel_consumption = self.fuel_consumption
        try:
            dist <= fuel / fuel_consumption
        except NotEnoughFuel:
            print()
        fuel -= dist * fuel_consumption
        return fuel
