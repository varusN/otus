"""
создайте класс `Car`, наследник `Vehicle`
"""
from homework_02.base import Vehicle


class Car(Vehicle):
    def __init__(self, engine):
        self.engine = engine

    def set_engine(self, Engine):
        self.Car = Engine
