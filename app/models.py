from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    books = db.relationship('Book', backref='author', lazy=True)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'books':[book.to_dict() for book in self.books]
         }

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'), nullable=True)

    def to_dict(self):
        return {'id':self.id, 'name':self.name}

