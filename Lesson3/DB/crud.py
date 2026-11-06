from .import models
from sqlalchemy.orm import Session
from .import schemas
# функція для читання всіх книг
def read_books(session: Session):
    return session.query(Book).all()
# функція для конкретної книги за id
def read_books(session: Session,book_id: id):
    return session.query(Book).filter(Book.id == book_id).first()
# функція для читання всіх авторів
def read_authors(session: Session):
    return session.query(Author).all()
# функція для читання конкретного автора по id
def read_author(session: Session, author_id: id):
    return session.query(Author).filter(Author.id == author_id).first()
# функція для створення нового автора
def create_author(session:Session,new_author: schemas.AuthorClient):
    author_db = models.Author(name = new_author.name)
    session.add(author_db)
    session.commit()
    session.refresh(author_db)
    return author_db

# функція для створення нової книги
def create_book(session: Session, new_book: schemas.BookClient,author_id: int):
    book_db = models.Book(title=new_book.title,pages=new_book.pages,author_id=author_id)
    session.add(book_db)
    session.commit()
    session.refresh(book_db)
    return book_db

# функція для видалення книги 
def delete_book(session:Session,book_id:int):
    book_db = session.query(models.Book).get(models.Book.id == book_id)
    if book_db is None:
        return {"message": "Book was not found"}
    session.delete(book_db)
    session.commit()
    return {"message": "Book was deleted successfully"}