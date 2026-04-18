from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from models.table import CreateTable
from schemas.book import SBookAdd

class BookRepository():
    @classmethod
    async def return_all(cls, session: AsyncSession):

        query = select(CreateTable)
        result = await session.execute(query)

        models = result.scalars().all()
        return models

    @classmethod
    async def return_one(cls, id: int, session: AsyncSession):

        query = select(CreateTable).where(CreateTable.id == id)
        result = await session.execute(query)

        models = result.scalar_one_or_none()
        return models

    @classmethod
    async def create(cls, book: SBookAdd, session: AsyncSession) -> CreateTable:

        new_book = CreateTable(**book.model_dump())
        session.add(new_book)

        await session.commit()
        await session.refresh(new_book)

        return new_book

    @classmethod
    async def update_one(cls, id: int, book: SBookAdd, session: AsyncSession) -> CreateTable:

        new_book = book.model_dump()

        query = update(CreateTable).where(CreateTable.id == id).values(**new_book).returning(CreateTable)
        result = await session.execute(query)
        await session.commit()

        models = result.scalar_one_or_none()
        return models

    @classmethod
    async def delete_one(cls, id: int, session: AsyncSession) -> CreateTable:

        query = delete(CreateTable).where(CreateTable.id == id)

        await session.execute(query)
        await session.commit()
