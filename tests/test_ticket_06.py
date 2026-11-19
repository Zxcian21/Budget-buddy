import unittest
from features.core import set_savings_goal, savings_goal_progress

class TestSavingsGoal(unittest.TestCase):
    def test_under_at_over(self):
        data = {"starting_balance": 50, "transactions": []}
        set_savings_goal(data, 100)
        self.assertEqual(savings_goal_progress(data), 50)
        set_savings_goal(data, 50)
        self.assertEqual(savings_goal_progress(data), 100)
        set_savings_goal(data, 20)
        self.assertEqual(savings_goal_progress(data), 100)
    def test_invalid_or_unset(self):
        data = {"starting_balance": -10, "transactions": []}
        self.assertEqual(savings_goal_progress(data), 0)
        data["savings_goal"] = 0
        self.assertEqual(savings_goal_progress(data), 0)
        with self.assertRaises(ValueError):
            set_savings_goal(data, -1)
