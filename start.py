from ddUtils import *
from database import initDB, closeDB, getBuildings, getDensity, addDensityEntry
from density import *
from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)
TAG = "start.py"

log(TAG, "Starting API")
db = initDB()
buildings = getBuildings(db)
densityData = getDensity(db)
buildings = assignDensityPerBuilding(buildings, densityData)

@app.route('/api/buildings/all')
def serveBuildings():
    return jsonify(buildingsDictToData(buildings))

@app.route('/api/buildings/<id>')
def serveBuilding(id):
    return jsonify(buildings[id])

@app.route('/api/density/add')
def addDensity():
    latitude = (request.args.get('latitude'))
    longitude = (request.args.get('longitude'))
    addDensityEntry(db, latitude, longitude)
    return '200 OK', 200

@app.route('/api/navigation/route')
def findRoute():
    return jsonify([(42.273347, -71.809901), (42.273824, -71.809794), (42.274133, -71.809162), (42.273991, -71.808561), (42.274554, -71.808454), (42.274499, -71.807757), (42.275324, -71.807618), (42.275562,-71.807834)])