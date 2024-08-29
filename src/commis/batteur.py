import threading
import time

from src.commis.commis import Commis
from src.recipients.recipient import Recipient


class BatteurOeufs(Commis, threading.Thread):
    def __init__(self, nb_oeufs: int, recipient: Recipient):
        threading.Thread.__init__(self)
        self.nb_oeufs = nb_oeufs
        self.recipient = recipient

    def run(self):
        nb_tours = self.nb_oeufs * 8
        for no_tour in range(1, nb_tours + 1):
            print(f"\tJe bats les {self.nb_oeufs} oeufs, tour n°{no_tour}")
            time.sleep(0.5)  # temps supposé d'un tour de batteur
