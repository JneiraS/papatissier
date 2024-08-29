import threading
from abc import ABC, abstractmethod

from src.recipients.recipient import Recipient


class Commis(threading.Thread, ABC):

    def __init__(self, quantite, recipient: Recipient):
        self.quantite = quantite
        self.recipient = recipient
        threading.Thread.__init__(self)

    @abstractmethod
    def run(self):
        """
        Lancer le commis
        :return:
        """
        ...
