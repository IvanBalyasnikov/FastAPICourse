from typing import Optional
from pydantic import BaseModel, Field


class SHotelAdd(BaseModel):
    title:Optional[str] = Field(None, description="Название отеля")
    name:Optional[str] = Field(None, description="Именной идентификатор отеля")


class SHotel(SHotelAdd):
    id:int = Field(description="Id отеля")

class SHotelGET(SHotelAdd):
    id:Optional[int] = Field(None, description="Id отеля")



class SHotelPUT(BaseModel):
    title:str = Field(description="Название отеля")
    name:str = Field(description="Именной идентификатор отеля")

class SSuccess(BaseModel):
    status:str = Field(description="Статус выполнения")