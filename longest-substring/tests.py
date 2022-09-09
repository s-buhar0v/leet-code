import unittest

from substring import length_of_longest_substring


class TestLengthOfLongestSubstring(unittest.TestCase):
    test_cases = [
        {
            'input': 'abcabcc',
            'expected': 3,
        },
        {
            'input': 'bbbb',
            'expected': 1,
        }
    ]

    def test_length_of_longest_substring(self):
        for test_case in self.test_cases:
            length = length_of_longest_substring(test_case['input'])

            self.assertEqual(length, test_case['expected'])


if __name__ == '__main__':
    unittest.main()
