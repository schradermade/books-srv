from datetime import datetime
from fastapi import FastAPI, Path, Query, HTTPException
from .helpers import next_book_id
from .models import Book, BookRequest
from .db import BOOKS

app = FastAPI()

# All books
@app.get('/books')
async def read_all_books():
    return BOOKS

# Book by id
@app.get('/books/{book_id}')
async def read_book(book_id: int = Path(gt=0)):
    for book in BOOKS:
        if book.id == book_id:
            return book
    raise HTTPException(status_code=404, detail='Item not found')

# books by publish_date
@app.get('/books/publish/')
async def read_books_by_publish_date(
    published_date: datetime = Query(lt=datetime.now())):
    books_to_return = []
    for book in BOOKS:
        if book.published_date == published_date:
            books_to_return.append(book)
    return books_to_return

# new book
@app.post('/create_book')
async def create_book(book_request: BookRequest):
    book_data = book_request.model_dump()
    book_data['id'] = next_book_id(BOOKS)
    new_book = Book(**book_data)
    BOOKS.append(new_book)
    return new_book

# books by rating
@app.get('/books/')
async def read_book_by_rating(book_rating: int = Query(gt=0, lt=6)):
    books_to_return = []

    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)

    return books_to_return

# update a book
@app.put('/book/update_book')
async def update_book(book: BookRequest):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book.id:
            BOOKS[i] = book
            book_changed = True
    if not book_changed:
        raise HTTPException(status_code=404, detail='Update unsuccessful, book not found.')

# delete a book
@app.delete('/books/{book_id}')
async def delete_book(book_id: int = Path(gt=0)):
    book_changed = False
    for i in range(len(BOOKS)):
        if BOOKS[i].id == book_id:
            deleted_book = BOOKS.pop(i)
            return deleted_book
    if not book_changed:
        raise HTTPException(status_code=404, detail='Update unsuccessful, book not found.')