import pytest
from app import create_app, db
from config import Config
from app.models import Author, Book

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite://'

@pytest.fixture
def client():
    app = create_app(TestConfig)

    app_context = app.app_context()

    app_context.push()

    db.create_all()

    with app.test_client() as client:
        yield client

    db.session.remove()
    db.drop_all()
    app_context.pop()


@pytest.fixture
def sample_author(client):
    author = Author(name='NK Jemisin')
    db.session.add(author)
    db.session.commit()
    return author

@pytest.fixture
def sample_book(sample_author):
    book = Book(name='The Fifth Season', author=sample_author)
    db.session.add(book)
    db.session.commit()
    return book

@pytest.fixture
def solo_book(client):
    book = Book(name='Good Omens')
    db.session.add(book)
    db.session.commit()
    return book