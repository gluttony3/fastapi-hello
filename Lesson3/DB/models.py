from sqlalchemy import Column, Integer, String
from .database import Base

# модель таблиці книг у базі даних
class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author_name = Column(String, index=True, nullable=False)
    pages = Column(Integer, nullable=False)
