import unittest
from unittest.mock import MagicMock

from src.commis.verseurs import Verseurs
from src.ingredients.ingredient import Ingredient
from src.recipients.recipient import Recipient


class TestAddToRecipient(unittest.TestCase):
    def test_add_valid_ingredient(self):
        recipient = MagicMock(spec=Recipient)
        recipient.contient = MagicMock()
        ingredient = Ingredient("test", 10.0, "g")
        Verseurs.add_to_recipient(recipient, 10.0, ingredient)
        recipient.contient.add_ingredient.assert_called_once_with(ingredient)

    def test_add_ingredient_with_negative_quantity(self):
        recipient = MagicMock(spec=Recipient)
        recipient.contient = MagicMock()
        ingredient = Ingredient("test", -10.0, "g")
        with self.assertRaises(ValueError):
            Verseurs.add_to_recipient(recipient, -10.0, ingredient)

    def test_add_ingredient_with_zero_quantity(self):
        recipient = MagicMock(spec=Recipient)
        recipient.contient = MagicMock()
        ingredient = Ingredient("test", 0.0, "g")
        with self.assertRaises(ValueError):
            Verseurs.add_to_recipient(recipient, 0.0, ingredient)

    def test_add_ingredient_to_none_recipient(self):
        recipient = Recipient("test", Ingredient("test", 10.0, "g"))
        ingredient = Ingredient("test", 10.0, "g")
        with self.assertRaises(AttributeError):
            Verseurs.add_to_recipient(recipient, 10.0, ingredient)


if __name__ == '__main__':
    unittest.main()
