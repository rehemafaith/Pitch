from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SelectField,SubmitField
from wtforms.validators import Required

class PitchForm(FlaskForm):

    title = StringField('Pitch title',validators=[Required()])
    pitch = TextAreaField('Category', validators=[Required()])
    category = SelectField(
        'Category',
        choices=[('pickup,pickup'),('interview,interview'),('product,product'),('promotion,promotion')]
    )
    

class Comment(FlaskForm):
    content = TextAreaField("Add Comment")
    submit = SubmitField("Add")

class Updateprofile(FlaskForm):
    bio = TextAreaField('Tell us about you.',validators = [Required()])
    submit = SubmitField('Submit')