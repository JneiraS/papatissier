import math
import threading
import time

from src.commis.commis import Commis
from src.recipients.recipient import Recipient


class FondeurChocolat(Commis, threading.Thread):
    def __init__(self, quantite, recipient: Recipient):
        threading.Thread.__init__(self)
        self.quantite = quantite
        self.recipient = recipient

    def run(self):
        print("Je mets de l'eau à chauffer dans une bouilloire")
        time.sleep(8)
        print("Je verse l'eau dans une casserole")
        time.sleep(2)
        print("J'y pose le bol rempli de chocolat")
        time.sleep(1)
        nb_tours = math.ceil(self.quantite / 10)
        for no_tour in range(1, nb_tours + 1):
            print(f"Je mélange {self.quantite} de chocolat à fondre, tour n°{no_tour}")
            time.sleep(1)  # temps supposé d'un tour de spatule