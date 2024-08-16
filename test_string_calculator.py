import unittest
from string_calculator import StringCalculator
import random


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

    def test_add_any_amount_of_number(self):
        """
        Test cases for large and multiple numbers
        """

        result = self.calculator.add("10,20,30,40,50,60")
        self.assertEqual(10 + 20 + 30 + 40 + 50 + 60, result)

        result = self.calculator.add("111111,222222,333333,444444,555555")
        self.assertEqual(111111 + 222222 + 333333 + 444444 + 555555, result)

        data_list = [random.randrange(10000000000, 1000000000000) for _ in range(100)]
        input_data = ", ".join([str(i) for i in data_list])
        result = self.calculator.add(input_data)
        self.assertEqual(sum(data_list), result)


if __name__ == "__main__":
    unittest.main()
