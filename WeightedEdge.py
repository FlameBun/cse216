class WeightedEdge:
    def __init__(self, initNode1, initNode2, initWeight):
        self.node1 = initNode1
        self.node2 = initNode2
        self.weight = initWeight

    def getNode1(self):
        return self.node1
    
    def getNode2(self):
        return self.node2
    
    def getWeight(self):
        return self.weight