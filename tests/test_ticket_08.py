import csv
import unittest
from pathlib import Path
from tempfile import TemporaryDirectory
from features.core import export_transactions_csv

class TestCsv(unittest.TestCase):
    def test_round_trip(self):
        tx = [{"id": 1, "description": "Movie, popcorn", "amount": -12.5, "category": "fun"},
              {"id": 2, "description": "Gift", "amount": 20, "category": "income"}]
        with TemporaryDirectory() as directory:
            path = Path(directory) / "tx.csv"
            export_transactions_csv(tx, path)
            with path.open(newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                self.assertEqual(reader.fieldnames, ["id", "description", "amount", "category"])
                self.assertEqual(list(reader), [
                    {"id": "1", "description": "Movie, popcorn", "amount": "-12.5", "category": "fun"},
                    {"id": "2", "description": "Gift", "amount": "20", "category": "income"}])
