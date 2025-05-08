import unittest
from factorial import factorial_iterative, factorial_recursive

class TestFactorial(unittest.TestCase):
    
    def test_factorial_iterative_positive_numbers(self):
        self.assertEqual(factorial_iterative(0), 1)
        self.assertEqual(factorial_iterative(1), 1)
        self.assertEqual(factorial_iterative(5), 120)
        self.assertEqual(factorial_iterative(10), 3628800)