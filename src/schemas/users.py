from pydantic import BaseModel, Field


class SUserRequestAdd(BaseModel):
    email:str = Field(description="Email пользователя")
    password:str = Field(description="Пароль пользователя")


class SUserAdd(BaseModel):
    email:str = Field(description="Email пользователя")
    hashed_password:str = Field(description="Пароль пользователя")

class SUser(BaseModel):
    id:int = Field(description="Id пользователя")
    email:str = Field(description="Email пользователя")



