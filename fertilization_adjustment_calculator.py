from calculator import Calculator

class FertilizationAdjustmentCalculator(Calculator):
    def __init__(self) -> None:
        super().__init__()

    def calculate(ppm: float, pure_element: float) -> float:
        return ppm / pure_element