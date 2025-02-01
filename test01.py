# Programa en python
def promedio(a, b):
    return (a + b) / 2

# Import
import unittest
class TestCalculator2(unittest.TestCase):

    def test_sub(self):
        '''Test case function for subtraction'''
        self.calc = Calculator()
        result = self.calc.sub(10, 5)
        expected = 5
        self.assertEqual(result, expected)

    def test_mul(self):
        '''Test case function for multiplication'''
        self.calc = Calculator()
        result = self.calc.mul(3, 7)
        expected = 21
        self.assertEqual(result, expected)
        print("Hola")
