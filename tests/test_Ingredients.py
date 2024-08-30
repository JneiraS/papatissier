import unittest

from src.ingredients.ingredient import Ingredient


class TestIngredientInit(unittest.TestCase):
    def test_valid_input(self):
        ingredient = Ingredient("nom", 1.0, "unite")
        self.assertEqual(ingredient.nom, "nom")
        self.assertEqual(ingredient.quantite, 1.0)
        self.assertEqual(ingredient.unite, "unite")

    def test_invalid_input(self):
        with self.assertRaises(TypeError):
            Ingredient(123, 1.0, "unite")  # non-string nom
        with self.assertRaises(TypeError):
            Ingredient("nom", 1.0, 123)  # non-string unite
        with self.assertRaises(TypeError):
            Ingredient("nom", "un", "unite")  # non-float quantite

    def test_edge_cases(self):
        ingredient = Ingredient("", 0.0, "")
        self.assertEqual(ingredient.nom, "")
        self.assertEqual(ingredient.quantite, 0.0)
        self.assertEqual(ingredient.unite, "")


if __name__ == "__main__":
    unittest.main()
