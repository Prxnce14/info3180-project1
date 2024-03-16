from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import StringField, TextAreaField, SelectField

from wtforms.validators import InputRequired, Email

#This is the name that will bbe displayed above your input fields

class PropertyForm(FlaskForm):
    prop_title = StringField('Property Title ', validators=[InputRequired()])
    descript = TextAreaField('Description ', validators=[InputRequired()])
    room_no = StringField('No. of Rooms', validators=[InputRequired()])
    bath_no = StringField('No. of Bathrooms', validators=[InputRequired()])
    price = StringField('Price ', validators=[InputRequired()])
    location = StringField('Location ', validators=[InputRequired()])
    photofile = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png'], 'Images only!')
    ]) 
   

class TypeForm(FlaskForm):

    prop_type = SelectField('Property Type', choices=[
        ('house', 'House'),
        ('apartment', 'Apartment'),
    ])