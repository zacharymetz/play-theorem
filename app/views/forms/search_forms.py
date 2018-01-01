from flask_wtf import FlaskForm, Form
from wtforms import  TextField, SubmitField, validators
from wtforms.validators import DataRequired


class SteamidForm(Form):
    steamid = TextField('steamid', [validators.DataRequired()])
    submit = SubmitField("Start Searching")
