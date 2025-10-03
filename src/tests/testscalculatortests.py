import unittest
from calculator.core import Calculator


class CalculatorTests(unittest.TestCase):
    def test_class_instantiate_ok(self):
        calculator = Calculator()
        self.assertIsNotNone(calculator, "could not instantiate calculator")

    def test_add_works(self):
        # Arrange
        calculator = Calculator()
        operator1, operator2, expected = 3,7,10
        # Act
        result = calculator.Add(operator1, operator2)
        # Assert
        self.assertEqual(expected,result,"add method doesn't add properly")

    def test_substract_works(self):
        # Arrange
        calculator = Calculator()
        operator1, operator2, expected = 8,3,5
        # Act
        result = calculator.Substract(operator1, operator2)
        # Assert
        self.assertEqual(expected, result, "substract method doesn't work!")

    def test_multiply_works(self):
        # Arrange
        calculator = Calculator()
        operator1, operator2, expected = 5,5,25
        # Act
        result = calculator.Multiply(operator1, operator2)
        # Assert
        self.assertEqual(expected, result, "multiply method doesn't work!")

    def test_divide_works(self):
        # Arrange
        calculator = Calculator()
        operator1, operator2, expected = 40,8,5
        # Act
        result = calculator.Divide(operator1, operator2)
        # Assert
        self.assertEqual(expected, result, "divide method doesn't work!")        