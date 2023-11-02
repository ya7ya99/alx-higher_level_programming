#!/usr/bin/python3
""" modle unittest to test max_integer function """
import unittest
max_integer = __import__('6-max_integer').max_integer

""" Class test MaxInteger """


class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        """ test Empty list should return None """
        self.assertIsNone(max_integer([]), "Empty list should return None")

    def test_single_element_list(self):
        """ test Single-element list should return the element itself """
        self.assertEqual(max_integer([5]), 5, "Single-element list")

    def test_positive_numbers(self):
        """test Max of positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5, "positive numbers")

    def test_negative_numbers(self):
        """test Max of negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4, -5]), -1, "negative num")

    def test_mixed_numbers(self):
        """test Max of mixed numbers (negative and positive)"""
        self.assertEqual(max_integer([-1, 0, 5, 2, -10]), 5, "mixed numbers")

    def test_duplicate_max(self):
        """Test a list of equal integers."""
        self.assertEqual(max_integer([3, 3, 3, 3]), 3, "Duplicate max value")

    def test_ints_and_floats(self):
        """Test a list of integerss and floats."""
        self.assertEqual(max_integer([1.53, 15.5, -9, 15]), 15.5, "Float int")

    def test_string(self):
        """Test a string."""
        self.assertEqual(max_integer("Brennan"), 'r')

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_list_of_strings(self):
        """Test a list of strings."""
        self.assertEqual(max_integer(["My", "name", "is", "Aboubakr"]), "name")


if __name__ == '__main__':
    unittest.main()
