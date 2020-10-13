import json
with open('config.json') as config_file:
    config = json.load(config_file)

class Config:
    def get(property):
        return config[property]

class CampusNode:
    def __init__(self, id, latitude, longitude):
        self.id = id
        self.latitude = latitude
        self.longitude = longitude
        self.neighbors = []


def log(tag, message):
    if (Config.get("environment") == "dev"):
        print(f"[{tag}] {message}")

def buildingsDictToData(buildingsDict):
    buildingsArr = []
    for building in buildingsDict.items():
        totalInBuilding = 0
        for floor in building[1]['people']:
            totalInBuilding += floor
        buildingEach = {
            "id": building[1]['id'],
            "buildingName": building[1]['buildingName'],
            "latitude": building[1]['latitude'],
            "longitude": building[1]['longitude'],
            "floors": building[1]['floors'],
            "people": building[1]['people'],
            "densityLevel": building[1]['densityLevel'],
            "type": building[1]['type'],
            "url": building[1]['url']
        }
        buildingsArr.append(buildingEach)
    
    return buildingsArr
