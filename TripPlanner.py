from Airport import Airport
from pyTPS import pyTPS
from WeightedGraph import WeightedGraph
from AddToStop_Transaction import AddToStop_Transaction
import json

tps = pyTPS()
airportGraph = WeightedGraph()
stops = []

def initAllAirports():
    data = json.load(open("flights.json"))
    
    airports = data["airports"]
    for i in range(0, len(airports)):
        code = airports[i]["code"]
        latDeg = airports[i]["latitudeDegrees"]
        latMin = airports[i]["latitudeMinutes"]
        longDeg = airports[i]["longitudeDegrees"]
        longMin = airports[i]["longitudeMinutes"]
        airportGraph.addNode(code, Airport(code, latDeg, latMin, longDeg, longMin))

    edges = data["edges"]
    for i in range(0, len(edges)):
        node1 = edges[i]["node1"]
        node2 = edges[i]["node2"]
        a1 = airportGraph.getNodeData(node1)
        a2 = airportGraph.getNodeData(node2)
        distance = Airport.calculateDistance(a1, a2)
        airportGraph.addEdge(node1, node2, distance)
        airportGraph.addEdge(node2, node1, distance)

initAllAirports()