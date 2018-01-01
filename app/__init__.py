from flask import Flask         #import Flask
from app.models import db
from .views.search import search    # search blueprint
from .views.steam import init_steam_connection

def create_app():
    app = Flask(__name__)                   #flask constructor takes name of current module as argument

    #Used for the setting of the current users session
    app.config.update(
        DEBUG = True,
        SECRET_KEY = 'secret_xxx'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db/database.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    app.register_blueprint(search)

    init_steam_connection()


    return app
