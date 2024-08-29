from src.ingredients.ingredient import Ingredient
from src.recipients.recipient import Recipient


class ConcretRecipient(Recipient):

    def __init__(self, name: str, contient: Ingredient = None):
        super().__init__(name, contient)

    def __str__(self):
        return (f"{self.name} contenant: {self.contient.quantite} "
                f"{self.contient.unite} de {self.contient.nom}")
