from parkingservice.constant import GAS_FEE, CAR_FEE
from parkingservice.employee import Employee


class Car:
    def __init__(
        self, licence_plate: str, size: str, fuel_level: str, fuel_capacity: str
    ):
        self.licence_plate = licence_plate
        self.size = size
        self.fuel_level = fuel_level
        self.fuel_capacity = fuel_capacity
        self.fuel_added = 0
        self.total_cost = 0
        self.employee = None

    def refuel_car(self, employee: Employee) -> float:
        if self.fuel_level < 0.1:
            self.fuel_added = 1 - self.fuel_level
            self.total_cost = self.fuel_added * self.fuel_capacity * GAS_FEE
        self.total_cost += CAR_FEE[self.size]
        self.employee = employee
        print(self)
        return self.total_cost * employee.commission

    def __str__(self):
        return f"""{{
    "licensePlate": {self.licence_plate},
    "employee": {self.employee.name if self.employee else None},
    "fuelAdded": {round(self.fuel_added, 2)}L,
    "price": ${round(self.total_cost, 2)}
}}"""
