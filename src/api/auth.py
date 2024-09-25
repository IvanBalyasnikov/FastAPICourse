from fastapi import APIRouter, Body
from src.repositories.users import UsersRepository
from src.schemas.users import SUserAdd, SUserRequestAdd
from src.database import async_session_maker
from src.api.users_examples import add_examples


router = APIRouter(prefix="/users",
                   tags = ["Аунтефикация "])


@router.post("/register")
async def register_user(
    user_data:SUserRequestAdd = Body(description="Информация для регистрации пользователей", openapi_examples=add_examples)
    ):
    hashed_password = user_data.password
    new_user_data = SUserAdd(email=user_data.email, hashed_password=hashed_password)
    async with async_session_maker() as session:
        await UsersRepository(session).add(new_user_data)
        await session.commit()
    return {"status":"OK"}



