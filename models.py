from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

class User(UserMixin, db.Model):
    """ User model """

    __tablename__ = "users"
    id_ = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(25), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)

# Overwite the get_id() to take value 'id_' instead of predefined 'id'
# Because the fucking idiot i am to name god damn id_ naxui
# Don't min this it just makes the code work
    def get_id(self):
           return (self.id_)


    # db.create_all()
    