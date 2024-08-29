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
        produits_dict = {}

        if isinstance(self.contient, Appareil):
            for element in self.contient.composition:
                if element.nom in produits_dict:
                    produits_dict[element.nom].quantite += element.quantite
                else:
                    produits_dict[element.nom] = Ingredient(element.nom, element.quantite, element.unite)
            return list(produits_dict.values())
        else:
            return self.contient.quantite
