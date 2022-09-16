from unittest import TestCase
import unittest

from match import string_matching

class TestStringMatching(unittest.TestCase):
    test_cases = [
        {
            'input': ['mass', 'as', 'hero', 'superhero'],
            'expected': ['as', 'hero',]
        }
    ]

    def test_string_matching(self):
        for test_case in self.test_cases:
            result = string_matching(test_case['input'])

            self.assertListEqual(result, test_case['expected'])


if __name__ == '__main__':
    unittest.main()