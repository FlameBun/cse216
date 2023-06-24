from pyTPS_Transaction import pyTPS_Transaction

class AddToStop_Transaction(pyTPS_Transaction):
    def __init__(self, initStops, initStopToAdd):
        self.stops = initStops
        self.stopToAdd = initStopToAdd

    def doTransaction(self):
        self.stops.append(self.stopToAdd)

    def undoTransaction(self):
        self.stops.pop(len(self.stops) - 1)

    def __str__(self):
        return self.stopToAdd
