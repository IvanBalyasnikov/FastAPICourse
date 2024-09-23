
from pydantic import BaseModel
from sqlalchemy import delete, insert, select, update, text
from sqlalchemy.ext.asyncio import AsyncSession
from database import Base

class BaseRepository():
    model:Base = None

    def __init__(self, session) -> None:
        self.session:AsyncSession = session

    async def get_all(self, *args, **kwargs):
        query = select(self.model)
        result = await self.session.execute(query)
        return result.scalars().all()
    
    async def get_one_or_none(self, **filter_by):
        query = select(self.model).filter_by(**filter_by)
        result = await self.session.execute(query)
        return result.scalars().one_or_none()
    
    async def add(self, data:BaseModel):
        stmt = insert(self.model).values(**data.model_dump()).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().one()
    
    async def edit(self, data:BaseModel, **filter_by):
        stmt = update(self.model).filter_by(**filter_by).values(**data.model_dump())
        await self.session.execute(stmt)

    async def delete(self, **filter_by):
        stmt = delete(self.model).filter_by(**filter_by)
        await self.session.execute(stmt)