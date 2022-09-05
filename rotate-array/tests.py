import unittest

from first import rotate as first_solution
from second import rotate as second_solution
from third import rotate as third_solution


class TestRotateArray(unittest.TestCase):
    test_cases = [
        {
            'input': [1, 2, 3, 4, 5, 6, 7],
            'expected': [5, 6, 7, 1, 2, 3, 4],
            'k': 3,
        },
    ]

    def test_rotate_array__first_solution(self):
        for test_case in self.test_cases:
            nums = test_case['input'].copy()

            first_solution(nums, test_case['k'])

            self.assertListEqual(nums, test_case['expected'])

    def test_rotate_array__second_solution(self):
        for test_case in self.test_cases:
            nums = test_case['input'].copy()

            second_solution(nums, test_case['k'])

            self.assertListEqual(nums, test_case['expected'])

    def test_rotate_array__third_solution(self):
        for test_case in self.test_cases:
            nums = test_case['input'].copy()

            third_solution(nums, test_case['k'])

            self.assertListEqual(nums, test_case['expected'])


if __name__ == '__main__':
    unittest.main()
