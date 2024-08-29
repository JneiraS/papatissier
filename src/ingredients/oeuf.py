from src.ingredients.ingredient import Ingredient


class Oeuf(Ingredient):

    def __init__(self, quantite: float, unite: str):
        super().__init__("oeuf", quantite, unite)

    @property
    def quantite(self):
        return self._quantite
