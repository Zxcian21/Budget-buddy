import unittest
from features.core import search_transactions

class TestSearch(unittest.TestCase):
    def test_matches_case_insensitively(self):
        tx = [{"description": "School lunch"}, {"description": "Bus"}, {"description": "School supplies"}]
        self.assertEqual(search_transactions(tx, "sChOoL"), [tx[0], tx[2]])
    def test_empty_result(self):
        self.assertEqual(search_transactions([{"description": "Lunch"}], "movie"), [])
