import unittest

from first import move as first_solution
from second import move as second_solution


class TestMoveZeros(unittest.TestCase):
    test_cases = [
        {
            'input': [1, 2, 0, 4, 0],
            'expected': [1, 2, 4, 0, 0]
        },
        {
            'input': [0, 0, 1, 2],
            'expected': [1, 2, 0, 0]
        },
    ]

    def test_move_zeros__first_solution(self):
        for test_case in self.test_cases:
            nums = test_case['input'].copy()

            first_solution(nums)

            self.assertListEqual(nums, test_case['expected'])

    def test_move_zeros__second_solution(self):
        for test_case in self.test_cases:
            nums = test_case['input'].copy()

            second_solution(nums)

            self.assertListEqual(nums, test_case['expected'])


if __name__ == '__main__':
    unittest.main()
