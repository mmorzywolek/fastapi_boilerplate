import sqlalchemy
import databases

DATABASE_URL = "postgresql://inbdwlwqdarcns:c02e007044c8db5c9c264351cd5727d9587a872b543b244b037873ec6c12e01c@ec2-34-247-72-29.eu-west-1.compute.amazonaws.com:5432/d3fh43dgaonv24"
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
