"""
    Backend for serving files.
"""

from flask import Flask, send_from_directory, send_file, escape, Markup, render_template, abort, request, jsonify
import re
import os
import json
import flask_restful
from app.models import *
from flask_sqlalchemy import SQLAlchemy
import subprocess

app = Flask(__name__)

api = flask_restful.Api(app)

# API Function to grab url's from the db
class UrlHandler(flask_restful.Resource):
  def get(self, url_name):
    url = Url.query.filter_by(name=url_name)
    url = url.first()

    if url:
      url_response = url.url

    return url_response

api.add_resource(UrlHandler, '/api/urls/<string:url_name>')

# API Function to grab a god given god name from the db
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

# API Function to grab a god given god name from the db
class GodHandler(flask_restful.Resource):
  def get(self, god_name):
    god = God.query.filter_by(name=god_name)
    god = god.first()
    god_response = {}

    if god:
      god_response = {
        'name': god.name,
        'romanname': god.romanname,
        'power': god.power,
        'symbol': god.symbol,
        'father': god.father,
        'mother': god.mother,
      }

    return jsonify(god_response)
api.add_resource(GodHandler, '/api/gods/<string:god_name>')

# API Function to grab a all gods from the db
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

# API Function to grab a hero given hero name from the db
class HeroHandler(flask_restful.Resource):
  def get(self, hero_name):
    hero = Hero.query.filter_by(name=hero_name)
    hero = hero.first()
    hero_response = {}

    if hero:
      hero_response = {
        'name': hero.name,
        'herotype': hero.herotype,
        'power': hero.power,
        'father': hero.father,
        'mother': hero.mother,
        'home': hero.home,
      }

    return jsonify(hero_response)
api.add_resource(HeroHandler, '/api/heroes/<string:hero_name>')

# API Function to grab a all myths from the db
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

# API Function to grab a myth given myth name from the db
class MythHandler(flask_restful.Resource):
  def get(self, myth_name):
    myth = Myth.query.filter_by(name=myth_name)
    myth = myth.first()
    myth_response = {}

    if myth:
      myth_response = {
        'name': myth.name,
        'description': myth.description,
        'gods': myth.gods,
        'non-gods': myth.nongods,
        'place': myth.place,
        'theme': myth.theme,
      }

    return jsonify(myth_response)
api.add_resource(MythHandler, '/api/myths/<string:myth_name>')

# API Function to grab a all locations from the db
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

# API Function to grab a location given location name from the db
class LocationHandler(flask_restful.Resource):
  def get(self, location_name):
    location = Location.query.filter_by(name=location_name)
    location = location.first()
    location_response = {}

    if location:
      location_response = {
        'name': location.name,
        'alternate_name': location.altname,
        'myth': location.myth,
        'type': location.locationtype,
        'gods': location.gods,
      }

    return jsonify(location_response)
api.add_resource(LocationHandler, '/api/locations/<string:location_name>')


#Static pages
app.config['STATIC_ABOUT_PAGE'] = os.path.join('.', 'static', 'about.html')
app.config['STATIC_SPLASH_PAGE'] = os.path.join('.', 'static', 'index.html')
app.config['STATIC_VISUALIZATION_PAGE'] = os.path.join('.', 'static', 'visualization.html')

#Pillar pages
app.config['STATIC_GODS_FOLDER'] = os.path.join('.', 'static', 'gods')
app.config['STATIC_HEROES_FOLDER'] = os.path.join('.', 'static', 'heroes')
app.config['STATIC_LOCATIONS_FOLDER'] = os.path.join('.', 'static', 'locations')
app.config['STATIC_MYTHS_FOLDER'] = os.path.join('.', 'static', 'myths')

#List pages
app.config['STATIC_GODS_LIST'] = os.path.join('.', 'static', 'gods.html')
app.config['STATIC_HEROES_LIST'] = os.path.join('.', 'static', 'heroes.html')
app.config['STATIC_LOCATIONS_LIST'] = os.path.join('.', 'static', 'locations.html')
app.config['STATIC_MYTHS_LIST'] = os.path.join('.', 'static', 'myths.html')

