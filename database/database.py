import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional

DB_DIR = Path(__file__).resolve().parent
DB_PATH = DB_DIR / "database.db"


def get_db_path(db_path: Optional[Path] = None) -> Path:
    return db_path or DB_PATH


def init_db(db_path: Optional[Path] = None) -> Path:
    path = get_db_path(db_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS prediction_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            state TEXT NOT NULL,
            crop TEXT NOT NULL,
            prediction REAL NOT NULL
        )
        """
    )
    conn.commit()
    conn.close()
    return path


def insert_prediction(
    state: str,
    crop: str,
    prediction: float,
    db_path: Optional[Path] = None,
) -> int:
    path = init_db(db_path)
    conn = sqlite3.connect(path)
    cursor = conn.execute(
        """
        INSERT INTO prediction_history (date, state, crop, prediction)
        VALUES (?, ?, ?, ?)
        """,
        (datetime.now(timezone.utc).isoformat(), state, crop, float(prediction)),
    )
    conn.commit()
    row_id = cursor.lastrowid
    conn.close()
    return row_id


def get_prediction_history(db_path: Optional[Path] = None) -> list[dict[str, Any]]:
    path = init_db(db_path)
    conn = sqlite3.connect(path)
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT id, date, state, crop, prediction FROM prediction_history ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return [dict(row) for row in rows]
