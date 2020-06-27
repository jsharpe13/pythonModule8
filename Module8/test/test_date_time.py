import unittest
import datetime
from more_fun_with_collections import date_time


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        Birthday = datetime.datetime(2020, 1, 23,)
        result = date_time.half_birthday(Birthday)
        expected = datetime.datetime(2020, 7, 23, 12, 0)
        self.assertEquals(result, expected)


if __name__ == '__main__':
    unittest.main()