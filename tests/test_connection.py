"""Repeatable SQLite connection test (Hito 1)."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from viajes_aventura.persistence.connection import get_connection, init_db  # noqa: E402

EXPECTED_TABLES = {
    "users",
    "destinations",
    "tour_packages",
    "package_destinations",
    "reservations",
}


class TestSQLiteConnection(unittest.TestCase):
    def setUp(self):
        self.conn = get_connection(":memory:")
        init_db(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_tables_created(self):
        rows = self.conn.execute(
            "SELECT name FROM sqlite_master WHERE type='table'"
        ).fetchall()
        names = {row["name"] for row in rows}
        self.assertTrue(EXPECTED_TABLES.issubset(names))

    def test_foreign_key_enforced(self):
        with self.assertRaises(Exception):
            self.conn.execute(
                "INSERT INTO reservations (user_id, package_id, reserved_at, "
                "people_count, total_price) VALUES (999, 999, '2026-01-01', 1, 10)"
            )

    def test_insert_and_read_user(self):
        self.conn.execute(
            "INSERT INTO users (name, email, password_hash) VALUES (?, ?, ?)",
            ("Ana", "ana@example.com", "hash123"),
        )
        row = self.conn.execute("SELECT * FROM users").fetchone()
        self.assertEqual(row["email"], "ana@example.com")
        self.assertEqual(row["role"], "client")


if __name__ == "__main__":
    unittest.main()
