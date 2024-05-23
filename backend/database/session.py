from services.config import get_settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

settings = get_settings()


engine = create_engine(
    settings.sqlite_connection
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db_session():

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

