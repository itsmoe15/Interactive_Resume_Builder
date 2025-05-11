from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
import bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))

def create_database():
    with app.app_context():
        db.drop_all()  # This will delete all existing tables
        db.create_all()  # This will create new tables
        print("Database created successfully!")

if __name__ == '__main__':
    create_database() 