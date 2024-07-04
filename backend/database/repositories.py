from sqlalchemy.orm import Session
from sqlalchemy import func, desc, text
from database.models import CatchDetail, Media, SearchIndex
from helpers import assign_object_from_dict
from typing import List
from datetime import datetime

class LookupRepository:

    def get_unique_catch_techniques(self, db: Session):
        return db.query(CatchDetail.technique).distinct().order_by(CatchDetail.technique).all()

    def get_unique_catch_species(self, db: Session):
        return db.query(CatchDetail.species).distinct().order_by(CatchDetail.species).all()

    def get_unique_catch_sky_conditions(self, db: Session):
        return db.query(CatchDetail.sky_conditions).distinct().order_by(CatchDetail.sky_conditions).all()

    def get_unique_catch_terminal_tackle(self, db: Session):
        return db.query(CatchDetail.terminal_tackle).distinct().order_by(CatchDetail.terminal_tackle).all()

    def get_unique_catch_baits(self, db: Session):
        return db.query(CatchDetail.bait).distinct().order_by(CatchDetail.bait).all()

    def get_unique_catch_rods(self, db: Session):
        return db.query(CatchDetail.rod).distinct().order_by(CatchDetail.rod).all()

class CatchRepository:

    def add_catches(self, db: Session, raw_catch_records: List[dict]):

        results = []

        for raw_catch_record in raw_catch_records:
            model: CatchDetail = assign_object_from_dict(CatchDetail(), raw_catch_record)
            db.add(model)
            results.append(model) 

        db.flush()
    
        return results

    def add_catch(self, db: Session, raw_catch_record: dict):
    
        #Rehydrate the model
        model: CatchDetail = assign_object_from_dict(CatchDetail(), raw_catch_record)
    
        db.add(model)
        db.flush()

        return model


class StatRepository:

    def ytd_catch_stats_overall(self, db: Session):

        current_year = datetime.now().year

        date_start_filter = f'{current_year}-01-01'
        date_end_filter = f'{current_year}-12-31'
        
        return db.query(CatchDetail.species ,func.count(CatchDetail.id)).\
            filter(CatchDetail.catch_date >= date_start_filter). \
            filter(CatchDetail.catch_date <= date_end_filter). \
            group_by(CatchDetail.species). \
            all()
        
        #if result:
        #    return result[0][0]

    def ytd_catch_stats_by_species(self, db: Session):

        current_year = datetime.now().year

        date_start_filter = f'{current_year}-01-01'
        date_end_filter = f'{current_year}-12-31'
        
        return db.query(CatchDetail.species, func.count(CatchDetail.species)).\
            filter(CatchDetail.catch_date >= date_start_filter). \
            filter(CatchDetail.catch_date <= date_end_filter). \
            group_by(CatchDetail.species). \
            all()

    def ytd_top_techniques(self, db: Session):

        current_year = datetime.now().year

        date_start_filter = f'{current_year}-01-01'
        date_end_filter = f'{current_year}-12-31'
        
        return db.query(CatchDetail.technique, func.count(CatchDetail.technique).label("count")).\
            filter(CatchDetail.catch_date >= date_start_filter). \
            filter(CatchDetail.catch_date <= date_end_filter). \
            group_by(CatchDetail.technique). \
            order_by(text("count desc")). \
            limit(3). \
            all()

    def prior_yr_top_techniques(self, db: Session):

        current_year = datetime.now().year

        date_start_filter = f'{(current_year -1)}-01-01'
        date_end_filter = f'{(current_year -1)}-12-31'
        
        return db.query(CatchDetail.technique, func.count(CatchDetail.technique).label("count")).\
            filter(CatchDetail.catch_date >= date_start_filter). \
            filter(CatchDetail.catch_date <= date_end_filter). \
            group_by(CatchDetail.technique). \
            order_by(text("count desc")). \
            limit(3). \
            all()

    def ytd_top_baits(self, db: Session):

        current_year = datetime.now().year

        date_start_filter = f'{current_year}-01-01'
        date_end_filter = f'{current_year}-12-31'
        
        return db.query(CatchDetail.bait, func.count(CatchDetail.bait).label("count")).\
            filter(CatchDetail.catch_date >= date_start_filter). \
            filter(CatchDetail.catch_date <= date_end_filter). \
            group_by(CatchDetail.bait). \
            order_by(text("count desc")). \
            limit(3). \
            all()

    def prior_yr_top_baits(self, db: Session):

        current_year = datetime.now().year

        date_start_filter = f'{(current_year -1)}-01-01'
        date_end_filter = f'{(current_year -1)}-12-31'
        
        return db.query(CatchDetail.bait, func.count(CatchDetail.bait).label("count")).\
            filter(CatchDetail.catch_date >= date_start_filter). \
            filter(CatchDetail.catch_date <= date_end_filter). \
            group_by(CatchDetail.bait). \
            order_by(text("count desc")). \
            limit(3). \
            all()
