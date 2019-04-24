from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import Required,Email,EqualTo
from ..models import User 

class PitchForm(FlaskForm):

  title = StringField('Pitch title',validators=[Required()])
  review = TextAreaField('Pitch',validators=[Required()])
  submit = SubmitField('Submit')