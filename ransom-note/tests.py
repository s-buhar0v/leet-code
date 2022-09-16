import unittest

from note import can_construct

class TestCanConstruct(unittest.TestCase):
    test_cases = [
        {
            'ransom_note': 'a',
            'magazine': 'b',
            'expected': False
        },
        {
            'ransom_note': 'aa',
            'magazine': 'aac',
            'expected': True
        },
                {
            'ransom_note': 'aa',
            'magazine': 'bab',
            'expected': False
        }
    ]

    def test_can_construct(self):
        for test_case in self.test_cases:
            result = can_construct(test_case['ransom_note'], test_case['magazine'])

            self.assertEqual(result, test_case['expected'])


if __name__ == '__main__':
    unittest.main()