from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):

    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=4, max=16)
        ]
    )

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8,max=16)
        ]
    )

    confirm_password = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            EqualTo('password')
        ]
    )

    submit = SubmitField(
        'Sign Up'
    )

class LoginForm(FlaskForm):

    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )

    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=8,max=16)
        ]
    )

    remember_me = BooleanField(
        'Remember Me'
    )

    submit = SubmitField(
        'Login'
    )