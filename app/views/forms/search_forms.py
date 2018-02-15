from flask_wtf import FlaskForm, Form
from wtforms import  TextField, SubmitField, validators, HiddenField
from wtforms.validators import DataRequired


class SteamidForm(Form):

    steamid = TextField('steamid', [validators.DataRequired()])
    
    submit = SubmitField("Start Searching")


class FilterForm(Form):

    gaming_mood = HiddenField()

    genre_casual = HiddenField()
    genre_indie = HiddenField()
    genre_adventure = HiddenField()
    genre_action = HiddenField()
    genre_strategy = HiddenField()
    genre_rpg = HiddenField()
    genre_racing = HiddenField()
    genre_sports = HiddenField()
    genre_simulation = HiddenField()

    category_singleplayer = HiddenField()
    category_multiplayer = HiddenField()
    category_coop = HiddenField()
    category_local_coop = HiddenField()
    category_controller = HiddenField()
    category_splitscreen = HiddenField()
    category_mods = HiddenField()

    submit = SubmitField("Start Searching")
