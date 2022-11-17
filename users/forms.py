from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, EmailField
from wtforms.validators import DataRequired, ValidationError
import re


def forbidden_chars(form, field):
    excluded_char = "&<>%"

    for char in field.data:
        if char in excluded_char:
            raise ValidationError(f"Char {char} is not allowed")


def phone_num_check(self, data_field):
    p = re.compile(r'(\d{4}-\d{3}-\d{4}$)')
    if not p.match(data_field.data):
        raise ValidationError("Phone number must be in the form XXXX-XXX-XXXX")


class RegisterForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    firstname = StringField(validators=[DataRequired(), forbidden_chars])
    lastname = StringField(validators=[DataRequired(), forbidden_chars])
    phone = StringField(validators=[DataRequired(), phone_num_check])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])
    submit = SubmitField(validators=[DataRequired()])
