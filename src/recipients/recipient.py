from abc import ABC

from src.ingredients.ingredient import Ingredient


class Recipient(ABC):
    def __init__(self, name: str, contient: Ingredient):
        self.name = name
        self.contient = contient

    def __str__(self):
        return f"{self.name} {self.contient}"
