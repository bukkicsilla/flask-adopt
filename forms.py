from flask_wtf  import FlaskForm
from wtforms import StringField, IntegerField, SelectField, TextAreaField, BooleanField
from wtforms.validators import InputRequired, Optional, URL, NumberRange, Length

class AddPetForm(FlaskForm):
    """Form for adding pets."""

    choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")]
    name = StringField("Pet Name", validators=[InputRequired(message="Pet name cannot be blank!")])
    species = SelectField("Species", choices=choices)
    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    age = IntegerField("Age", validators=[Optional(), NumberRange(min=0, max=30)])
    notes = TextAreaField("Some comments", validators=[Optional(), Length(min=10)])

class EditPetForm(FlaskForm):
    """Form for editing an existing pet."""

    photo_url = StringField("Photo URL", validators=[Optional(), URL()])
    notes = TextAreaField("Some comments", validators=[Optional(), Length(min=10)])
    available = BooleanField("Is your pet available?")