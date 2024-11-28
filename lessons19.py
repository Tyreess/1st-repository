from enum import Enum

class Vehicle(Enum):
    Brand = 'Toyota'
    Model = 'Supra'

class Car(Vehicle):
    def __init__(self, num_doors: int):
        super().__init__(num_doors, Vehicle.Brand, Vehicle.Model)


class Bike(Vehicle):
    def __init__(self, type: str):
        super().__init__(type, Vehicle.Brand, Vehicle.Model)


class Truck(Vehicle):
    def __init__(self, capacity: int):
        super().__init__(capacity, Vehicle.Brand, Vehicle.Model)


Vehicle1 = Car(4)
Vehicle2 = Bike('Mountation')
Vehicle3 = Truck(2000)
