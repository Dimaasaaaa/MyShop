from pathlib import Path
import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"
load_dotenv(dotenv_path=ENV_PATH)

def clean(value: str | None) -> str:
    if not value:
        return ""

    return "".join(c for c in value if c.isprintable()).strip()

DB_USER = clean(os.getenv("DB_USER"))
DB_PASSWORD = clean(os.getenv("DB_PASSWORD"))
DB_HOST = clean(os.getenv("DB_HOST"))
DB_PORT = clean(os.getenv("DB_PORT"))
DB_NAME = clean(os.getenv("DB_NAME"))

DATABASE_URL = (
    f"postgresql+psycopg://"
    f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL, echo=True, future=True)


class Base(DeclarativeBase):
    pass

ENV_PATH = BASE_DIR / '.env'
load_dotenv(dotenv_path=ENV_PATH)
