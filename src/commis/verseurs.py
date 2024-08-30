import math
import threading

from src.commis.commis import Commis
from src.ingredients.ingredient import Ingredient
from src.recipients.recipient import Recipient


class Verseurs(Commis, threading.Thread):
    """
    Classe qui permet de verser des quantités d'ingreédients dans un recipient
    """

    def __init__(self, recipient_a_verser: Recipient, target_recipient: Recipient | None = None):
        """
        Initialisation d'un commis verseur
        :param recipient_a_verser: recipient d'origine
        :param target_recipient: recopient vers lequel on doit verser les ingreédients
        """
        threading.Thread.__init__(self)
        self.recipient_a_verser = recipient_a_verser
        self.target_recipient = target_recipient

    def run(self):

        self.target_recipient.convert_ingredient_to_appareil()

        number_of_laps: int = math.ceil(self.recipient_a_verser.contient.quantite / 10)
        quantity_to_be_paid_per_round: int = self.recipient_a_verser.contient.quantite / number_of_laps

        for no_tour in range(1, number_of_laps + 1):
            chocolat = self.recipient_a_verser.remove_ingredient(
                Ingredient("chocolat", quantity_to_be_paid_per_round, "g"))
            self.add_to_recipient(self.target_recipient, quantity_to_be_paid_per_round, chocolat)

            print(
                f"Je verse environ {quantity_to_be_paid_per_round:.0f} {self.recipient_a_verser.contient.unite} "
                f"de chocolat fondu, "
                f"tout en melangeant, "
                f"tour n°{no_tour}")

    @staticmethod
    def add_to_recipient(recipient: Recipient, quantite: float, ingredient: Ingredient):
        """
        Ajoute une quantité d'ingreédient au recipient
        """
        if quantite <= 0:
            raise ValueError("La quantité doit être supérieure à 0.")

        recipient.contient.add_ingredient(ingredient)
