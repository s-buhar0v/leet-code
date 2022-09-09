import unittest

from square import is_perfect_square

class TestPerfectSquare(unittest.TestCase):
    test_cases = [
        {
            'input': 16,
            'is_perfect_square': True,
        },
        {
            'input': 144,
            'is_perfect_square': True,
        },
        {
            'input': 10,
            'is_perfect_square': False,
        },
                {
            'input': -1,
            'is_perfect_square': False,
        }

    ]

    def test_perfect_square(self):
        for test_case in self.test_cases:
            result = is_perfect_square(test_case['input'])

            self.assertEqual(result, test_case['is_perfect_square'])

if __name__ == '__main__':
    unittest.main()