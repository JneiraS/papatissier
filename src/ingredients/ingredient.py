from abc import ABC


class Ingredient(ABC):

    def __init__(self, nom: str, quantite: float, unite: str):
        """

        :param nom:
        :param quantite:
        :param unite:
        """
        self.nom = nom
        self._quantite = quantite
        self.unite = unite

    @property
    def quantite(self):
        return self._quantite

    def __str__(self):
        return f"{self.quantite} {self.unite} de {self.nom}"

    @quantite.setter
    def quantite(self, value):
        self._quantite = value
