import unittest

from sum_nuemros import sum_number

class TestSumNumbers(unittest.TestCase):
    
    def test_sum_numbers_default(self):
        """Test that the default value is a list"""
        self.assertEqual(sum_number(), 5050)
        self.assertEqual(sum_number(numbers=None), 5050)
        

    def test_sum_numbers_with_list(self):
        self.assertEqual(sum_number([1, 2, 3]), 6)


if __name__ == '__main__':
    unittest.main()