from . import db
from datetime import datetime
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    contact_num = db.Column(db.Integer, nullable=False)
    address = db.Column(db.String(255), nullable=False)

class Listing(db.Model):
    __tablename__ = 'listings'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    size = db.Column(db.String(50), nullable=False)
    origin = db.Column(db.String(200), nullable=False)
    colour = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    startbid = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(400), nullable=False)
    upost = db.Column(db.String(30), db.ForeignKey('users.name'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    status = db.Column(db.Boolean, default=True, nullable=False)

    def __repr__(self): #string print method
        return "<Name: {}>".format(self.name)

class Bidding(db.Model):
    __tablename__ = 'bids'
    id = db.Column(db.Integer, primary_key=True)
    sub_bid = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.now())
    usr_id = db.Column(db.String(100), db.ForeignKey('users.id'), nullable=False)
    lis_id = db.Column(db.Integer, db.ForeignKey('listings.id'), nullable=False)

    def __repr__(self): #string print method
        return "<Bid: {}>".format(self.name)

class Watchlist(db.Model):
    __tablename__ = 'watching'
    id = db.Column(db.Integer, primary_key=True)
    added_at = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    list_id = db.Column(db.Integer, db.ForeignKey('listings.id'), nullable=False)
    