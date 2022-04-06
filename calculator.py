from abc import ABC, abstractmethod
from numbers import Number


class Calculator(ABC):
    
    @abstractmethod
    def calculate(self) -> float:
        raise NotImplementedError
    

class FertilizationCalculator(Calculator):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def calculate(nutrient_quantity: float, required_nutrient_quantity: float, nutrient_efficiency: float) -> float:
        return (nutrient_quantity * required_nutrient_quantity) / nutrient_efficiency






