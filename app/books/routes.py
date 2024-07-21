from fastapi import FastAPI
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
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

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
async def read_book_by_rating(book_rating: int):
    books_to_return = []

    for book in BOOKS:
        if book.rating == book_rating:
            books_to_return.append(book)

    return books_to_return

