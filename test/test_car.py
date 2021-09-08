import pytest

from parkingservice.car import Car
from parkingservice.employee import Employee


class TestCar:
    employee = Employee("A", 0.22)

    @pytest.mark.parametrize(
        "car, employee, expected_profit",
        [
            (Car("A", "large", 0.07, 57), employee, 28.11),
            (Car("B", "large", 0.59, 66), employee, 7.7),
            (Car("C", "large", 0.49, 54), employee, 7.7),
        ],
    )
    def test_refuel_car(
        self, car: Car, employee: Employee, expected_profit: float
    ) -> None:
        assert round(car.refuel_car(employee), 2) == expected_profit
