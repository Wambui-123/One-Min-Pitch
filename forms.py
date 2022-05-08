from flask import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, EmailField

class SignUpForm(FlaskForm):
    username = StringField('Username')
    text = StringField('Text')
    password = StringField('Password')
    email = StringField('Email')
    submit = SubmitField('Sign Up')
    

    