import json

def test_get_no_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert json.loads(response.data.decode()) == []

def test_sample_book_fixture(sample_book):
    assert sample_book.id == 1
    assert sample_book.name == 'The Fifth Season'

def test_solo_book_fixture(solo_book):
    assert solo_book.id == 1
    assert solo_book.name == 'Good Omens'

def test_create_book_with_author(client, sample_author):
    book_info = {'name':'The Fifth Season', 'author':'NK Jemisin'}
    response = client.post('/books', data=book_info)
    assert response.status_code == 200

def test_create_solo_book(client):
    book_info = {'name':'Good Omens'}
    response = client.post('/books', data=book_info)    
    assert response.status_code == 200

    response = client.get('/books')
    books = json.loads(response.data.decode())

    assert len(books) == 1
    assert books[0]['name'] == 'Good Omens'
    assert books[0].get('author') is None

def test_get_one_book(client, sample_book):
    response = client.get(f'/books/{sample_book.id}')
    books_dict = json.loads(response.data.decode())
    assert books_dict['name'] == 'The Fifth Season'


