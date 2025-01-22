
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