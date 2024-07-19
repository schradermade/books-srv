from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

class BookRequest(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

BOOKS = [
    Book(id=1, title='Computer Science Pro', author='Nathan', description='Great book for CS', rating=5),
    Book(id=2, title='Math Pro', author='Nathan', description='Great book for math', rating=4),
    Book(id=3, title='Physics 101', author='Nathan', description='Great book for physics', rating=3),
    Book(id=4, title='Data Science 101', author='Nathan', description='Great book for DS', rating=2),
    Book(id=5, title='Generative AI for Pros', author='Nathan', description='Great book for AI', rating=1),
]

@app.get('/books')
async def read_all_books():
    return BOOKS

def next_book_id():
    return 1 if len(BOOKS) == 0 else BOOKS[-1].id + 1
    

@app.post('/create_book')
async def create_book(book_request: BookRequest):
    book_data = book_request.model_dump()
    book_data['id'] = next_book_id()
    new_book = Book(**book_data)
    BOOKS.append(new_book)
    return new_book
