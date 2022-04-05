from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin
db = SQLAlchemy()
from secrets import token_hex

# create our models based of our ERD

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, unique=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250), nullable=False)
    post = db.relationship('Post', backref = 'author', lazy=True)
    cart_item = db.relationship('Cart', backref='cart_user', lazy=True)
    apitoken = db.Column(db.String, default = None, nullable=True)





    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
        self.apitoken = token_hex(16)
    

    def to_dict(self):
        return{
            'id':self.id,
            'email':self.email,
            'username':self.username,
            'token':self.apitoken

        }
        


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False, unique=False)
    image = db.Column(db.String(300))
    caption = db.Column(db.String(300))
    date_created = db.Column(db.DateTime, nullable=False, default=datetime.utcnow())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)


    def __init__(self,title,image,caption,user_id):
        self.title = title
        self.image = image
        self.caption = caption
        self.user_id = user_id
    
    def to_dict(self):
        return {
            'id':self.id,
            'title': self.title,
            'image': self.image,
            'caption': self.caption,
            'date_created': self.date_created,
            'user_id':self.user_id
        }


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(200), nullable=False, unique=False)
    image = db.Column(db.String(300))
    description = db.Column(db.String(300))
    price = db.Column(db.Float())
    cart_item = db.relationship('Cart', backref='cart_product', lazy=True)


    def __init__(self, product_name,image,description, price):
        self.product_name = product_name
        self.image = image
        self.price = price
        self.description = description


class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)

class Pokedex(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False, unique=False)
    image = db.Column(db.String(300))
    abilities = db.Column(db.String(300))

    def __init__(self, name, image, abilities):
        self.name = name
        self.image = image 
        self.abilities = abilities