from . import db

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    book_title = db.Column(db.String, nullable=False)
    book_description = db.Column(db.String)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))

class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String, nullable=False)

    books = db.relationship('Book', backref='author', lazy=True)
