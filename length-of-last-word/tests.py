import unittest

from length import length_of_last_word


class TestLengthOfLastWord(unittest.TestCase):

    def test_length_of_last_word(self):
        test_cases = [
            {
                'input': 'Hello World',
                'expected_length': 5,
            },
            {
                'input': '   fly me   to   the moon  ',
                'expected_length': 4,
            },
            {
                'input': 'uffy is still joyboy',
                'expected_length': 6,
            }
        ]

        for test_case in test_cases:
            prefix = length_of_last_word(test_case['input'])

            self.assertEqual(prefix, test_case['expected_length'])


if __name__ == '__main__':
    unittest.main()
