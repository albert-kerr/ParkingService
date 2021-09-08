from parkingservice.car import Car
from parkingservice.employee import Employee
from parkingservice.parking_service import ParkingService


class TestParkingService:
    def test_parking_service(self):
        employees = [Employee("A", 0.11), Employee("B", 0.15)]
        parking_service = ParkingService(len(employees))
        cars = [
            Car("A", "large", 0.07, 57),
            Car("B", "large", 0.59, 66),
            Car("C", "large", 0.49, 54),
        ]
        for employee in employees:
            parking_service.add_employee(employee)

        for car in cars:
            parking_service.park_car(car)
