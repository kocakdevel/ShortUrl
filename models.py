from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    shorturls = relationship('ShortUrl', backref='creator', lazy=True)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)


class ShortUrl(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(2083), nullable=False)
    custom_url = db.Column(db.String(120), unique=True, nullable=False)
    views = db.Column(db.Integer, default=0)
    created_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


if __name__ == '__main__':
    db.create_all()