import unittest

from increment_line_number import read_file


class TestIncrementLineNumber(unittest.TestCase):
    def test_read_file_works(self):
        expected = ['1. line', '2. second line', '3. third line']

        actual = read_file('test.txt')

        self.assertEqual(expected, actual)

    def it_works(self):
        pass
        # Mock to return some predefined content
        # Make assertion


if __name__ == '__main__':
    unittest.main()
