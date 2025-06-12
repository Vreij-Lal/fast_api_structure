import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://user:pass@host:port/dbname"

engine = create_engine(DATABASE_URL, echo=False, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def load_sql(path: str) -> str:
    base = os.path.join(os.path.dirname(__file__), "..", "sql")
    return open(os.path.join(base, path), encoding="utf-8").read()
