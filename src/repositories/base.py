
from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update, text
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base

class BaseRepository():
    model:Base = None
    schema:BaseModel

    def __init__(self, session) -> None:
        self.session:AsyncSession = session

    async def get_all(self, *args, **kwargs) -> list[BaseModel]:
        query = select(self.model)
        result = await self.session.execute(query)
        return [self.schema.model_validate(model, from_attributes=True) for model in result.scalars().all()]
    
    async def get_one_or_none(self, **filter_by) -> BaseModel | None:
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        model = result.scalars().one_or_none()
        if model:
            return self.schema.model_validate(model, from_attributes=True)
    
    async def add(self, data:BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(stmt)
        model = result.scalars().one_or_none()
        return self.schema.model_validate(model, from_attributes=True)
    
    async def edit(self, data:BaseModel, exclude_unset:bool = False, **filter_by):
        stmt = (
            update(self.model)
            .filter_by(**filter_by)
            .values(**data.model_dump(exclude_unset=exclude_unset))
            )
        await self.session.execute(stmt)

    async def delete(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)