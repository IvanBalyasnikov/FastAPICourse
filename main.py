from typing import Optional
from fastapi import Body, FastAPI, Query
import uvicorn
from routers.hotels import router as hotels_router

app = FastAPI()
app.include_router(hotels_router)









if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)