import unittest

from src.commis.commis import Commis


class TestCommisRunMethod(unittest.TestCase):

    def test_run_method_is_abstract(self):
        with self.assertRaises(TypeError):
            Commis()


if __name__ == '__main__':
    unittest.main()
