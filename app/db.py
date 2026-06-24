from sqlalchemy import create_engine
# malformed URL — extra .db suffix
engine = create_engine("postgresql://admin:admin@localhost:5432/testdb")
