import unittest
from features.reports import monthly_summary

class TestMonthlySummary(unittest.TestCase):
    def test_two_months(self):
        data = {"transactions": [{"amount": 100, "date": "2026-01-01"},
                                 {"amount": -12.5, "date": "2026-01-13"},
                                 {"amount": -4, "date": "2026-02-01"},
                                 {"amount": 300}]}
        self.assertEqual(monthly_summary(data), {
            "2026-01": {"income": 100, "spending": 12.5},
            "2026-02": {"income": 0, "spending": 4}})
    def test_undated(self):
        self.assertEqual(monthly_summary({"transactions": [{"amount": 10}]}), {})
