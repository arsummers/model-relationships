from app import db
from app.models import Author, Book

def test_author(client):
    author = Author(name='Terry Pratchett')
    db.session.add(author)
    db.session.commit()
    assert Author.query.first().name == 'Terry Pratchett'

def test_book(client):
    book = Book(name='Thud')
    db.session.add(book)
    db.session.commit()
    assert Book.query.first().name == 'Thud'

def test_book_by_author(client):
    author = Author(name='Neil Gaiman')
    book = Book(name='Sandman', author=author)
    db.session.add(book)
    db.session.commit()

    assert Author.query.first().name == 'Neil Gaiman'
    assert Book.query.first().name == 'Sandman'

    books_by_author = Author.query.first().books

    assert books_by_author[0].name == 'Sandman'
    assert books_by_author[0].author.name == 'Neil Gaiman'