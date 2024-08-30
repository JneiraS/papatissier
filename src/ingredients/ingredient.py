from abc import ABC

class Ingredient(ABC):

    def __init__(self, nom: str, quantite: float, unite: str):
        """
        Initialisation d'un ingredient.
        :param nom: Le nom de l'ingrédient.
        :param quantite: La quantité de l'ingrédient.
        :param unite: L'unité de mesure de l'ingrédient.
        """
        self.nom = nom
        self.quantite = quantite  # Cela déclenchera le setter, qui effectue les vérifications.
        self.unite = unite

    def __str__(self):
        return f"{self.quantite} {self.unite} de {self.nom}"

    @property
    def quantite(self):
        return self._quantite

    @quantite.setter
    def quantite(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("La quantité doit être un nombre")
        if value < 0:
            raise ValueError("La quantité doit être positive")
        self._quantite = value

    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, value):
        if not isinstance(value, str):
            raise TypeError("Le nom doit être une chaîne de caractères")
        self._nom = value

    @property
    def unite(self):
        return self._unite

    @unite.setter
    def unite(self, value):
        if not isinstance(value, str):
            raise TypeError("L'unité doit être une chaîne de caractères")
        self._unite = value
