
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "postgresql://admin:vansnoden1234@localhost:5432/crdss_db"
SQLALCHEMY_DATABASE_URL = "postgresql://postgres_db:5432/crdss_db?user=postgres&password=admin"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

