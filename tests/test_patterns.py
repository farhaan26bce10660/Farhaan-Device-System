import unittest
from pattern_game import pattern_game


class TestPatternModule(unittest.TestCase):
    def test_module_imports(self):
        self.assertTrue(callable(pattern_game))


if __name__ == "__main__":
    unittest.main()
