"""
    SQLAlchemy models for the Postgres database.
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres@greekmythology.me:5432/greekmyths'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Url(db.Model):
    """
    Information about a god in Greek mythology.
    """

    __tablename__ = 'urls'

    name = db.Column(db.String, primary_key=True)
    url  = db.Column(db.String)

    def __init__(self, name, url):
        self.name = name
        self.url = url

    def __repr__(self):
        return '<Url %r>' % self.name

class God(db.Model):
    """
    Information about a god in Greek mythology.
    """

    __tablename__ = 'gods'

    name = db.Column(db.String, primary_key=True)
    romanname = db.Column(db.String)
    power = db.Column(db.String)
    symbol = db.Column(db.String)
    father = db.Column(db.String, db.ForeignKey('god.name'), nullable=False)
    mother = db.Column(db.String, db.ForeignKey('god.name'), nullable=False)

    def __repr__(self):
        return '<God %r>' % self.name


class Hero(db.Model):
    """
    Information about a hero in Greek mythology.
    """

    __tablename__ = 'heroes'

    name = db.Column(db.String, primary_key=True, nullable=False)
    herotype = db.Column(db.String, nullable=False)
    father = db.Column(db.String, db.ForeignKey('god.name'), nullable=False)
    mother = db.Column(db.String, db.ForeignKey('god.name'), nullable=False)
    power = db.Column(db.String, nullable=False)
    home = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Hero %r>' % self.name


class Location(db.Model):
    """
    Information about a location from Greek mythology.
    """

    __tablename__ = 'locations'

    name = db.Column(db.String, primary_key=True, nullable=False)
    altname = db.Column(db.String, nullable=False)
    myth = db.Column(db.String, db.ForeignKey('myth.name'), nullable=False)
    locationtype = db.Column(db.String, nullable=False)
    gods = db.Column(db.String, db.ForeignKey('god.name'), nullable=False)

    def __repr__(self):
        return '<Location %r>' % self.name

class Myth(db.Model):
    """
    Information about a myth from Greek mythology.
    """

    __tablename__ = 'myths'

    name = db.Column(db.String, primary_key=True, nullable=False)
    description = db.Column(db.String, nullable=False)
    gods = db.Column(db.String, db.ForeignKey('god.name'), nullable=False)
    nongods = db.Column(db.String, nullable=False)
    place = db.Column(db.String, nullable=False)
    theme = db.Column(db.String, nullable=False)

    def __repr__(self):
        return '<Myth %r>' % self.name

if __name__ == "__main__":
    print(Url.query.all())
    print(God.query.all())
    print(Hero.query.all())
    print(Location.query.all())
    print(Myth.query.all())