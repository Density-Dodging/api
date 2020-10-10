from ddUtils import *
from database import initDB, closeDB, getBuildings, getDensity
from density import *
from flask import Flask
from flask import jsonify

app = Flask(__name__)
TAG = "start.py"

log(TAG, "Starting API")
db = initDB()
buildings = getBuildings(db)
densityData = getDensity(db)
closeDB(db)
buildings = assignDensityPerBuilding(buildings, densityData)

@app.route('/api/buildings/all')
def serveBuildings():
    return jsonify(buildings)

@app.route('/api/buildings/<id>')
def serveBuilding(id):
    return jsonify(buildings[id])