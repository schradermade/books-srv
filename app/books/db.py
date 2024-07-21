from .models import Book
from datetime import datetime

BOOKS = [
    Book(id=1, title='Computer Science Pro', author='Nathan', description='Great book for CS', rating=5, published_date=str(datetime(2024, 1, 5))),
    Book(id=2, title='Math Pro', author='Nathan', description='Great book for math', rating=4, published_date=str(datetime(2024, 1, 5))),
    Book(id=3, title='Physics 101', author='Nathan', description='Great book for physics', rating=3, published_date=str(datetime(2024, 3, 10))),
    Book(id=4, title='Data Science 101', author='Nathan', description='Great book for DS', rating=2, published_date=str(datetime(2024, 3, 10))),
    Book(id=5, title='Generative AI for Pros', author='Nathan', description='Great book for AI', rating=1, published_date=str(datetime(2024, 5, 30))),
]