import unittest

from prefix import longest_common_prefix


class TestLongestPrefix(unittest.TestCase):

    def test_longest_common_prefix(self):
        test_cases = [
            {
                'input': ['flower', 'flow', 'flight'],
                'expected_prefix': 'fl',
            },
            {
                'input': ['dog', 'racecar', 'car'],
                'expected_prefix': '',
            }
        ]

        for test_case in test_cases:
            prefix = longest_common_prefix(test_case['input'])

            self.assertEqual(prefix, test_case['expected_prefix'])


if __name__ == '__main__':
    unittest.main()
