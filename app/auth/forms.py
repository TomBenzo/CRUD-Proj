from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, EqualTo, Email


class UserCreationForm(FlaskForm):
    email = StringField('Email',validators=[Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")
    

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[Email()])
    password = PasswordField ('Password', validators= [DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField("Log In")