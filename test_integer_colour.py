import unittest

from integer_colour import integer_colour

"""
Task
Given an integer x perform the following conditional actions:

If x is odd, return 'Red'
If x is even and in the inclusive range of 2 to 5, return 'Blue'
If x is even and in the inclusive range of 6 to 20, return 'Red'
If x is even and greater than 20, return 'Blue'
"""


class TestIntegerColour(unittest.TestCase):
    def test_works_for_odd(self):
        expected = 'Red'

        actual = integer_colour(5)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
