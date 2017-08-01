from wtforms.form import Form
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired


class RegisterForm(Form):
    login = StringField('login', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])
    name = StringField('name', validators=[DataRequired()])
    email = StringField('email', validators=[DataRequired()])
