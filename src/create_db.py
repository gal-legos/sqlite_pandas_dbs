import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "clinic_simple.db"
CSV_PATH = ROOT / "data" / "patients.csv"
SCHEMA_PATH = ROOT / "sql" / "schema.sql"


def main():

    # Read the schema SQL file.
    schema_sql = SCHEMA_PATH.read_text(encoding="utf-8")

    # Create (or overwrite) the database and apply the schema.
    with sqlite3.connect(DB_PATH) as conn:
        conn.executescript(schema_sql)
        conn.commit()

    print(f"Created database: {DB_PATH}")


if __name__ == "__main__":
    main()