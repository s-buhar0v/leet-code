import unittest

from find import find_disappeared_numbers


class TestFindDisappearedNumbers(unittest.TestCase):
    test_cases = [
        {
            'input': [1, 1, 3],
            'expected': [2],
        },
        {
            'input': [2, 2, 4, 4, 5, 6],
            'expected': [1, 3],
        },
    ]

    def test_find_disappeared_numbers(self):
        for test_case in self.test_cases:
            result = find_disappeared_numbers(test_case['input'])

            self.assertListEqual(result, test_case['expected'])


if __name__ == '__main__':
    unittest.main()
