import unittest
from calculator import evaluate_expression


class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(evaluate_expression([1, 4], ["+"]), 5)

    def test_precedence(self):
        self.assertEqual(evaluate_expression([1, 4, 5, -1, 2], ["+", "-", "*", "/"]), 7.5)

    def test_division(self):
        self.assertEqual(evaluate_expression([10, 2], ["/"]), 5)

    def test_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            evaluate_expression([10, 0], ["/"])


if __name__ == "__main__":
    unittest.main()
