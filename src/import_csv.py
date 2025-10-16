import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB_PATH = ROOT / "clinic_simple.db"
CSV_PATH = ROOT / "data" / "patients.csv"


def main():
    try:
        # reading the csv file
        df = pd.read_csv(CSV_PATH, dtype=str)

        # creating database engine
        engine = create_engine(f"sqlite:///{DB_PATH}")

        df.to_sql(
            "patients",
            con=engine,
            if_exists="append",
            index=False,
        )

        # verifying the number of rows loaded
        sql_count = text("SELECT COUNT(*) FROM patients")
        with engine.connect() as conn:
            result = conn.execute(sql_count)
            total = result.scalar_one()

        print(f"Loaded {len(df)} rows into patients. Table now has {total} rows.")

    except Exception as exc:
        print("Error importing CSV:", exc)


if __name__ == "__main__":
    main()
