from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, ValidationError, Length, EqualTo
import re


def forbidden_chars(form, field):
    excluded_char = "&<>%"

    for char in field.data:
        if char in excluded_char:
            raise ValidationError(f"Char {char} is not allowed")


# regex validator for phone number
def phone_num_check(self, data_field):
    p = re.compile(r'(\d{4}-\d{3}-\d{4}$)')
    if not p.match(data_field.data):
        raise ValidationError("Phone number must be in the form XXXX-XXX-XXXX")


# regex validator for the password field
def password_validation(self, data_field):
    p = re.compile(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])')
    if not p.match(data_field.data):
        raise ValidationError("Password must contain at least 1 lowercase word character, 1 uppercase word character, "
                              "and 1 special character (non-word character)")


class RegisterForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    firstname = StringField(validators=[DataRequired(), forbidden_chars])
    lastname = StringField(validators=[DataRequired(), forbidden_chars])
    phone = StringField(validators=[DataRequired(), phone_num_check])
    password = PasswordField(validators=[DataRequired(), Length(min=6, max=12), password_validation])
    confirm_password = PasswordField(validators=[DataRequired(), EqualTo("password", message="Passwords do not match")])
    submit = SubmitField(validators=[DataRequired()])
