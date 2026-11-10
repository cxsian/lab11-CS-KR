# https://github.com/cxsian/lab11-CS-KR.git
# Partner 1: Cosmo Sian
# Partner 2: Kaylee Rodriguez

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self): # 3 assertions
        self.assertEqual(add(5,3), 8)
        self.assertEqual(add(10, -4), 6)
        self.assertEqual(add(15, 20), 35)

    def test_subtract(self): # 3 assertions
        self.assertEqual(sub(18, 8), 10)
        self.assertEqual(sub(10, -8), 18)
        self.assertEqual(sub(9, 12), -3)

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(-1, 5), -5)
        self.assertEqual(mul(0, 10), 0)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(20, 100), 5)
        self.assertEqual(div(-5, 25), -5)
        with self.assertRaises(ZeroDivisionError):
            div(0, 10)
    # ##########################

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
    #     # call division function inside, example:
    #     # with self.assertRaises(<INSERT_ERROR_TYPE>):
    #     #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(0,5)

    def test_logarithm(self): # 3 assertions
        self.assertEqual(log(2, 8), 3)
        self.assertEqual(log(2, 4), 2)
        self.assertEqual(log(3, 81), 4)

    def test_log_invalid_base(self): # 1 assertion
    #     # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            log(1, 8)
    
    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        # call log function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     logarithm(0, 5)
        with self.assertRaises(ValueError):
            log(0, 10)
        

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertEqual(hypotenuse(-3, -4), 5)
        self.assertEqual(hypotenuse(-3, 4), 5)

    def test_sqrt(self): # 3 assertions
        # Test for invalid argument, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #    square_root(NUM)
        # Test basic function
        self.assertEqual(square_root(9), 3)
        self.assertEqual(square_root(16), 4)
        with self.assertRaises(ValueError):
            square_root(-4)
    ##########################

# Do not touch this
if __name__ == "__main__":
    unittest.main()