from sqlalchemy import func, select
from src.schemas.users import SUser
from src.models.users import UsersOrm
from src.repositories.base import BaseRepository


class UsersRepository(BaseRepository):
    model = UsersOrm
    schema = SUser

   