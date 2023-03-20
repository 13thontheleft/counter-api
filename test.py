import json
import unittest
from app import CVCounter, lambda_handler
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

    def test_total_is_JSON_object(self):
        data = lambda_handler(None, None)
        self.assertIs(self.is_json(data), True)

    def is_json(self, myjson):
        try:
            json.loads(myjson)
        except ValueError as e:
            return False
        return True


if __name__ == '__main__':
    unittest.main()
