from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length, EqualTo 

class RegistrationForm(FlaskForm):
    """ Registration Form """

    username = StringField('username_label',
        validators=[InputRequired(message="Username field required"),
        Length(min=4, max=25,
        message="Username must be between 4 to 25 characters")])
    password = PasswordField('password_label',
        validators=[InputRequired(message="Password field required"),
        Length(min=6, max=25,
        message='Password must be between 6 to 25 characters')])
    confirm_psw = PasswordField('confirm_psw_label',
        validators=[InputRequired(message="Password field required"),
        EqualTo('password',
        message="Passwords must match")])
    submit_button = SubmitField('Create') 