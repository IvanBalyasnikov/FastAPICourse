from typing import List, Optional
from fastapi import APIRouter, Body, Depends, Query
from src.schemas.hotels import SHotel, SHotelAdd
from src.api.dependencies import PaginationDep
from src.database import async_session_maker
from sqlalchemy import func, insert, select
from src.models.hotels import HotelsOrm
from src.api.hotels_examples import examples

router = APIRouter(prefix="/hotels",
                   tags = ["Отели"])


@router.post("")
async def add_hotel(hotel:SHotelAdd = Body(openapi_examples=examples)):
    async with async_session_maker() as session:
        stmt = insert(HotelsOrm).values(**hotel.model_dump())
        await session.execute(stmt)
        await session.commit()



@router.get("")
async def get_hotels(
    pagination:PaginationDep,
    title:Optional[str] = Query(None, description="Название отеля"),
    location:Optional[str] = Query(None, description="Местонахождение отеля"),
    ) -> List[SHotel]:
    per_page = pagination.per_page or 10
    async with async_session_maker() as session:
        query = select(HotelsOrm)
        if title:
            query = query.filter(func.lower(HotelsOrm.title).like(f"%{title.lower()}%"))
        if location:
            query = query.filter(func.lower(HotelsOrm.location).like(f"%{location.lower()}%"))
        query = (
            query
            .limit(per_page)
            .offset(per_page * (pagination.page - 1))
        )
        result = await session.execute(query)
        hotels_models = result.scalars().all()
    
    return [SHotel.model_validate(hotel.__dict__) for hotel in hotels_models]

    

