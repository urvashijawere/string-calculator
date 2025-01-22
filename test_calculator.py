
import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):
    def setUp(self):
        """Create a Calculator instance for testing."""
        self.calc = Calculator()

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


