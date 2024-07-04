from fastapi import UploadFile
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from typing import Union, List, Optional
from typing_extensions import Annotated

class Catch(BaseModel):

    latitude: Decimal
    longitude: Decimal
    catch_date: datetime
    species: str
    weight: Optional[Decimal]= None
    water_temperature: Optional[Decimal]= None
    air_temperature: Optional[Decimal]= None
    water_depth: Optional[Decimal]= None
    sky_conditions: Optional[str]= None
    terminal_tackle: Optional[str]= None
    technique: Optional[str]= None
    bait: Optional[str]= None
    rod: Optional[str]=None
    
