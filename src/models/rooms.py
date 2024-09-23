from typing import Optional
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String, ForeignKey


class RoomsOrm(Base):
    __tablename__ = "hotels"

    id:Mapped[int] = mapped_column(primary_key=True)
    hotel_id:Mapped[int] = mapped_column(ForeignKey("hotels.id"))
    title:Mapped[str] = mapped_column(String(100))
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    price:Mapped[int]
    quantity:Mapped[int]