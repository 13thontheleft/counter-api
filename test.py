import unittest
from app import CVCounter
from decimal import Decimal

cv_counter = CVCounter()


class MyTestCase(unittest.TestCase):
    # def __init__(self):
        # super().__init__()
        # self.data = cv_counter.get_total()

    def test_total_is_more_than_zero(self):
        data = cv_counter.get_total()
        self.assertEqual(data['total'] > 0, True)  # add assertion here

    def test_total_is_decimal(self):
        data = cv_counter.get_total()
        self.assertIsInstance(data['total'], Decimal)


if __name__ == '__main__':
    unittest.main()
