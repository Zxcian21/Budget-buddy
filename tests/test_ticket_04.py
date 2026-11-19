import unittest
from features.core import set_category_budget, category_budget_status, over_budget_categories

class TestBudgets(unittest.TestCase):
    def test_under_and_over(self):
        data = {"transactions": [{"amount": -12, "category": "food"}, {"amount": -15, "category": "fun"}]}
        set_category_budget(data, "food", 20)
        set_category_budget(data, "fun", 10)
        self.assertFalse(category_budget_status(data, "food")["over_budget"])
        self.assertTrue(category_budget_status(data, "fun")["over_budget"])
        self.assertEqual(list(over_budget_categories(data)), ["fun"])

    def test_missing_and_invalid(self):
        data = {"transactions": []}
        with self.assertRaises(ValueError):
            category_budget_status(data, "food")
        with self.assertRaises(ValueError):
            set_category_budget(data, "food", 0)