#Static files
app.config['STATIC_CSS_FOLDER'] = os.path.join('.', 'static', 'css')
app.config['STATIC_FONTS_FOLDER'] = os.path.join('.', 'static', 'fonts')
app.config['STATIC_JS_FOLDER'] = os.path.join('.', 'static', 'js')
app.config['STATIC_IMAGES_FOLDER'] = os.path.join('.', 'static', 'img')

#Generate a tuple of queries (and query then or query)
#Parameters:
####searchterm: String with search terms seperated by spaces
####tablename: String with name of tablename
####columns: List of column names as strings
#Example:
# generateQuery("hera zeus", 'gods', ['name', 'romanname', 'power', 'symbol', 'father', 'mother'])
# returns a tuple of the searches ('hera AND zeus', 'hera OR zeus')

def generateQuery(searchterm, tablename, columns):
        terms = searchterm.split()

        columnstring = ' || \' \' || '.join(columns)

        first = True
        andQ = ''
        orQ = ''

        for term in terms:
            if re.match(r'\A[\w-]+\Z', term):
                if not first:
                    andQ += ' INTERSECT '
                    orQ += ' UNION '
                first = False
                andQ += 'SELECT * FROM ' + tablename +' WHERE to_tsvector(' + columnstring +') @@ to_tsquery(\'english\', \'' + term + '\')'
                orQ += 'SELECT * FROM ' + tablename +' WHERE to_tsvector(' + columnstring +') @@ to_tsquery(\'english\', \'' + term + '\')'

        return (andQ, orQ)

def boldSearchTerms(searchterm, inputstring):
    """
        Wraps all instances of searchterm in inputstring with bold HTML tags.
    """
    terms = searchterm.split()
    for term in terms:
        inputstring = re.sub(r'('+ term +')', r'<b>\1</b>', inputstring, flags=re.IGNORECASE)
    return inputstring


def error_wrapper(content):
    """
        Shows error message.
    """
    return render_template('error_template.html', error_message=content)

@app.route('/')
def index():
    """
        Shows the splash page.
    """
    if os.path.exists(app.config['STATIC_SPLASH_PAGE']):
        return send_file(app.config['STATIC_SPLASH_PAGE'])
    return error_wrapper('Hello, World! <SPLASH PAGE NOT YET ADDED>'), 404

@app.route('/about')
@app.route('/about/')
def about_page():
    """
        Connects to the about page.
    """
    if os.path.exists(app.config['STATIC_ABOUT_PAGE']):
        return send_file(app.config['STATIC_ABOUT_PAGE'])
    return error_wrapper('About page to be added'), 404


@app.route('/visualization')
@app.route('/visualization/')
def about_page():
    """
        Connects to the about page.
    """
    if os.path.exists(app.config['STATIC_VISUALIZATION_PAGE']):
        return send_file(app.config['STATIC_VISUALIZATION_PAGE'])
    return error_wrapper('About page to be added'), 404

@app.route('/gods')
@app.route('/gods/')
def gods_model():
    """
        Connects to the gods page.
    """
    if os.path.exists(app.config['STATIC_GODS_LIST']):
        return send_file(app.config['STATIC_GODS_LIST'])
    return error_wrapper('Gods Model page to be added'), 404

@app.route('/heroes')
@app.route('/heroes/')
def heroes_model():
    """
        Connects to the heroes page.
    """
    if os.path.exists(app.config['STATIC_HEROES_LIST']):
        return send_file(app.config['STATIC_HEROES_LIST'])
    return error_wrapper('Heroes Model page to be added'), 404

