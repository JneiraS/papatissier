import threading
from abc import ABC, abstractmethod


class Commis(threading.Thread, ABC):

    @abstractmethod
    def run(self):
        """
        Lancer le commis
        :return:
        """
        ...
