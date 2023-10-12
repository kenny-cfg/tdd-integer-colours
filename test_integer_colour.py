import unittest

from integer_colour import integer_colour


class TestIntegerColour(unittest.TestCase):
    # If x is odd, return 'Red'
    def test_works_for_odd(self):
        expected = 'Red'

        actual = integer_colour(5)

        self.assertEqual(expected, actual)

    # If x is even and in the inclusive range of 2 to 5, return 'Blue'
    def test_works_for_even_between_2_and_5(self):
        expected = 'Blue'

        actual = integer_colour(2)

        self.assertEqual(expected, actual)

    # If x is even and in the inclusive range of 6 to 20, return 'Red'
    def test_works_for_even_between_6_and_20(self):
        expected = 'Red'

        actual = integer_colour(20)

        self.assertEqual(expected, actual)

    # If x is even and greater than 20, return 'Blue'
    def test_works_for_even_greater_than_20(self):
        expected = 'Blue'

        actual = integer_colour(599934)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
