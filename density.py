from ddUtils import *
TAG = "density.py"

def assignDensityPerBuilding(buildings, densityData):
    pendingBuildings = buildings
    for key in buildings:
        buildings[key]['people'] = 0
    for entry in densityData:
        for key in buildings:
            building = buildings[key]
            latitude = entry['latitude']
            latitudeMin = building['latitudeMin']
            latitudeMax = building['latitudeMax']
            longitude = entry['longitude']
            longitudeMin = building['longitudeMin']
            longitudeMax = building['longitudeMax']

            if (latitude > latitudeMin):
                if (latitude < latitudeMax):
                    if (longitude > longitudeMin):
                        if (longitude < longitudeMax):
                            buildingId = building['id']
                            buildings[buildingId]['people'] += 1
                            log(TAG, "Found entry in building: " + building['id'])
                            break

    return pendingBuildings