
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Create a Calculator instance for testing."""
        comma_delimiter = ","
        semicolon_delimiter = ";"
        self.calc = Calculator(comma_delimiter)
        self.calc2 = Calculator(semicolon_delimiter)

    def test_add_empty_string(self):
        """Test addition."""
        self.assertEqual(self.calc.add(""), 0)

    def test_add_numbers_in_string(self):
        self.assertEqual(self.calc.add("1"), 1)
        self.assertEqual(self.calc.add("1,2"), 3)
        self.assertEqual(self.calc.add("1,2,3,4,5,6,7,8,9,0,1,2,3,4,5,6,7,8,9"), 90)

    def test_new_line_in_between_valid(self):
        self.assertEqual(self.calc.add("1\n2,3"), 6)
        # new line at the end is invalid
        self.assertEqual(self.calc.add("1,\n"), "invalid")

    def test_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            self.calc.add("1,2,3,-4,-5")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -4,-5")

        with self.assertRaises(ValueError) as context:
            self.calc2.add("1;2;3;-4;-5")
        self.assertEqual(str(context.exception), "Negative numbers not allowed: -4,-5")

    def test_different_delimiter(self):
        self.assertEqual(self.calc2.add("1;2"), 3)



