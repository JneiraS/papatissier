import math
import threading
import time

from src.commis.commis import Commis
from src.ingredients.ingredient import Ingredient
from src.recipients.recipient import Recipient


class Verseurs(Commis, threading.Thread):
    """
    Classe qui permet de verser des quantités d'ingreédients dans un recipient
    """
    def __init__(self, recipient_a_verser: Recipient, recipient_final: Recipient | None = None):
        threading.Thread.__init__(self)
        self.recipient_a_verser = recipient_a_verser
        self.recipient_final = recipient_final

    def run(self):
        self.recipient_final.convert_ingredient_to_appareil()
        nb_tours = math.ceil(self.recipient_a_verser.contient.quantite / 10)
        qt_verser = self.recipient_a_verser.contient.quantite / nb_tours
        for no_tour in range(1, nb_tours + 1):
            self.add_to_recipient(self.recipient_final, qt_verser)

            print(
                f"Je verse environ {qt_verser:.0f} {self.recipient_a_verser.contient.unite} "
                f"de chocolat fondu, "
                f"tout en melangeant, "
                f"tour n°{no_tour}")
            time.sleep(.01)

    @staticmethod
    def add_to_recipient(recipient: Recipient, quantite: float):
        """
        Ajoute une quantité d'ingreédient au recipient
        :param recipient:
        :param quantite:
        :return:
        """
        recipient.contient.add_ingredient(Ingredient("chocolat", quantite, "g"))
