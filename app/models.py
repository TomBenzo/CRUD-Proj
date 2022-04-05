from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
db = SQLAlchemy()
from flask_login import UserMixin

class Buyer(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(250), nullable=False)
    cart_item = db.relationship('Cart', backref='cart_buyer', lazy=True)
    is_admin = db.Column(db.Boolean, default=False)
   
    def __init__(self,email,password, is_admin=False):
        self.email = email
        self.password = generate_password_hash(password)
        self.is_admin = is_admin


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(800), nullable=False, unique=False)
    image = db.Column(db.String(800))
    description = db.Column(db.String(1000))
    price = db.Column(db.Float())
    cart_item = db.relationship('Cart', backref='cart_product', lazy=True)


    def __init__(self, product_name,image,description, price):
        self.product_name = product_name
        self.image = image
        self.price = price
        self.description = description


    def to_dict(self):
        return {
            "id":self.id,
            "product_name":self.product_name,
            "image":self.image,
            "price":self.price,
            "description":self.description
        }

class Cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('buyer.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    def __init__(self,user_id, product_id):
        self.user_id = user_id
        self.product_id = product_id

