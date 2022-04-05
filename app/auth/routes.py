from flask import Blueprint, redirect, render_template, request, url_for
from .forms import UserCreationForm, LoginForm
from app.models import Buyer
from app.models import db
from werkzeug.security import check_password_hash
from flask_login import login_user, logout_user, login_required, current_user

auth = Blueprint('auth',__name__, template_folder='auth_templates')

@auth.route('/login',methods = ["GET","POST"])
def logMeIn():
    form = LoginForm()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if request.method == "POST":
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember_me = form.remember_me.data

            user = Buyer.query.filter_by(email=email).first()

            if Buyer is None or check_password_hash(user.password, password):
                redirect(url_for('auth.logMeIn'))

            login_user(user,remember = remember_me)
            return redirect(url_for('home'))

            
    return render_template('login.html', form = form )

@auth.route('/signup',methods=["GET", "POST"])
def signMeUp():
    form = UserCreationForm()
    if request.method == 'POST':
        print('valid')
        if form.validate_on_submit():
            print('valid')
            email = form.email.data
            password = form.password.data

            user = Buyer(email,password)

            db.session.add(user)
        
            db.session.commit()
            return redirect(url_for('auth.logMeIn'))
    return render_template('signup.html',form=form)


@auth.route('/logout')
@login_required
def logMeOut():
    logout_user()
    return redirect(url_for('auth.logMeIn'))
