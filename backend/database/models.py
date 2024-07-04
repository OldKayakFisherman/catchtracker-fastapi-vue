from decimal import Decimal
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import relationship, mapped_column, Mapped, DeclarativeBase
from typing import List
from datetime import datetime


class Base(DeclarativeBase):
    pass


class CatchDetail(Base):
    
    __tablename__ = "catch_details"


    id: Mapped[int] = mapped_column(primary_key=True)
    latitude: Mapped[Decimal] = mapped_column(nullable=False)
    longitude: Mapped[Decimal] = mapped_column(nullable=False)
    catch_date: Mapped[datetime] = mapped_column(nullable=False)
    species: Mapped[str] = mapped_column(String(100), nullable=False)
    weight: Mapped[Decimal]
    water_temperature: Mapped[Decimal]
    air_temperature: Mapped[Decimal]
    water_depth: Mapped[Decimal]
    sky_conditions: Mapped[str] = mapped_column(String(100))
    terminal_tackle: Mapped[str] = mapped_column(String(1000))
    technique: Mapped[str] = mapped_column(String(1000))
    bait: Mapped[str] = mapped_column(String(1000))
    rod: Mapped[str] = mapped_column(String(1000))

    def from_dict(self, args:dict):
        if args["id"]:
            self.id = int(args["id"]) 
        if args["latitude"]:
            self.latitude = float(args["latitude"])
        if args["longitude"]:
            self.longitude = float(args["longitude"])
        if args["catch_date"]:
            self.catch_date = args["catch_date"]
        if args["species"]:
            self.species = args["species"]


class Media(Base):

    __tablename__ = "media"


    id: Mapped[int] = mapped_column(primary_key=True)
    file_size: Mapped[int] = mapped_column(nullable=False)
    filename: Mapped[str] = mapped_column(nullable=False)
    extension: Mapped[str] = mapped_column(nullable=False)
    mimetype: Mapped[str] = mapped_column(nullable=False)
    upload_date: Mapped[datetime] = mapped_column(nullable=False)
    content: Mapped[FileField] = 
    catch_detail_id : Mapped[int] = mapped_column(ForeignKey("catch_details.id"))
    catch_detail: Mapped[CatchDetail] = relationship("CatchDetail", order_by=id)
    

class SearchIndex(Base):

    __tablename__ = "simple_search_index"

    id: Mapped[int] = mapped_column(primary_key=True)
    data: Mapped[str] = mapped_column(nullable=False)
    catch_detail_id : Mapped[int] = mapped_column(ForeignKey("catch_details.id"))
    catch_detail: Mapped[CatchDetail] = relationship("CatchDetail", order_by=id)

