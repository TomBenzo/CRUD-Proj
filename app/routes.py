from app import app
from flask import render_template, redirect, url_for, request,session


@app.route('/')
def home():
    return render_template('index.html')



@app.route ('/Cart')
def Carts():
    return render_template ('Cart.html')


@app.route ('/signup')
def signMeUp():
    return