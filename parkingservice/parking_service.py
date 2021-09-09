from concurrent.futures import ThreadPoolExecutor, Future
from queue import PriorityQueue, Queue

from parkingservice.employee import Employee
from parkingservice.car import Car


class ParkingService:
    def __init__(self, employee_size):
        self.executor = ThreadPoolExecutor(max_workers=employee_size)
        self.employee_queue = PriorityQueue()
        self.busy_employees = Queue()
        self.task_queue = Queue()

    def add_employee(self, employee: Employee):
        self.employee_queue.put((-1.0 * employee.commission, employee))

    def park_car(self, car: Car) -> Future:
        _, employee = self.employee_queue.get()
        while self.busy_employees.qsize():
            self.add_employee(self.busy_employees.get())
        future = self.executor.submit(car.refuel_car, employee)
        self.busy_employees.put(employee)
        return future
