from abc import ABC


class Recipient(ABC):
    def __init__(self, name: str):
        self.name = name
