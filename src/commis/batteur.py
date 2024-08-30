import threading
import time

from src.commis.commis import Commis
from src.ingredients.ingredient import Ingredient
from src.recipients.recipient import Recipient


class BatteurOeufs(Commis, threading.Thread):
    """
    Classe qui permet de battre des oeufs
    """
    def __init__(self, ingredient: Ingredient, recipient: Recipient):
        threading.Thread.__init__(self)
        self.nb_oeufs = ingredient
        self.recipient = recipient

    def run(self):
        nb_tours = self.nb_oeufs.quantite * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\tJe bats les {self.nb_oeufs.quantite} oeufs, tour n°{no_tour}")
            time.sleep(0.01)  # temps supposé d'un tour de batteur
        self.recipient.contient = self.nb_oeufs
