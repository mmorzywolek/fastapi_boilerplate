import os

import sqlalchemy
import databases
from dotenv import load_dotenv

load_dotenv()


DATABASE_URL = os.getenv('DATABASE_URI')
database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

Article = sqlalchemy.Table(
    "article",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("title", sqlalchemy.String(100)),
    sqlalchemy.Column("description", sqlalchemy.String(500))
)

User = sqlalchemy.Table(
    "user",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("username", sqlalchemy.String(100)),
    sqlalchemy.Column("password", sqlalchemy.String(500))
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
