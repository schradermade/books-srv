from fastapi import FastAPI
from .helpers import next_book_id
from .models import Book, BookRequest
from .db import BOOKS

app = FastAPI()

@app.get('/books')
async def read_all_books():
    return BOOKS

@app.get('/books/{book_id}')
async def read_book(book_id: int):
    for book in BOOKS:
        if book.id == book_id:
            return book

@app.post('/create_book')
async def create_book(book_request: BookRequest):
    book_data = book_request.model_dump()
    book_data['id'] = next_book_id(BOOKS)
    new_book = Book(**book_data)
    BOOKS.append(new_book)
    return new_book

