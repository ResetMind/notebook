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
    choices1 = [
        ("auto", "Detect automatically"),
        ("af", "Afrikaans"),
        ("sq", "Albanian"),
        ("ar", "Arab"),
        ("hy", "Armenian"),
        ("az", "Azerbaijani"),
        ("ba", "Bashkir"),
        ("eu", "Basque"),
        ("be", "Belorussian"),
        ("bn", "Bengal"),
        ("bs", "Bosnian"),
        ("bg", "Bulgarian"),
        ("my", "Burmese"),
        ("ca", "Catalan	"),
        ("zh", "Chinese"),
        ("hr", "Croatian"),
        ("cs", "Czech"),
        ("da", "Danish"),
        ("en", "English"),
        ("a", "Estonian"),
        ("fi", "Finnish"),
        ("fr", "French"),
        ("ka", "Georgian"),
        ("de", "German"),
        ("el", "Greek"),
        ("hi", "Hindi"),
        ("hu", "Hungarian"),
        ("is", "Icelandic"),
        ("id", "Indonesian"),
        ("it", "Italian"),
        ("ja", "Japanese"),
        ("jv", "Javanese"),
        ("kk", "Kazakh"),
        ("ko", "Korean"),
        ("ky", "Kyrgyz"),
        ("la", "Latin"),
        ("lv", "Latvian"),
        ("lt", "Lithuanian"),
        ("lb", "Luxembourgish"),
        ("mk", "Macedonian"),
        ("ms", "Malay"),
        ("mn", "Mongolian"),
        ("no", "Norwegian"),
        ("fa", "Persian"),
        ("pl", "Polish"),
        ("pt", "Portuguese"),
        ("ro", "Romanian"),
        ("ru", "Russian"),
        ("sr", "Serbian"),
        ("sk", "Slovak"),
        ("sl", "Slovenian"),
        ("es", "Spanish"),
        ("sv", "Swedish"),
        ("tg", "Tajik"),
        ("tt", "Tatar"),
        ("tr", "Turkish	"),
        ("udm", "Udmurt"),
        ("uk", "Ukrainian"),
        ("uz", "Uzbek"),
        ("vi", "Vietnamese")]
    choices2 = [
        ("af", "Afrikaans"),
        ("sq", "Albanian"),
        ("ar", "Arab"),
        ("hy", "Armenian"),
        ("az", "Azerbaijani"),
        ("ba", "Bashkir"),
        ("eu", "Basque"),
        ("be", "Belorussian"),
        ("bn", "Bengal"),
        ("bs", "Bosnian"),
        ("bg", "Bulgarian"),
        ("my", "Burmese"),
        ("ca", "Catalan	"),
        ("zh", "Chinese"),
        ("hr", "Croatian"),
        ("cs", "Czech"),
        ("da", "Danish"),
        ("en", "English"),
        ("a", "Estonian"),
        ("fi", "Finnish"),
        ("fr", "French"),
        ("ka", "Georgian"),
        ("de", "German"),
        ("el", "Greek"),
        ("hi", "Hindi"),
        ("hu", "Hungarian"),
        ("is", "Icelandic"),
        ("id", "Indonesian"),
        ("it", "Italian"),
        ("ja", "Japanese"),
        ("jv", "Javanese"),
        ("kk", "Kazakh"),
        ("ko", "Korean"),
        ("ky", "Kyrgyz"),
        ("la", "Latin"),
        ("lv", "Latvian"),
        ("lt", "Lithuanian"),
        ("lb", "Luxembourgish"),
        ("mk", "Macedonian"),
        ("ms", "Malay"),
        ("mn", "Mongolian"),
        ("no", "Norwegian"),
        ("fa", "Persian"),
        ("pl", "Polish"),
        ("pt", "Portuguese"),
        ("ro", "Romanian"),
        ("ru", "Russian"),
        ("sr", "Serbian"),
        ("sk", "Slovak"),
        ("sl", "Slovenian"),
        ("es", "Spanish"),
        ("sv", "Swedish"),
        ("tg", "Tajik"),
        ("tt", "Tatar"),
        ("tr", "Turkish	"),
        ("udm", "Udmurt"),
        ("uk", "Ukrainian"),
        ("uz", "Uzbek"),
        ("vi", "Vietnamese")]
    firstLang = SelectField("Original language: ", choices=choices1)
    secondLang = SelectField("Translate language: ", choices=choices2)
