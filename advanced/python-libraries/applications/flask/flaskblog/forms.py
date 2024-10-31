from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from flaskblog.models import User
from flask_login import current_user

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

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already taken! Please choose another one')
        
    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('Email already taken! Please choose another one')

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

class UpdateAccount(FlaskForm):

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

    picture = FileField(
        'Update Profile Picture',
        validators=[
            FileAllowed(['jpg', 'jpeg', 'png'])
        ]
    )

    submit = SubmitField(
        'Update'
    )

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('Username already taken! Please choose another one')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('Email already taken! Please choose another one')
            
class PostForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])
    submit = SubmitField('Post')

class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if not user:
            raise ValidationError("If an account with this email address exists, a password reset message will be sent shortly.")
        
class ResetPasswordForm(FlaskForm):

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

    submit = SubmitField('Reset Password')