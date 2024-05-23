from sqlalchemy.orm import Session
from database.models import CatchDetail, Media, SearchIndex
from helpers import assign_variables_from_dict
from typing import List

class LookupRepository:

    def get_unique_catch_techniques(self, db: Session):
        return db.query(CatchDetail.technique).distinct().all()

    def get_unique_catch_species(self, db: Session):
        return db.query(CatchDetail.species).distinct().all()

    def get_unique_catch_sky_conditions(self, db: Session):
        return db.query(CatchDetail.sky_conditions).distinct().all()

    def get_unique_catch_terminal_tackle(self, db: Session):
        return db.query(CatchDetail.terminal_tackle).distinct().all()

    def get_unique_catch_baits(self, db: Session):
        return db.query(CatchDetail.bait).distinct().all()

    def get_unique_catch_rods(self, db: Session):
        return db.query(CatchDetail.rod).distinct().all()

class CatchRepository:

    def add_catches(self, db: Session, raw_catch_records: List[dict]):

        results = []

        for raw_catch_record in raw_catch_records:
            model: CatchDetail = assign_variables_from_dict(CatchDetail(), raw_catch_record)
            db.add(model)
            results.append(model) 

        db.flush()
    
        return results

    def add_catch(self, db: Session, raw_catch_record: dict):
    
        #Rehydrate the model
        model: CatchDetail = assign_variables_from_dict(CatchDetail(), raw_catch_record)
    
        db.add(model)
        db.flush()

        return model
