from WeightedEdge import WeightedEdge

class WeightedGraph:
    def __init__(self):
        self.nodes = {}
        self.edges = {}
    
    def getNodes(self):
        return self.nodes.keys()
    
    def getEdges(self):
        return self.edges.keys()
    
    def addNode(self, nodeId, data):
        self.nodes[nodeId] = data

    def getNodeData(self, nodeId):
        return self.nodes[nodeId]
    
    def getEdgeId(self, node1, node2):
        return node1 + "-" + node2
    
    def addEdge(self, node1, node2, weight):
        edgeId = self.getEdgeId(node1, node2)
        self.edges[edgeId] = WeightedEdge(node1, node2, weight)

    def getNeighbors(self, node):
        neighbors = []
        edges = self.getEdges()
        temp = node + "-"

        for i in range(0, len(edges)):
            if temp in edges[i]:
                neighbors.append(edges[i][4:])
        
        return neighbors
    
    def nodeExists(self, nodeId):
        return nodeId in self.getNodes()
    
    def findPath(self, node1, node2):
        visitedNodes = {}
        nodes = self.getNodes()
        for i in range(0, len(nodes)):
            visitedNodes[nodes[i]] = False

        pathQueue = []
        startPath = []
        startPath.append(node1)
        visitedNodes[node1] = True
        pathQueue.append(startPath)

        while True:
            if len(pathQueue) == 0:
                break

            tempPath = pathQueue.pop(0)
            lastNode = tempPath[len(tempPath) - 1]
            if lastNode == node2:
                return tempPath
            
            neighbors = self.getNeighbors(lastNode)
            for i in range(0, len(neighbors)):
                if visitedNodes[neighbors[i]] == False:
                    tempPath.append(neighbors[i])
                    pathQueue.append(tempPath.copy())
                    tempPath.pop()
                    visitedNodes[neighbors[i]] = True

        return []
