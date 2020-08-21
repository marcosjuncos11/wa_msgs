from src.config.config import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256))
    email = db.Column(db.String(256), index=True, unique=True)  # index => should not be duplicate
    password = db.Column(db.String(256))
    posts = db.relationship('Post', backref='author')

    def __repr__(self):
        return '<User %r>' % self.email