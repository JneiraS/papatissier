from src.ingredients.ingredient import Ingredient


class Appareil:

    def __init__(self):
        self.composition: list[Ingredient] = []

    def add_ingredient(self, ingredient: Ingredient):
        """
        Ajoute une quantité d'ingreédient à l'appareil
        """
        self.composition.append(ingredient)

    def __str__(self):
        return "\n".join([str(ingredient) for ingredient in self.composition])
