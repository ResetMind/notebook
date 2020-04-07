from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class NoteForm(FlaskForm):
    header = StringField('Header', validators=[DataRequired()], render_kw={"placeholder": "Type note's header"})
    body = TextAreaField('Body', validators=[DataRequired()], render_kw={"placeholder": "Type note"})
    submit = SubmitField('Save')


class LanguageForm(FlaskForm):
    firstLang = SelectField("Original language: ", choices=[
        ("ясно", "ясно"),
        ("пасмурно", "пасмурно"),
        ("туман", "туман"),
        ("дождь", "дождь"),
        ("снег", "снег")])
    secondLang = SelectField("Translate language: ", choices=[
        ("ясно", "ясно"),
        ("пасмурно", "пасмурно"),
        ("туман", "туман"),
        ("дождь", "дождь"),
        ("снег", "снег")])
    submit2 = SubmitField('Translate')
