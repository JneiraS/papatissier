from src.ingredients.ingredient import Ingredient


class Oeuf(Ingredient):

    def __init__(self, quantite: float, unite: str):
        """
        Initialisation d'un oeuf

        :param quantite: la quantit  de l'oeuf
        :type quantite: float
        :param unite: l'unit  de la quantit  de l'oeuf
        :type unite: str
        """

        super().__init__("oeuf", quantite, unite)

    @property
    def quantite(self) -> float:
        """
        Get the quantity of eggs

        :return: the quantity of eggs
        :rtype: float
        """
        return self._quantite
