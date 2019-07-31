from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app(ConfigClass):
    app = Flask(__name__)
    app.config.from_object(ConfigClass)
    db.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
##################
######AUTHOR CRUD######
#####################

        @app.route('/authors', methods=['GET'])
        def all_authors():
            authors = [author.to_dict() for author in Author.query.all()]
            return jsonify(authors)
        
        @app.route('/authors/<int:id>')
        def one_author(id):
            author = Author.query.get(id)
            return jsonify(author.to_dict())

        @app.route('/authors', methods=['POST'])
        def create_author():
            author_info = request.json or request.form
            author = Author(name=author_info.get('name'))

            db.session.add(author)
            db.session.commit()

            return jsonify(author.to_dict())

        @app.route('/authors/<int:id>', methods=['PUT'])
        def update_author(id):
            author_info = request.json or request.form
            author_id = Author.query.filter_by(id=id).update(author_info)
            db.session.commit()
            return jsonify(author_id)


        @app.route('/authors/<int:id>', methods=['DELETE'])
        def delete_author(id):
            author = Author.query.get(id)
            db.session.delete(author)
            db.session.commit()
            return jsonify(id)

        @app.route('/authors/<string:name>', methods=['GET'])
        def get_author_by_name(name):
            
            author = Author.query.filter_by(name=name).first()
            return jsonify(author.to_dict)

 ######################       
########## BOOKS CRUD ######
###########################

        @app.route('/books', methods=['GET'])
        def all_books():
            books = [book.to_dict() for book in Book.query.all()]
            return jsonify(books)

        @app.route('/books/<int:id>')
        def one_book(id):
            book = Book.query.get(id)
            return jsonify(book.to_dict())

        @app.route('/books', methods=['POST'])
        def create_book():
            book_info = request.json or request.form
            book = Book(
                name=book_info.get('name'),
                author_id=book_info.get('author'))

            db.session.add(book)
            db.session.commit()

            return jsonify(book.to_dict())

        @app.route('/books/<int:id>', methods=['PUT'])
        def update_book(id):
            book_info = request.json or request.form
            book_id = Book.query.filter_by(id=id).update(book_info)
            db.session.commit()
            return jsonify(book_id)

        @app.route('/books/<int:id>', methods=['DELETE'])
        def delete_book(id):
            book = Book.query.get(id)
            db.session.delete(book)
            db.session.commit()
            return jsonify(id)
        

        @app.route('/authors/<int:id>/books')
        def get_books_by_author(id):
            books = [book.to_dict() for book in Author.query.get(id).books]
            return jsonify(books)
        return app
        
from app.models import Author, Book