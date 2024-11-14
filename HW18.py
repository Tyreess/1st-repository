class car:

    def __init__(self, year: int, country: str, mark: str, mileage: int, fuel_consumption: float):
        self.year = year
        self.country = country
        self.mark = mark
        self.mileage = mileage
        self.fuel_consumption = fuel_consumption
        self.cost_of_service = mileage * 7.6

car1 = car(2012, 'Japan', 'Toyota', 20000, 5.5)
car2 = car(2024, 'German', 'Audi', 0, 3.3)
car3 = car(2020, 'France', 'Sitroen', 80000, 1.8)


car2.mileage = 10000
print(car1.cost_of_service)
print("Я авто марки " + car2.mark + " їду по справам господаря")
