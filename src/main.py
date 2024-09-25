from typing import Optional
from fastapi import Body, FastAPI, Query
import uvicorn
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))


from src.api.hotels import router as hotels_router
from src.api.auth import router as auth_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(hotels_router)









if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)