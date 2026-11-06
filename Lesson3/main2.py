from fastapi import FastAPI , HTTPException, Path
from pydantic import BaseModel , Field
from typing import Annotated
from DB import models
from DB.database import SessionLocal,engine
models.Base.metadata.create_all(bind = engine)
app = FastAPI()
library = {}
#pydentic-модель книги
class Book(BaseModel):
    title:str
    #author_name:str = Field(min_length=3, max_length=30)
    author_name: Annotated[str,Field(min_length=3, max_length=30)]
    pages:Annotated[int,Field(ge=10)]
#ендпоінт для додавання нової книги 
@app.post("/new_book/")
def add_book(new_book: Book):
    if new_book.author_name not in library:
        library[new_book.author_name] = []
    library[new_book.author_name].append(new_book)
    return {"Message: Book added succesfully"}
# ендпоінт для отримання книги конкретного автора
@app.get("/book/{author_name}")
def get_books_by_author(author_name: Annotated[str,Path(min_length=3,max_length=30)]):
    if author_name not in library:
        raise HTTPException(status_code=404,detail="Author not found")
    return {"Author": author_name, "Books": library[author_name]}
# ендпоінт для видалення книги
@app.delete("/book/")
def delete_book(title,author_name):
    if author_name not in library:
        raise HTTPException(status_code=404,detail="Author not found")
    for exsisting_book in library[author_name]:
        if exsisting_book.title == title:
            library[author_name].remove(exsisting_book)
            return {"Message: Book not found"}
    raise HTTPException(status_code=404,detail="Book not found")