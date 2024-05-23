from fastapi import APIRouter, Depends, HTTPException, status, Request
from database.session import get_db_session
from sqlalchemy.orm import Session
from database.repositories import LookupRepository


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



