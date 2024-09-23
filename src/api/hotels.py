from typing import List
from fastapi import APIRouter, Depends
from src.schemas.hotels import SHotel, SHotelAdd, SHotelPUT, SHotelGET, SSuccess
from src.api.dependencies import PaginationDep


router = APIRouter(prefix="/hotels",
                   tags = ["Отели"])


hotels = [
    {"id": 1, "title": "Sochi", "name": "sochi"},
    {"id": 2, "title": "Дубай", "name": "dubai"},
    {"id": 3, "title": "Мальдивы", "name": "maldivi"},
    {"id": 4, "title": "Геленджик", "name": "gelendzhik"},
    {"id": 5, "title": "Москва", "name": "moscow"},
    {"id": 6, "title": "Казань", "name": "kazan"},
    {"id": 7, "title": "Санкт-Петербург", "name": "spb"},
]


@router.get("")
def get_hotels(
    pagination:PaginationDep,
    hotel:SHotelGET = Depends(),
    ) -> List[SHotel]:
    global hotels
    target_hotels = []
    for hotel_ in hotels:
        if hotel.id and hotel.id!= hotel_['id']:
            continue
        if hotel.title and hotel.title!= hotel_['title']:
            continue
        if hotel.name and hotel.name!= hotel_['name']:
            continue
        target_hotels.append(hotel_)
    if pagination.page:
        pagination.page-=1
        if pagination.per_page:
            target_hotels = target_hotels[pagination.page*pagination.per_page:(pagination.page+1)*pagination.per_page]
        else:
            target_hotels = target_hotels[pagination.page*2:(pagination.page+1)*2]

    return target_hotels



@router.patch("/hotels/{hotel_id}")
def change_hotel(hotel_id:int,
                 hotel:SHotelAdd
                 ) -> SSuccess:
    global hotels
    target_hotel = [hotel_ for hotel_ in hotels if hotel['id'] == hotel_id][0]
    if hotel.title:
        target_hotel['title'] = hotel.title
    if hotel.name:
        target_hotel['name'] = hotel.name
    return {"status": "OK"}


@router.put("/hotels/{hotel_id}")
def update_hotel(hotel_id:int,
                 hotel:SHotelPUT
                 ) -> SSuccess:
    global hotels
    target_hotel = [hotel for hotel in hotels if hotel['id'] == hotel_id][0]
    target_hotel['title'] = hotel.title
    target_hotel['name'] = hotel.name
    return {"status": "OK"}