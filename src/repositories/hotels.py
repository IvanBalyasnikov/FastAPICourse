


from sqlalchemy import func, select
from src.schemas.hotels import SHotel
from src.models.hotels import HotelsOrm
from src.repositories.base import BaseRepository


class HotelsRepository(BaseRepository):
    model = HotelsOrm
    schema = SHotel

    async def get_all(self,
                title:str,
                location:str,
                limit:int,
                offset:int
                    ) -> list[SHotel]:
        query = select(HotelsOrm)
        if title:
            query = query.filter(func.lower(HotelsOrm.title).contains(title.strip().lower()))
        if location:
            query = query.filter(func.lower(HotelsOrm.location).contains(location.strip().lower()))
        query = (
            query
            .offset(offset)
            .limit(limit)
        )
        result = await self.session.execute(query)
        return [self.schema.model_validate(model, from_attributes=True) for model in result.scalars().all()]