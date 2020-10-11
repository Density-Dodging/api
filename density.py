from ddUtils import *
TAG = "density.py"

def assignDensityPerBuilding(buildings, densityData):
    pendingBuildings = buildings
    for key in buildings:
        people = []
        for i in range(buildings[key]['floors']):
            people.append(0)
        buildings[key]['people'] = people
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
                            for floor in buildings[buildingId]['people']:
                                buildings[buildingId]['people'][floor] += 1
                            log(TAG, "Found entry in building: " + building['id'])
                            break

    return pendingBuildings