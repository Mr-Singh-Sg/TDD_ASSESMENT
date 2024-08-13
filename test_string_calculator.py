import unittest
from string_calculator import StringCalculator


class TestStringCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = StringCalculator()

    def test_add_number(self):
        """
        Test cases for an empty string, single number,
        two numbers and more then two numbers
        """

        result = self.calculator.add("")  # passing empty string
        self.assertEqual(0, result)

        result = self.calculator.add("1")  # passing single number
        self.assertEqual(1, result)

        result = self.calculator.add("1,2")  # passing two numbers
        self.assertEqual(1 + 2, result)

        result = self.calculator.add("1,2,3")  # passing three numbers
        self.assertEqual(1 + 2 + 3, result)


if __name__ == "__main__":
    unittest.main()
