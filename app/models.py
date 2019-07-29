from app import db

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    books = db.relationship("Books", backref="band", lazy=True)

    def to_dict(self):
        return {'id':self.id, 'name':self.name}

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), unique=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author_id'), nullabe=True)

    def to_dict(self):
        return {'id':self.id, 'name':self.name}