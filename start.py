from ddUtils import *
from database import initDB, closeDB, getBuildings, getDensity
from density import *
from flask import Flask
from flask import jsonify
from flask import request
import atexit

app = Flask(__name__)
TAG = "start.py"

log(TAG, "Starting API")
db = initDB()
atexit.register(closeDB(db))
buildings = getBuildings(db)
densityData = getDensity(db)
buildings = assignDensityPerBuilding(buildings, densityData)

@app.route('/api/buildings/all')
def serveBuildings():
    return jsonify(buildings)

@app.route('/api/buildings/<id>')
def serveBuilding(id):
    return jsonify(buildings[id])

@app.route('/api/density/add')
def addDensity():
    latitude = request.args.get['latitude']
    longitude = request.args.get['longitude']
    addDensityEntry(db, latitude, longitude)