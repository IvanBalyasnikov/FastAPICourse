from pydantic import BaseModel, Field, EmailStr


class SUserRequestAdd(BaseModel):
    email:EmailStr = Field(description="Email пользователя")
    password:str = Field(description="Пароль пользователя")


class SUserAdd(BaseModel):
    email:EmailStr = Field(description="Email пользователя")
    hashed_password:str = Field(description="Пароль пользователя")

class SUser(BaseModel):
    id:int = Field(description="Id пользователя")
    email:EmailStr = Field(description="Email пользователя")



