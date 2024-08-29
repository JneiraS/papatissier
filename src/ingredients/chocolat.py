from src.ingredients.ingredient import Ingredient


class Chocolat(Ingredient):

    def __init__(self, quantite: float, unite: str):
        super().__init__("chocolat", quantite, unite)
        self._quantite = quantite

    @property
    def quantite(self):
        return self._quantite
