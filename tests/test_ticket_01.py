import unittest
from features.core import big_expenses


class TestBigExpenses(unittest.TestCase):
    def setUp(self):
        self.transactions = [
            {"amount": -12, "description": "Movie"},
            {"amount": -4, "description": "Snack"},
            {"amount": 30, "description": "Allowance"},
            {"amount": -10, "description": "Book"},
        ]

    def test_mixed_transactions_and_inclusive_threshold(self):
        self.assertEqual([t["description"] for t in big_expenses(self.transactions, 10)], ["Movie", "Book"])

    def test_no_matches(self):
        self.assertEqual(big_expenses(self.transactions, 50), [])

    def test_invalid_threshold(self):
        for value in (0, -1, float("nan"), float("inf")):
            with self.subTest(value=value), self.assertRaises(ValueError):
                big_expenses(self.transactions, value)
