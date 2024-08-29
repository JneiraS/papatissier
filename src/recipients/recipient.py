from abc import ABC

from src.Appareil import Appareil
from src.ingredients.ingredient import Ingredient


class Recipient(ABC):
    def __init__(self, name: str, contient: Ingredient | Appareil):
        self.name = name
        self.contient = contient

    def convert_ingredient_to_appareil(self):

        if isinstance(self.contient, Ingredient):
            ingredient = self.contient
            self.contient = Appareil()
            self.contient.add_ingredient(ingredient)

    def sum_of_quantite(self):
        total = 0
        if isinstance(self.contient, Appareil):
            for qty in self.contient.composition:
                total += qty.quantite
            return total
        else:
            return self.contient.quantite
