from pydantic import BaseModel, Field

# Модель для валідації Автора
class AuthorClient(BaseModel):
    name: str = Field(max_length=100)
    
# Модель для валідації Книг
class BookClient(BaseModel):
    title: str = Field(max_length=100)
    pages: int = Field(gt=10)
