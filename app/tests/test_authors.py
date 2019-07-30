import json
import pytest

def test_get_no_authors(client):
    response = client.get('/authors')

    assert response.status_code == 200
    assert json.loads(response.data.decode()) == []

def test_create_author(client):
    response = client.post('/authors', data={'name':'NK Jemisin'})

    assert response.status_code == 200

def test_sample_author(sample_author):
    assert sample_author.id == 1
    assert sample_author.name == 'NK Jemisin'

def test_create_author_and_check(client):
    client.post('/authors', data={'name':'NK Jemisin'})
    response = client.get('/authors')
    authors = json.loads(response.data.decode())

    assert len(authors) == 1
    assert authors[0]['name'] == 'NK Jemisin'

def test_create_author_and_fetch(client, sample_author):
    response = client.get(f'/authors/{sample_author.id}')

    assert response.status_code == 200

    author_dict = json.loads(response.data.decode())
    assert author_dict['name'] == 'NK Jemisin'

def test_update_author(client, sample_author):
    response = client.put(f'/authors/{sample_author.id}', data={'name':'Not Jemisin'})
    assert response.status_code == 200

    assert json.loads(response.data.decode()) == sample_author.id
    
    response = client.get(f'/authors/{sample_author.id}')

    author_dict = json.loads(response.data.decode())
    assert author_dict['name'] == 'Not Jemisin'

def test_get_author_books(client, sample_book):
    response = client.get(f'/authors/{sample_book.id}')

    author_dict = json.loads(response.data.decode())

    assert author_dict['books'][0]['name'] == 'The Fifth Season'

def test_delete_author(client, sample_author):
    response = client.get(f'/authors/{sample_author.id}')
    assert response.status_code == 200

def test_get_author_by_name(client, sample_author):
    response = client.get('/authors/NK Jemisin')
    assert response.status_code == 200

    author_dict = json.loads(response.data.decode())

    assert author_dict['name'] == 'NK Jemisin'