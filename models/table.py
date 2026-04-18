from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean
from database import Model

class CreateTable(Model):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, init=False)
    title: Mapped[str] = mapped_column(String)
    author: Mapped[str] = mapped_column(String)
    year: Mapped[int] = mapped_column(Integer)
    pages: Mapped[int] = mapped_column(Integer)
    is_read: Mapped[bool] = mapped_column(Boolean)