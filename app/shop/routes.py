from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import current_user, login_required


shop = Blueprint('shop', __name__, template_folder='shop_templates')

from app.models import db, Product


