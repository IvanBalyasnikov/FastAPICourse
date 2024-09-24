from typing import List, Optional
from fastapi import APIRouter, Body, Query
from src.repositories.hotels import HotelsRepository
from src.schemas.hotels import SHotel, SHotelAdd, SHotelPATCH
from src.api.dependencies import PaginationDep
from src.database import async_session_maker
from src.api.hotels_examples import add_examples, put_examples

router = APIRouter(prefix="/hotels",
                   tags = ["Отели"])


@router.post("")
async def add_hotel(hotel:SHotelAdd = Body(openapi_examples=add_examples)):
    async with async_session_maker() as session:
        hotel_model = await HotelsRepository(session).add(hotel)
        await session.commit()
    return {"status":"OK", "data":hotel_model.__dict__}



@router.get("")
async def get_hotels(
    pagination:PaginationDep,
    title:Optional[str] = Query(None, description="Название отеля"),
    location:Optional[str] = Query(None, description="Местонахождение отеля"),
    ) -> List[SHotel]:
    per_page = pagination.per_page or 10
    async with async_session_maker() as session:
        hotels_models = await HotelsRepository(session).get_all(
            title,
            location,
            per_page,
            per_page * (pagination.page - 1)
            )
    
    return [SHotel.model_validate(hotel.__dict__) for hotel in hotels_models]


@router.put("/{hotel_id}")
async def edit_hotel(hotel_id:int,
                     hotel_data:SHotelAdd = Body(openapi_examples=put_examples)):
    async with async_session_maker() as session:
        await HotelsRepository(session).edit(hotel_data, id = hotel_id)
        await session.commit()

@router.patch("/{hotel_id}")
async def update_hotel(hotel_id:int,
                     hotel_data:SHotelPATCH = Body(openapi_examples=put_examples)):
    async with async_session_maker() as session:
        await HotelsRepository(session).edit(hotel_data, exclude_unset=True, id = hotel_id)
        await session.commit()


@router.delete("/{hotel_id}")
async def delete_hotel(hotel_id:int):
    async with async_session_maker() as session:
        await HotelsRepository(session).delete(id = hotel_id)
        await session.commit()

    

