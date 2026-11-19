import unittest
from features.reports import category_report


class TestCategoryReport(unittest.TestCase):
    def test_mixed_totals(self):
        data = {"transactions": [
            {"category": "food", "amount": -5.25},
            {"category": "food", "amount": -4.75},
            {"category": "income", "amount": 20},
            {"category": "food", "amount": 2},
        ]}
        self.assertEqual(category_report(data), {"food": -8, "income": 20})

    def test_empty(self):
        self.assertEqual(category_report({"transactions": []}), {})
