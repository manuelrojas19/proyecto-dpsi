from calculator import Calculator

class InyectionRelationCalculator(Calculator):
    def __init__(self) -> None:
        super().__init__()

    def calculate(tank_capacity: float, needed_liters) -> float:
        return tank_capacity / needed_liters
