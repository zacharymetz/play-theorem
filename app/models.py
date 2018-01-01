from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


#example ones
class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Genre(db.Model):
    __tablename__ = 'genre'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Type(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

class Platform(db.Model):
    __tablename__ = 'platform'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

#for the app we need a many to many table
class AppGenre(db.Model):
    __tablename__ = 'app_genre'
    id = db.Column(db.Integer, primary_key=True)
    app = db.Column(db.Integer)
    genre = db.Column(db.Integer)

class AppCategroy(db.Model):
    __tablename__ = 'app_categroy'
    id = db.Column(db.Integer, primary_key=True)
    app = db.Column(db.Integer)
    categroy = db.Column(db.Integer)
class AppPlatform(db.Model):
    __tablename__ = 'app_platform'
    id = db.Column(db.Integer, primary_key=True)
    app = db.Column(db.Integer)
    platform = db.Column(db.Integer)

class App(db.Model):
    __tablename__ = 'app'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    app_type = db.Column(db.String)
    header_image = db.Column(db.String)
