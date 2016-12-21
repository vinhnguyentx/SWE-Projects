from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
import flask_restful

app = Flask(__name__)
api = flask_restful.Api(app)

class GodsHandler(flask_restful.Resource):
  def get(self):
    gods = God.query.all()
    
    gods_response = {}
    for god in gods:
      god_data = {
        'name': god.name,
        'romanname': god.romanname,
        'power': god.power,
        'symbol': god.symbol,
        'father': god.father,
        'mother': god.mother,
      }
      gods_response[god.name] = god_data

    return jsonify(gods_response)

api.add_resource(GodsHandler, '/api/gods/') 

class HeroesHandler(flask_restful.Resource):
  def get(self):
    heroes = Hero.query.all()
    
    heroes_response = {}
    for hero in heroes:
      hero_data = {
        'name': hero.name,
        'herotype': hero.herotype,
        'power': hero.power,
        'father': hero.father,
        'mother': hero.mother,
        'home': hero.home,
      }
      heroes_response[hero.name] = hero_data

    return jsonify(heroes_response)

api.add_resource(HeroesHandler, '/api/heroes/') 

class MythsHandler(flask_restful.Resource):
  def get(self):
    myths = Myth.query.all()
    
    myths_response = {}
    for myth in myths:
      myth_data = {
        'name': myth.name,
        'description': myth.description,
        'gods': myth.gods,
        'non-gods': myth.nongods,
        'place': myth.place,
        'theme': myth.theme,
      }
      myths_response[myth.name] = myth_data

    return jsonify(myths_response)

api.add_resource(MythsHandler, '/api/myths/') 

class LocationsHandler(flask_restful.Resource):
  def get(self):
    locations = Location.query.all()
    
    locations_response = {}
    for location in locations:
      location_data = {
        'name': location.name,
        'alternate_name': location.altname,
        'myth': location.myth,
        'type': location.locationtype,
        'gods': location.gods,
      }
      locations_response[location.name] = location_data

    return jsonify(locations_response)

api.add_resource(LocationsHandler, '/api/locations/') 