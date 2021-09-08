class Employee:
    def __init__(self, name: str, commission: float):
        self.name = name
        self.commission = commission

    @staticmethod
    def parse_percentage_to_decimal(s: str) -> float:
        return float(s.strip("%")) * 0.01
