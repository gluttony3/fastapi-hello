from fastapi import FastAPI , HTTPException, Path, Depends
from pydantic import BaseModel , Field
from typing import Annotated
from DB import models, schemas, crud
from DB.database import SessionLocal,engine
models.Base.metadata.create_all(bind = engine)
app = FastAPI()
app.get_session()
session = SessionLocal()
try:
    yield session
finally:
    session.close()
# ендпоінт для додавання нової книги 
@app.post("/new_book/")
def add_book(new_book: schemas.BookClient,author_id:int,session=Depends(get_session)):
   return crud.create_book(session=session,new_book=new_book,author_id=author_id)
# ендпоінт для отримання книги конкретного автора
@app.get("/book/{author_name}")
def get_books_by_id(book_id: int,session=Depends(get_session)):
    return crud.read_book(session=session,book_id=book_id)

# ендпоінт для видалення книги
@app.delete("/book/")
def delete_book(book_id:int,session=Depends(get_session)):
    return crud.delete_book(session=session,book_id=book_id)