import unittest
from flatten import flatten_list

class TestFlatten(unittest.TestCase):
    
    def test_flatten_simple_list(self):
        lista = [1, 2, 3, 4]
        resultado_esperado = [1, 2, 3, 4]
        self.assertEqual(flatten_list(lista), resultado_esperado)
    
    def test_flatten_nested_lists(self):
        lista = [1, [2, 3], [4, [5, 6]]]
        resultado_esperado = [1, 2, 3, 4, 5, 6]
        self.assertEqual(flatten_list(lista), resultado_esperado)
    
    def test_flatten_mixed_structures(self):
        lista = [1, (2, 3), {'a': 4, 'b': 5}, [6, [7, 8]]]
        resultado_esperado = [1, 2, 3, 'a', 4, 'b', 5, 6, 7, 8]
        self.assertEqual(flatten_list(lista), resultado_esperado)
    
    def test_flatten_empty_list(self):
        self.assertEqual(flatten_list([]), [])
    
    def test_flatten_deeply_nested_structures(self):
        lista = [1, [2, [3, [4, [5]]]]]
        resultado_esperado = [1, 2, 3, 4, 5]
        self.assertEqual(flatten_list(lista), resultado_esperado)

if __name__ == "__main__":
    unittest.main()