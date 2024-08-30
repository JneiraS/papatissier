from src.Appareil import Appareil
from src.ingredients.ingredient import Ingredient
from src.recipients.recipient import Recipient


class ConcretRecipient(Recipient):

    def __init__(self, name: str, contient: Ingredient | Appareil | None = None):
        super().__init__(name, contient)

    def __str__(self):
        e = self.sum_of_quantite()
        return f"{self.name}, contenant: {', '.join(str(i) for i in e)}"
