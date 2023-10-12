import unittest
from unittest import mock

from increment_line_number import read_file, increment_line_number


class TestIncrementLineNumber(unittest.TestCase):
    def test_read_file_works(self):
        expected = ['1. line', '2. second line', '3. third line']

        actual = read_file('test.txt')

        self.assertEqual(expected, actual)

    @mock.patch('increment_line_number.read_file')
    def test_increment_line_number_works(self, read_file_mock):
        content = [
            '1. Hello',
            '2. Hi',
            '3. Good morning'
        ]
        read_file_mock.return_value = content
        expected = 4

        actual = increment_line_number('some_file')

        self.assertEqual(expected, actual)

    @mock.patch('increment_line_number.read_file')
    def test_increment_line_number_works_with_two_items(self, read_file_mock):
        content = [
            '1. Hello',
            '2. Hi',
        ]
        read_file_mock.return_value = content
        expected = 3

        actual = increment_line_number('some_file')

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
