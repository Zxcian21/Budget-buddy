import unittest
from features.core import top_spending_category


class TestTopCategory(unittest.TestCase):
    def test_accumulates_spending_and_ignores_income(self):
        transactions = [
            {"category": "food", "amount": -6},
            {"category": "fun", "amount": -10},
            {"category": "food", "amount": -7},
            {"category": "fun", "amount": 500},
        ]
        self.assertEqual(top_spending_category(transactions), "food")

    def test_no_expenses(self):
        self.assertIsNone(top_spending_category([{"category": "income", "amount": 4}]))
        self.assertIsNone(top_spending_category([]))
