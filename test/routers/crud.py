from fastapi import APIRouter, HTTPException, status
from schemas.book import SBookAdd, SBook
from database import SessionDep
from repository import BookRepository

router = APIRouter(
    prefix="/books",
    tags=["Книги"]
)

@router.get("", status_code=status.HTTP_200_OK)
async def get_books(session: SessionDep) -> list[SBook]:

    books = await BookRepository.return_all(session)
    return books

@router.get("/{id}")
async def get_one_book(id: int, session: SessionDep) -> SBook:

    book = await BookRepository.return_one(id, session)

    if book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Книга не найдена")

    return book

@router.post("", status_code=status.HTTP_201_CREATED)
async def create_book(book: SBookAdd, session: SessionDep) -> SBook:

    created_book = await BookRepository.create(book, session)
    return created_book

@router.put("/{id}")
async def put_book(id: int, book: SBookAdd, session: SessionDep) -> SBook:

    update_book = await BookRepository.update_one(id, book, session)

    if update_book is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Книга не найдена"
        )

    return update_book

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int, session: SessionDep):

    delete_book = await BookRepository.delete_one(id, session)