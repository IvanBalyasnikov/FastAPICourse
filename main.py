from typing import Optional
from fastapi import Body, FastAPI, Query
import uvicorn


app = FastAPI()


hotels = [
    {"id":1, "title": "Sochi", "name":"sochi"},
    {"id":2, "title": "Dubai", "name":"dubai"},
    {"id":3, "title": "Moscow", "name":"moscow"},
]


@app.get("/hotels")
def get_hotels(
    id:Optional[int] = Query(None, description="Id of the hotel"),
    title:Optional[str] = Query(None, description="Title of the hotel"),
    name:Optional[str] = Query(None, description="Name of the hotel"),
    ):
    target_hotels = []
    for hotel in hotels:
        if id and id!= hotel['id']:
            continue
        if title and title!= hotel['title']:
            continue
        if name and name!= hotel['name']:
            continue
        target_hotels.append(hotel)
    return target_hotels



@app.patch("/hotels/{hotel_id}")
def change_hotel(hotel_id:int,
                 title:Optional[str] = Body(None, description="The title of hotel"),
                 name:Optional[str] = Body(None, description = "The name of hotel")
                 ):
    global hotels
    target_hotel = [hotel for hotel in hotels if hotel['id'] == hotel_id][0]
    if title:
        target_hotel['title'] = title
    if name:
        target_hotel['name'] = name
    return {"status": "OK"}


@app.put("/hotels/{hotel_id}")
def update_hotel(hotel_id:int,
                 title:str = Body(description="The title of hotel"),
                 name:str = Body(description = "The name of hotel")
                 ):
    global hotels
    target_hotel = [hotel for hotel in hotels if hotel['id'] == hotel_id][0]
    target_hotel['title'] = title
    target_hotel['name'] = name
    return {"status": "OK"}




if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)