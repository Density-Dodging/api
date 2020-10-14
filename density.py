from ddUtils import *
TAG = "density.py"

randomIndex = 24
randoms = [75, 7, 70, 40, 45, 43, 68, 99, 29, 59, 21, 46, 5, 47, 92, 86, 88, 42, 37, 78, 33, 55, 1, 30, 53]
def getRandom():
    randomIndex += 1
    if (randomIndex >= len(randomIndex) - 1):
        randomIndex = 0
    return randsoms[randomIndex]

def assignDensityPerBuilding(buildings, densityData):
    pendingBuildings = buildings
    for key in buildings:
        people = []
        for i in range(buildings[key]['floors']):
            people.append(getRandom())
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
                            break

    return pendingBuildings