from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.form import Form


class PostForm(Form):
    post = StringField('post', validators=[DataRequired()])

