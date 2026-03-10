import unittest
from src.calculator import add

class TestCalculator(unittest.TestCase):

    def test_add(self):
        # Test the add function
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1,1), 0)

if __name__ == '__main__':
    unittest.main()