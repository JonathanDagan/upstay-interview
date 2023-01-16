from calculator import Calculator
import unittest


class TestMain(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(Calculator.calculate(self.calc, "1+1"), 2)
        self.assertEqual(Calculator.calculate(self.calc, "1+22"), 23)
        self.assertEqual(Calculator.calculate(self.calc, "1+-3"), -2)

    def test_subtract(self):
        self.assertEqual(Calculator.calculate(self.calc, "1-1"), 0)
        self.assertEqual(Calculator.calculate(self.calc, "1-22"), -21)
        self.assertEqual(Calculator.calculate(self.calc, "1--3"), 4)

    def test_multiply(self):
        self.assertEqual(Calculator.calculate(self.calc, "1*1"), 1)
        self.assertEqual(Calculator.calculate(self.calc, "1*22"), 22)
        self.assertEqual(Calculator.calculate(self.calc, "1*-3"), -3)

    def test_divide(self):
        self.assertEqual(Calculator.calculate(self.calc, "1/1"), 1)
        self.assertEqual(Calculator.calculate(self.calc, "1/2"), 0.5)
        self.assertEqual(Calculator.calculate(self.calc, "1/-2"), -0.5)

    def test_order(self):
        self.assertEqual(Calculator.calculate(self.calc, "1+1+1"), 3)
        # self.assertEqual(Calculator.calculate(self.calc, "1+1-1"), 1)
        self.assertEqual(Calculator.calculate(self.calc, "1+1*1"), 2)
        self.assertEqual(Calculator.calculate(self.calc, "1+1/1"), 2)
