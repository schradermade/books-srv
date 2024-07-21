from typing import Optional
from pydantic import BaseModel, Field, field_validator
from datetime import datetime

class BaseBook(BaseModel):
    published_date: datetime = Field(default_factory=datetime.now)

    @field_validator('published_date')
    def check_published_date(cls, value):
        if value >= datetime.now():
            raise ValueError('Published date must be in the past')
        return value

class Book(BaseBook):
    id: int
    title: str
    author: str
    description: str
    rating: int

class BookRequest(BaseBook):
    id: Optional[int] = Field(description='ID is not needed on create', default=None)
    title: str = Field(min_length=3)
    author: str = Field(min_length=1)
    description: str = Field(min_length=1, max_length=100)
    rating: int = Field(gt=0, lt=6)

    model_config = {
      "json_schema_extra": {
          "example": {
              "title": "A new book",
              "author": "Nathan S",
              "description": "A new description of a book",
              "rating": 5,
              "published_date": str(datetime.now().date())
          }
      }
    }