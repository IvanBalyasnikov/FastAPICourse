
from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

class BaseRepository():
    model = None

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
    
    async def add(self, data):
        stmt = insert(self.model).values(**data).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalars().one()