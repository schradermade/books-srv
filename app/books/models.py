from typing import Optional
from pydantic import BaseModel, Field

class Book(BaseModel):
    id: int
    title: str
    author: str
    description: str
    rating: int

class BookRequest(BaseModel):
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
              "rating": 5
          }
      }
    }