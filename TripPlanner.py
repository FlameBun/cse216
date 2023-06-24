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
    
    # Initializing Nodes
    airports = data["airports"]
    for i in range(0, len(airports)):
        code = airports[i]["code"]
        latDeg = airports[i]["latitudeDegrees"]
        latMin = airports[i]["latitudeMinutes"]
        longDeg = airports[i]["longitudeDegrees"]
        longMin = airports[i]["longitudeMinutes"]
        airportGraph.addNode(code, Airport(code, latDeg, latMin, longDeg, longMin))

    # Initializing Edges
    edges = data["edges"]
    for i in range(0, len(edges)):
        node1 = edges[i]["node1"]
        node2 = edges[i]["node2"]
        a1 = airportGraph.getNodeData(node1)
        a2 = airportGraph.getNodeData(node2)
        distance = Airport.calculateDistance(a1, a2)
        airportGraph.addEdge(node1, node2, distance)
        airportGraph.addEdge(node2, node1, distance)

def displayAirports():
    # Display Airports
    print("\nAIRPORTS YOU CAN TRAVEL TO AND FROM:")
    codes = airportGraph.getNodes()
    for i in range(0, len(codes)):
        if i % 10 == 0:
            print("\t", end = "")
        print(codes[i], end = "")
        if i < len(codes) - 1:
            print(", ", end = "")
        if i % 10 == 9:
            print()
    print("\n")

def displayCurrentTrip():
    # Display Trip Stops
    print("Trip Stops:")
    for i in range(0, len(stops)):
        print("\t" + str(i + 1) + ". " + stops[i])
    print()

    # Display Trip Legs
    totalDistance = 0
    tripLegs = ""
    print("Trip Legs:")
    for i in range(0, len(stops) - 1):
        tripLegs += "\t" + str(i + 1) + ". "

        path = airportGraph.findPath(stops[i], stops[i + 1])

        legDistance = 0
        for j in range(0, len(path) - 1):
            if j == len(path) - 2:
                tripLegs += path[j] + "-" + path[j + 1] + " "
            else:
                tripLegs += path[j] + "-"

            a1 = airportGraph.getNodeData(path[j])
            a2 = airportGraph.getNodeData(path[j + 1])
            legDistance += Airport.calculateDistance(a1, a2)

        tripLegs += "(" + str(legDistance) + " Miles)" + "\n"
        totalDistance += legDistance
    print(tripLegs)

    # Display Total Trip Distance
    print("Total Trip Distance: " + str(totalDistance) + " Miles\n")

def displayMenu():
    # Display Menu
    print("ENTER A SELECTION")
    print("S) Add a Stop to your Trip")
    print("U) Undo")
    print("R) Redo")
    print("E) Empty Trip")
    print("Q) Quit")
    print("-")

def processUserInput():
    global stops
    
    # Get User Selection
    entry = input("")

    if entry == "S":
        entry = input("Enter airport stop: ")
        print()

        # Edge Cases
        if not airportGraph.nodeExists(entry):
            print("Error. Invalid airport stop.\n")
            return True
        if len(stops) != 0:
            path = airportGraph.findPath(stops[len(stops) - 1], entry)
            if len(path) == 0:
                print("Error. Path does not exist from " + stops[len(stops) - 1] + " to " + entry + ".\n")
                return True
            elif len(path) == 1:
                print("Error. Same as last stop.\n")
                return True
        
        # Add Stop Transaction
        transaction = AddToStop_Transaction(stops, entry)
        tps.addTransaction(transaction)

    elif entry == "U":
        tps.undoTransaction()
    elif entry == "R":
        tps.doTransaction()
    elif entry == "E":
        tps.clearAllTransactions()
        stops = []
    elif entry == "Q":
        return False
    return True

# Main Program
initAllAirports()
keepGoing = True
while keepGoing:
    displayAirports()
    displayCurrentTrip()
    displayMenu()
    keepGoing = processUserInput()
print("\nGOODBYE")
