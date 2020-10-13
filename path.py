from database import getPathNodes, getEdges
from ddUtils import *

TAG = "path.py"

pathNodes = []
buildingNodes = []
edges = []
allRawNodes = []
allNodes = []

def initializePathfinding(db, buildingNodesDict):
    log(TAG, "Initializing pathfinding data")
    pathNodes = getPathNodes(db)
    edges = getEdges(db)
    for key in buildingNodesDict:
        selectedBuilding = buildingNodesDict[key]
        thisBuilding = {
            "id" : selectedBuilding['id'],
            "latitude" : selectedBuilding['latitude'],
            "longitude" : selectedBuilding['longitude']
        }
        buildingNodes.append(thisBuilding)

    allRawNodes = pathNodes + buildingNodes

    for node in allRawNodes:
        campusNode = CampusNode(node['id'], node['latitude'], node['longitude'])
        allNodes.append(campusNode)

