from flask import Flask
from config import Config

from .auth.routes import auth
from .shop.routes import shop

from .models import Buyer, db
from flask_migrate import Migrate

from flask_login import LoginManager
from flask_cors import CORS

app = Flask(__name__)
login = LoginManager()
CORS(app)

@login.user_loader
def load_user(user_id):
    return Buyer.query.get(user_id)

app.register_blueprint(auth)
app.register_blueprint(shop)

app.config.from_object(Config)

db.init_app(app)
login.init_app(app)

migrate = Migrate(app,db)

from . import routes
from . import models

