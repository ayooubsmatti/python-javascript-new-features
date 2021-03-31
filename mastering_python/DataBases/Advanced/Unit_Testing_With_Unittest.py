# -----------------------------------------------------------
# ----- Advanced_lessons Unit Testing With Unittest--- -------
# -----------------------------------------------------------
# Test Runner
# -- the module that run the unit Testing (unittest,pytest)
# ---------------------------------------------------
# test case
# -- smalles unit of testing
# -- it use asserts methods to check for actions and responses
# - Test suite
# -- collection of multiple tests or test cases
# -Test Report
# -- A Full report contains the failure or succees
# --------------------------------------------------------
# -unitest
# ---add tests into classes as methods
# ---use a series of special assertion methods
# -https://docs.python.org/3/library/unittest.html
# --------------------------------------------------------
# assert 3*8 == 24, "shuld be 24"
# # --------------------------------
# def test_case_one():

#     assert 5*10 == 50, "shuld be 50"


# def test_case_two():

#     assert 5*50 == 2240, "shuld be 250"


# if __name__ == "__main__":
#     test_case_one()
#     test_case_two()
#     print("All test pass")
# -------------------------------------
import unittest


class MyTestCase(unittest.TestCase):
    def test_one(self):
        self.assertTrue(100 > 97, "should be true")

    def test_two(self):
        self.assertEqual(40+60, 100, "should be 100")

    def test_three(self):
        self.assertGreater(100, 80, "should be true")


if __name__ == "__main__":
    unittest.main()
