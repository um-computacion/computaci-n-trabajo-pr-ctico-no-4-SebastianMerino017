import unittest
from factorial import factorial_iterative, factorial_recursive

class TestFactorial(unittest.TestCase):
    
    def test_factorial_iterative_positive_numbers(self):
        self.assertEqual(factorial_iterative(0), 1)
        self.assertEqual(factorial_iterative(1), 1)
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_iterative(10), 3628800)

    def test_factorial_iterative_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorial_iterative(-1)
        with self.assertRaises(ValueError):
            factorial_iterative(-5)

    def test_factorial_recursive_positive_numbers(self):
        self.assertEqual(factorial_recursive(0), 1)
        self.assertEqual(factorial_recursive(1), 1)
        self.assertEqual(factorial_recursive(5), 120)
        self.assertEqual(factorial_recursive(10), 3628800)

    def test_factorial_recursive_negative_numbers(self):
        with self.assertRaises(ValueError):
            factorial_recursive(-1)
        with self.assertRaises(ValueError):
            factorial_recursive(-5)

if __name__ == "__main__":
    unittest.main()