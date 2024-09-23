from typing import Annotated, Optional
from fastapi import Depends, Query
from pydantic import BaseModel

class DHotelsPagination(BaseModel):
    page:Annotated[int, Query(1, description="Страница", ge=1)]
    per_page:Annotated[Optional[int], Query(None, description="Сколько на странице", ge=1, lt=30)]


PaginationDep = Annotated[DHotelsPagination, Depends()]

