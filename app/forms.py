from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, BooleanField, PasswordField, IntegerField
from flask import flash
from app.models import Contact # User
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError


# class TitleForm(FlaskForm):
#     title = StringField('Title: ', validators=[DataRequired()])
#     submit = SubmitField('Submit')

# *** contact ***
class ContactForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    submit = SubmitField('Submit')

# *** login ***
class LoginForm(FlaskForm):
    username = StringField('Username:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

# *** register ***
class RegisterForm(FlaskForm):
    first_name = StringField('First Name:', validators=[DataRequired()])
    last_name = StringField('Last Name:', validators=[DataRequired()])
    username = StringField('Username:', validators=[DataRequired()])
    email = StringField('E-mail:', validators=[DataRequired(), Email()])
    age = IntegerField('Age:')
    bio = StringField('Bio:')
    url = StringField('Profile Pic URL:')
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Re-type Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

# *** validation method ***
    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            flash('Sorry but those credentials are already in use.')
            raise ValidationError('Username already taken.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            flash('Sorry but those credentials are already in use.')
            raise ValidationError('E-mail already taken.')
