from .import models
from sqlalchemy.orm import Session

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