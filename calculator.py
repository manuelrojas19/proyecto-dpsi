from abc import ABC, abstractmethod
from numbers import Number


class Calculator(ABC):

    @abstractmethod
    def calculate(self) -> float:
        raise NotImplementedError


class FertilizationAdjustmentCalculator(Calculator):
    def __init__(self) -> None:
        super().__init__()

    def calculate(ppm: float, pure_element: float) -> float:
        return ppm / pure_element

class InyectionRelationCalculator(Calculator):
    def __init__(self) -> None:
        super().__init__()

    def calculate(tank_capacity: float, needed_liters) -> float:
        return tank_capacity / needed_liters
