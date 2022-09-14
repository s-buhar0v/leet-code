import unittest

from sequence import longest_sequence


class TestLongetSequence(unittest.TestCase):
    test_cases = [
        {
            'input': [1, 2, 3],
            'expected': 3,
        },
        {
            'input': [1, 2, 5, 3],
            'expected': 3,
        }
    ]

    def test_longest_sequence(self):
        for test_case in self.test_cases:
            length = longest_sequence(test_case['input'])

            self.assertEqual(length, test_case['expected'])


if __name__ == '__main__':
    unittest.main()