import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Create a calculator instance before each test."""
        self.calc = SimpleCalculator()

    # ---- Addition Tests ----

    def test_addition(self):
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        self.assertEqual(self.calc.add(-2, -3), -5)

    def test_addition_mixed_sign_numbers(self):
        self.assertEqual(self.calc.add(-2, 3), 1)

    # ---- Subtraction Tests ----
    def test_subtract_positive_numbers(self):
        self.assertEqual(self.calc.subtract(10, 5), 5)

    def test_subtract_result_negative(self):
        self.assertEqual(self.calc.subtract(5, 10), -5)

    # ---- Multiplication Tests ----
    def test_multiply_positive_numbers(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiply_with_zero(self):
        self.assertEqual(self.calc.multiply(10, 0), 0)

    def test_multiply_negative_numbers(self):
        self.assertEqual(self.calc.multiply(-2, 3), -6)

    # ---- Division Tests ----
    def test_divide_positive_numbers(self):
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_numbers(self):
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_divide_fraction_result(self):
        self.assertEqual(self.calc.divide(3, 2), 1.5)

    def test_divide_by_zero_raises(self):
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(10, 0)

if __name__ == "__main__":
    unittest.main()