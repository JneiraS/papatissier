from abc import ABC

from src.Appareil import Appareil
from src.ingredients.ingredient import Ingredient


class Recipient(ABC):
    def __init__(self, name: str, contient: Ingredient | Appareil):
        """
        initialisation d'un recipient
        :param name:
        :param contient:
        """
        self.name = name
        self.contient = contient

    def convert_ingredient_to_appareil(self):
        """
        Convertit un ingredient en appareil
        :return:
        """
        if not isinstance(self.contient, Appareil):
            ingredient = self.contient
            self.contient = Appareil()
            self.contient.add_ingredient(ingredient)

    def sum_of_quantite(self) -> list[Ingredient]:
        """
        Calcule la somme des quantités d'ingrédients dans la composition d'un appareil ou renvoie
        l'ingrédient lui-même.
        Cette méthode traite deux cas :

        1. S'il s'agit d'un appareil :
           - Elle agrège les ingrédients en additionnant leurs quantités.
           - Les ingrédients dupliqués sont fusionnés en un seul élément avec la quantité totale.

        2. Si c'est un ingreédient :
           - Elle renvoie simplement l'ingrédient.

        :return: Une liste d'objets Ingredient représentant les ingrédients agrégés ou l'ingrédient unique.
        """
        produits_dict = {}

        if isinstance(self.contient, Appareil):
            for element in self.contient.composition:
                nom = element.nom
                if nom in produits_dict:
                    produits_dict[nom].quantite += element.quantite
                else:
                    produits_dict[nom] = Ingredient(nom, element.quantite, element.unite)
            return list(produits_dict.values())
        else:
            return [self.contient]

    def remove_ingredient(self, ingredient: Ingredient):
        """
        Enleve une quantité d'ingreédient
        :param ingredient:
        :return:
        """
        if isinstance(self.contient, Ingredient):
            self.contient.quantite -= ingredient.quantite
            return ingredient