@app.route('/locations')
@app.route('/locations/')
def creatures_model():
    """
        Connects to creatures page
    """
    if os.path.exists(app.config['STATIC_LOCATIONS_LIST']):
        return send_file(app.config['STATIC_LOCATIONS_LIST'])
    return error_wrapper('Locations Model page to be added'), 404

@app.route('/myths')
@app.route('/myths/')
def myths_model():
    """
        Connects to myths page
    """
    if os.path.exists(app.config['STATIC_MYTHS_LIST']):
        return send_file(app.config['STATIC_MYTHS_LIST'])
    return error_wrapper('Myths Model page to be added'), 404

@app.route('/performtests')
def performtests():
    output = subprocess.Popen('python3 tests.py'.split(' '), stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
    output.wait()
    stuff, output = output.communicate()
    return jsonify(**{'result': str(output)})

@app.route('/donkey')
def do_this():
    return "Donkey"


@app.route('/search')
@app.route('/search/')
def search_model():
    q = request.args.get('query')
    q = str(q)
    if q != '':
        tablename = 'gods'
        columns = db.engine.execute('Select * from ' + tablename).keys()
        godsAndQuery, godsOrQuery = generateQuery(q, tablename, columns)

        tablename = 'heroes'
        columns = db.engine.execute('Select * from ' + tablename).keys()
        heroesAndQuery, heroesOrQuery = generateQuery(q, tablename, columns)

        tablename = 'myths'
        columns = db.engine.execute('Select * from ' + tablename).keys()
        mythsAndQuery, mythsOrQuery = generateQuery(q, tablename, columns)

        tablename = 'locations'
        columns = db.engine.execute('Select * from ' + tablename).keys()
        locationsAndQuery, locationsOrQuery = generateQuery(q, tablename, columns)

        godsAndResult = db.engine.execute(godsAndQuery)
        godsOrResult = db.engine.execute(godsOrQuery)
        heroesAndResult = db.engine.execute(heroesAndQuery)
        heroesOrResult = db.engine.execute(heroesOrQuery)
        mythsAndResult = db.engine.execute(mythsAndQuery)
        mythsOrResult = db.engine.execute(mythsOrQuery)
        locationsAndResult = db.engine.execute(locationsAndQuery)
        locationsOrResult = db.engine.execute(locationsOrQuery)

        god_and_result = []
        hero_and_result = []
        location_and_result = []
        myth_and_result = []
        god_or_result = []
        hero_or_result = []
        location_or_result = []
        myth_or_result = []


        for row in godsAndResult:
            obi = {}
            obi["name"] = boldSearchTerms(q,row["name"])
            obi["romanname"] = boldSearchTerms(q,row["romanname"])
            obi["symbol"] = boldSearchTerms(q,row["symbol"])
            obi["power"] = boldSearchTerms(q,row["power"])
            obi["father"] = boldSearchTerms(q,row["father"])
            obi["mother"] = boldSearchTerms(q,row["mother"])
            god_and_result.append(json.dumps(obi))

        for row in heroesAndResult:
            obi = {}
            obi["name"] = boldSearchTerms(q,row["name"])
            obi["herotype"] = boldSearchTerms(q,row["herotype"])
            obi["power"] = boldSearchTerms(q,row["power"])
            obi["home"] = boldSearchTerms(q,row["home"])
            obi["father"] = boldSearchTerms(q,row["father"])
            obi["mother"] = boldSearchTerms(q,row["mother"])
            hero_and_result.append(json.dumps(obi))

        for row in locationsAndResult:
            obi = {}
            obi["name"] = boldSearchTerms(q,row["name"])
            obi["altname"] = boldSearchTerms(q,row["altname"])
            obi["locationtype"] = boldSearchTerms(q,row["locationtype"])
            obi["myth"] = boldSearchTerms(q,row["myth"])
            obi["gods"] = boldSearchTerms(q,row["gods"])
            location_and_result.append(json.dumps(obi))

        for row in mythsAndResult:
            obi = {}
            obi["name"] = boldSearchTerms(q,row["name"])
            obi["description"] = boldSearchTerms(q,row["description"])
            obi["theme"] = boldSearchTerms(q,row["theme"])
            obi["place"] = boldSearchTerms(q,row["place"])
            obi["gods"] = boldSearchTerms(q,row["gods"])
            obi["nongods"] = boldSearchTerms(q,row["nongods"])
            myth_and_result.append(json.dumps(obi))

        for row in godsOrResult:
            obi = {}
            obi["name"] = boldSearchTerms(q,row["name"])
            obi["romanname"] = boldSearchTerms(q,row["romanname"])
            obi["symbol"] = boldSearchTerms(q,row["symbol"])
            obi["power"] = boldSearchTerms(q,row["power"])
            obi["father"] = boldSearchTerms(q,row["father"])
            obi["mother"] = boldSearchTerms(q,row["mother"])
            god_or_result.append(json.dumps(obi))

        for row in heroesOrResult:
            obi = {}
            obi["name"] = boldSearchTerms(q,row["name"])
            obi["herotype"] = boldSearchTerms(q,row["herotype"])
            obi["power"] = boldSearchTerms(q,row["power"])
            obi["home"] = boldSearchTerms(q,row["home"])
            obi["father"] = boldSearchTerms(q,row["father"])
            obi["mother"] = boldSearchTerms(q,row["mother"])
            hero_or_result.append(json.dumps(obi))

        for row in locationsOrResult:
            obi = {}
            obi["name"] = boldSearchTerms(q,row["name"])
            obi["altname"] = boldSearchTerms(q,row["altname"])
            obi["locationtype"] = boldSearchTerms(q,row["locationtype"])
            obi["myth"] = boldSearchTerms(q,row["myth"])
            obi["gods"] = boldSearchTerms(q,row["gods"])
            location_or_result.append(json.dumps(obi))

        for row in mythsOrResult:
            obi = {}
            obi["name"] = boldSearchTerms(q,row["name"])
            obi["description"] = boldSearchTerms(q,row["description"])
            obi["theme"] = boldSearchTerms(q,row["theme"])
            obi["place"] = boldSearchTerms(q,row["place"])
            obi["gods"] = boldSearchTerms(q,row["gods"])
            obi["nongods"] = boldSearchTerms(q,row["nongods"])
            myth_or_result.append(json.dumps(obi))

    # print(god_and_result)
    return render_template('searchtemp.html', godand = god_and_result, heroand = hero_and_result, locationand = location_and_result, mythand = myth_and_result, godor = god_or_result, heroor = hero_or_result, locationor = location_or_result, mythor = myth_or_result)

#using string instead of path because we don't want '/' to count
# @app.route('/gods/<string:god>')
# @app.route('/gods/<string:god>/')
# def god_page(god):
#     if os.path.exists(os.path.join(app.config['STATIC_GODS_FOLDER'], god.lower() + ".html")):
#         return send_from_directory(app.config['STATIC_GODS_FOLDER'],
#                                god.lower() + '.html', as_attachment=False)
#     return error_wrapper('Page for god: ' + god + ' to be added'), 404

@app.route('/gods/<string:god>')
@app.route('/gods/<string:god>/')
def god_page(god):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static/js', 'godsinfo.json')
    data = json.load(open(json_url))
    god_info = []
    for i in data:
        if i['name'].lower() == god:
            god_info.append(i['name'])
            god_info.append(i['romanname'])
            god_info.append(i['symbol'])
            god_info.append(i['power'])
            god_info.append(i['father'])
            god_info.append(i['mother'])
            god_info.append(i['url'])
    return render_template('godtemp.html', god = god_info)

# Links to specific hero given by hero name
# @app.route('/heroes/<string:hero>')
# @app.route('/heroes/<string:hero>/')
# def hero_page(hero):
#     if os.path.exists(os.path.join(app.config['STATIC_HEROES_FOLDER'], hero.lower() + ".html")):
#         return send_from_directory(app.config['STATIC_HEROES_FOLDER'],
#                                hero.lower() + '.html', as_attachment=False)
#     return error_wrapper('Page for hero: ' + hero + ' to be added'), 404

@app.route('/heroes/<string:hero>')
@app.route('/heroes/<string:hero>/')
def hero_page(hero):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static/js', 'heroesinfo.json')
    data = json.load(open(json_url))
    hero_info = []
    for i in data:
        if i['name'].lower() == hero:
            hero_info.append(i['name'])
            hero_info.append(i['herotype'])
            hero_info.append(i['power'])
            hero_info.append(i['home'])
            hero_info.append(i['father'])
            hero_info.append(i['mother'])
            hero_info.append(i['url'])
    return render_template('herotemp.html', hero = hero_info)

# Links to specific creature given by creature name
# @app.route('/locations/<string:location>')
# @app.route('/locations/<string:location>/')
# def creature_page(location):
#     if os.path.exists(os.path.join(app.config['STATIC_LOCATIONS_FOLDER'], location.lower() + ".html")):
#         return send_from_directory(app.config['STATIC_LOCATIONS_FOLDER'],
#                                location.lower() + '.html', as_attachment=False)
#     return error_wrapper('Page for creature: ' + location + ' to be added'), 404

@app.route('/locations/<string:location>')
@app.route('/locations/<string:location>/')
def location_page(location):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static/js', 'locationsinfo.json')
    data = json.load(open(json_url))
    location_info = []
    for i in data:
        if i['name'].lower() == location:
            location_info.append(i['name'])
            location_info.append(i['altname'])
            location_info.append(i['locationtype'])
            location_info.append(i['myth'])
            location_info.append(i['gods'])
            location_info.append(i['url'])
    return render_template('locationtemp.html', location = location_info)

# Links to specific myth given by myth name
# @app.route('/myths/<string:myth>')
# @app.route('/myths/<string:myth>/')
# def myth_page(myth):
#     if os.path.exists(os.path.join(app.config['STATIC_MYTHS_FOLDER'], myth.lower() + ".html")):
#         return send_from_directory(app.config['STATIC_MYTHS_FOLDER'],
#                                myth.lower() + '.html', as_attachment=False)
#     return error_wrapper('Page for myth: ' + myth + ' to be added'), 404

@app.route('/myths/<string:myth>')
@app.route('/myths/<string:myth>/')
def myth_page(myth):
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, 'static/js', 'mythsinfo.json')
    data = json.load(open(json_url))
    myth_info = []
    for i in data:
        if i['name'].lower() == myth:
            myth_info.append(i['name'])
            myth_info.append(i['description'])
            myth_info.append(i['theme'])
            myth_info.append(i['place'])
            myth_info.append(i['gods'])
            myth_info.append(i['nongods'])
            myth_info.append(i['url'])
    return render_template('mythtemp.html', myth = myth_info)

@app.route('/static/<path:folder>/<string:file>')
def static_files(folder, file):
    """ Serves the static files that will be used through all iterations of the project
    """
    if folder == 'css':
        return send_from_directory(app.config['STATIC_CSS_FOLDER'],
                               file.lower(), as_attachment=False)
    elif folder == 'fonts':
        return send_from_directory(app.config['STATIC_FONTS_FOLDER'],
                               file.lower(), as_attachment=False)
    elif folder == 'js':
        return send_from_directory(app.config['STATIC_JS_FOLDER'],
                               file.lower(), as_attachment=False)
    elif folder == 'img':
        return send_from_directory(app.config['STATIC_IMAGES_FOLDER'],
                               file.lower(), as_attachment=False)
    elif folder == 'img/about':
        return send_from_directory(os.path.join(app.config['STATIC_IMAGES_FOLDER'], 'about'),
                               file.lower(), as_attachment=False)
    else:
        abort(code = 404)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
