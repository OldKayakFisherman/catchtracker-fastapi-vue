from faker import Faker
from faker.providers import internet, address
from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models import Base

@contextmanager
def get_db_text_session():

    engine = create_engine(
        'sqlite:///:memory:'
    )

    Base.metadata.create_all(engine)

    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()



def create_test_catch_records(number):

    records = []

    species = ['Bass', 'Crappie', 'Perch', 'Catfish']
    sky_conditions = ['Sunny', 'Partly Cloudy', 'Cloudy']
    terminal_tackle = ['swivel', '5/0 EWGHook', '2/0 Worm Hook', '3/16 Weight', '1/8 Weight']
    techniques = ['Texas Rig', 'Aggressive Jerkbait Retrieve']
    baits = ['Zoom Green Pumpkin Speed Craw', 'Rapala Purple/Yellow Jerkbait']
    rods = ['Rod 1','Rod 2', 'Rod 3']

    faker = Faker()

    for i in range(1, number):

        record = {
            "latitude": faker.latitude(),
            "longitude": faker.longitude(),
            "catch_date": faker.past_date(),
            "species": faker.random_choices(species, 1)[0],
            "weight": faker.pydecimal(),
            "water_temperature": faker.pydecimal(),
            "air_temperature": faker.pydecimal(),
            "water_depth": faker.pydecimal(),
            "sky_conditions": faker.random_choices(sky_conditions, 1)[0],
            "terminal_tackle": faker.random_choices(terminal_tackle, 1)[0],
            "technique": faker.random_choices(techniques, 1)[0],
            "bait": faker.random_choices(baits, 1)[0],
            "rod": faker.random_choices(rods, 1)[0],
        }

        records.append(record)

    return records
