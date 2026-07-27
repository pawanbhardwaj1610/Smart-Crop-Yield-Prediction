import sys
import tempfile
import unittest
from pathlib import Path

ROOT_DIR = Path(__file__).resolve().parents[1]
if str(ROOT_DIR) not in sys.path:
    sys.path.insert(0, str(ROOT_DIR))

from database.database import get_prediction_history, init_db, insert_prediction


class DatabaseTests(unittest.TestCase):
    def test_prediction_history_round_trip(self) -> None:
        with tempfile.TemporaryDirectory() as tmpdir:
            db_path = Path(tmpdir) / "test.db"

            init_db(db_path=db_path)
            row_id = insert_prediction(
                state="Punjab",
                crop="Wheat",
                prediction=2.5,
                db_path=db_path,
            )

            self.assertIsNotNone(row_id)
            history = get_prediction_history(db_path=db_path)

            self.assertEqual(len(history), 1)
            self.assertEqual(history[0]["state"], "Punjab")
            self.assertEqual(history[0]["crop"], "Wheat")
            self.assertAlmostEqual(history[0]["prediction"], 2.5)


if __name__ == "__main__":
    unittest.main()
