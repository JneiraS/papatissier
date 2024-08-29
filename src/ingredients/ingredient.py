from abc import ABC, abstractmethod


class Ingredient(ABC):
    @abstractmethod
    def __init__(self, nom: str ,quantite: float, unite: str):
        self.nom = nom
        self._quantite = quantite
        self.unite = unite

    @property
    def quantite(self):
        return self._quantite


