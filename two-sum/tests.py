import unittest

from twosum import two_sum


class TestTwoSum(unittest.TestCase):

    def test_two_sum(self):
        test_cases = [
            {
                'nums': [2, 7, 11, 15],
                'target': 9,
                'expected_indexes': [0, 1],
            },
            {
                'nums': [3, 2, 4],
                'target': 6,
                'expected_indexes': [1, 2],
            },
            {
                'nums': [3, 3],
                'target': 6,
                'expected_indexes': [0, 1],
            },
        ]

        for test_case in test_cases:
            print(test_case)
            indexes = two_sum(test_case['nums'], test_case['target'])

            self.assertListEqual(indexes, test_case['expected_indexes'])


if __name__ == '__main__':
    unittest.main()
