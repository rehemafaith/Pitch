from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    pitch = TextAreaField('Your Pitch', validators=[Required()])
    # categories = SelectField(
    #     'Category',
    #     choices=[('pickup,pickup'),('interview,interview'),('product,product'),('promotion,promotion')]
    # )
    submit = SubmitField('submit')
    

class Comment(FlaskForm):
    content = TextAreaField("Add Comment")
    submit = SubmitField("Add")

class Updateprofile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')