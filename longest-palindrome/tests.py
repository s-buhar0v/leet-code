import unittest

from palindrome import longest_palindrome

class TestLongestPalindrome(unittest.TestCase):
    test_cases = [
        {
            'input': 'aaa',
            'expected': 3
        },
        {
            'input': 'abccccdd',
            'expected': 7 # dccaccd
        }
    ]

    def test_longest_palindrome(self):
        for test_case in self.test_cases:
            result = longest_palindrome(test_case['input'])

            self.assertEqual(result, test_case['expected'])


if __name__ == '__main__':
    unittest.main()