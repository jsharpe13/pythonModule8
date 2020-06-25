import unittest
from more_fun_with_collections import set_membership


class MyTestCase(unittest.TestCase):
    def test_in_set_true(self):
        this_set = {1, 1, 2, 3, 4}
        self.assertTrue(set_membership.in_set(this_set, 3))

    def test_in_set_false(self):
        this_set = {1, 1, 2, 3, 4}
        self.assertFalse(set_membership.in_set(this_set, 7))


if __name__ == '__main__':
    unittest.main()
