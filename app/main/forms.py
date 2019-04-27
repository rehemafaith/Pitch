from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Pitch', validators=[Required()])
    submit = SubmitField("category",
        choices=[("pick-up", "pick-up"),("interview","interview"),("product","product"),("promotion","promotion")],validators = [Required()])

class Comment(FlaskForm):
    content = TextAreaField("Add Comment")
    submit = SubmitField("Add")

class Updateprofile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')