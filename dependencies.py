from typing import Annotated, Optional
from fastapi import Query
from pydantic import BaseModel

class DHotelsPagination(BaseModel):
    page:Annotated[Optional[int], Query(None, description="Страница")]
    per_page:Annotated[Optional[int], Query(None, description="Сколько на странице")]

