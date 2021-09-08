#!/usr/bin/python3

import argparse

from parkingservice.car import Car
from parkingservice.employee import Employee
from parkingservice.parking_service import ParkingService
from parkingservice.util import read_json_file


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input-file", type=str, required=True, help="JSON file containing car info"
    )

    return parser.parse_args()


def main():
    args = parse_args()
    car_info = read_json_file(args.input_file)
    employee_info = read_json_file("data/employees.json")
    parking_service = ParkingService(employee_size=len(employee_info))

    for employee in employee_info:
        commission = Employee.parse_percentage_to_decimal(employee.get("commission"))
        employee_obj = Employee(employee.get("name"), commission)
        parking_service.add_employee(employee_obj)

    for car in car_info:
        car_obj = Car(
            car.get("licencePlate"),
            car.get("size"),
            car.get("fuel").get("level"),
            car.get("fuel").get("capacity"),
        )
        parking_service.park_car(car_obj)


if __name__ == "__main__":
    main()
