from fastapi import APIRouter, Depends, HTTPException, status, Request
from database.session import get_db_session
from sqlalchemy.orm import Session
from database.repositories import LookupRepository, StatRepository
from api.parameters import Catch
from helpers import assign_dict_from_variables


router = APIRouter(prefix="/v1", tags=["v1"])

@router.get("/lookups")
async def lookups(db: Session = Depends(get_db_session)):    

    repo = LookupRepository()
    
    result = {
        "baits": repo.get_unique_catch_baits(db),
        "rods": repo.get_unique_catch_rods(db),
        "sky": repo.get_unique_catch_sky_conditions(db),
        "species": repo.get_unique_catch_species(db),
        "techniques": repo.get_unique_catch_techniques(db),
        "terminal_tackle": repo.get_unique_catch_terminal_tackle(db)
    }

    return result

@router.get('/stats')
async def stats(db: Session = Depends(get_db_session)):
    
    repo = StatRepository()

    result = {
        "prior_yr_top_baits" : repo.prior_yr_top_baits(db),
        "prior_yr_top_techniques": repo.prior_yr_top_techniques(db),
        "ytd_catch_stats_by_species": repo.ytd_catch_stats_by_species(db),
        "ytd_top_techniques": repo.ytd_top_techniques(db),
        "ytd_top_baits": repo.ytd_top_baits(db),
        "ytd_catch_stats_overall": repo.ytd_catch_stats_overall(db),
    }

    return result    
    
@router.post('/addcatch')
async def addCatch(catch: Catch, db: Session = Depends(get_db_session)):

    db_model = assign_dict_from_variables(catch)

    

    return status.HTTP_200_OK
