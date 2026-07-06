import unittest

from calculator.calculator import add, divide, multiply, normalize_choice, parse_number, subtract


class CalculatorTests(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(add(5, 3), 8)

    def test_subtraction(self):
        self.assertEqual(subtract(10, 4), 6)

    def test_multiplication(self):
        self.assertEqual(multiply(6, 7), 42)

    def test_division(self):
        self.assertEqual(divide(9, 2), 4.5)

    def test_divide_by_zero(self):
        self.assertEqual(divide(10, 0), None)

    def test_parse_number_accepts_spaces(self):
        self.assertEqual(parse_number("  12.5  "), 12.5)

    def test_parse_number_rejects_invalid_input(self):
        with self.assertRaises(ValueError):
            parse_number("abc")

        with self.assertRaises(ValueError):
            parse_number("")

    def test_normalize_choice_supports_direct_operators(self):
        self.assertEqual(normalize_choice("x"), "*")
        self.assertEqual(normalize_choice("÷"), "/")
        self.assertEqual(normalize_choice("1"), "+")


if __name__ == "__main__":
    unittest.main()
