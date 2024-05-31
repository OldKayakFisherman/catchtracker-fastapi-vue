from fastapi import File
from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from typing import Union, List
from typing_extensions import Annotated

class Catch(BaseModel):

    latitude: Decimal
    longitude: Decimal
    catch_date: datetime
    species: str
    weight: Union[Decimal, None]
    water_temperature: Union[Decimal, None]
    air_temperature: Union[Decimal, None]
    water_depth: Union[Decimal, None]
    sky_conditions: Union[str, None]
    terminal_tackle: Union[str, None]
    technique: Union[str, None]
    bait: Union[str, None]
    rod: Union[str, None]
    files: Union[Annotated[List[bytes], File(...)], None]

