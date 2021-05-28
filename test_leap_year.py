import unittest
import leap_year


class TestCase(unittest.TestCase):
    def test_input_1(self):
        self.assertEqual(leap_year.check_user_input(2000), 2000)
    
    def test_check_1(self):
        self.assertEqual(leap_year.check_leap_year(2000), 2)
    
    def test_check_2(self):
        self.assertEqual(leap_year.check_leap_year(2000), 1)

if __name__ == "__main__":
    unittest.main()
