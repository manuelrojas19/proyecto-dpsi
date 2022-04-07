from calculator import Calculator

class FertilizationUnderProduction(Calculator):
    def __init__(self) -> None:
        super().__init__()

    @staticmethod
    def calculate (plants_number: int, fertilizer_kg: int, plants_number_kg: float) -> float:
        return (plants_number * fertilizer_kg) / plants_number_kg