from typing import Optional
from pydantic import BaseModel, Field


class SHotelAdd(BaseModel):
    title:str = Field(None, description="Название отеля")
    location:str = Field(None, description="Адрес отеля")


class SHotel(SHotelAdd):
    id:int = Field(description="Id отеля")

