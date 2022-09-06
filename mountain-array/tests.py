import unittest

from first import peak_index as first_solution
from second import peak_index as second_solution


class TestPeakIndex(unittest.TestCase):
    test_cases = [
        {
            'input': [0, 1, 0],
            'expected': 1
        },
        {
            'input': [0, 2, 3, 2, 1],
            'expected': 2
        },
    ]

    def test_peak_index__first_solution(self):
        for test_case in self.test_cases:
            nums = test_case['input'].copy()

            index = first_solution(nums)

            self.assertEqual(index, test_case['expected'])

    def test_peak_index__second_solution(self):
        for test_case in self.test_cases:
            nums = test_case['input'].copy()

            index = second_solution(nums)

            self.assertEqual(index, test_case['expected'])


if __name__ == '__main__':
    unittest.main()
