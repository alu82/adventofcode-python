import math

class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.nodes = set()
        for edge in self.edges:
            self.nodes.add(edge[0])
            self.nodes.add(edge[1])
        self.edges = edges

    # return all edges where the given node is in fist position (source node)
    def getEdgesForNode(self, node):
        return dict(filter(lambda item: item[0][0] == node, self.edges.items()))
    
    def makeBiDirectional(self):
        inverseEdges = {}
        for edge in self.edges:
            inverseEdge = (edge[1], edge[0])
            inverseEdges[inverseEdge] = self.edges[edge]
        
        for inverseEdge in inverseEdges:
            self.edges[inverseEdge] =  inverseEdges[inverseEdge]

class Dijkstra:

    def __init__(self, graph):
        self.graph = graph
        self.reset()

    def reset(self):
        self.distance = {}
        self.pred = {}
        self.done = {}

        for node in self.graph.nodes:
            self.distance[node] = math.inf
            self.pred[node] = None
    
    def shortest(self, start, end):
        self.reset()
        self.init(start)

        currentNode = start
        while currentNode != end:
            self.updateDistances(currentNode)
            
            if len(self.distance) > 0: # if len == 0, the end is not reachable
                currentNode = min(self.distance, key=self.distance.get)
            else:
                break

    def shortestDistance(self, start, end):
        self.shortest(start, end)
        return self.distance[end]

    def shortestPath(self, start, end):
        self.shortest(start, end)
        path = [end]

        last = end
        while last in self.pred and self.pred[last] is not None:
            path.append(self.pred[last])
            last = self.pred[last]
        
        path.reverse()
        return path

    def init(self, start):
        self.distance[start] = 0
            
    def updateDistances(self, node):
        distance = self.distance.pop(node)
        self.done[node] = distance

        # update distance for all neighor nodes that have still have not been fixed (moved to done)
        for edge in self.graph.getEdgesForNode(node):
            neighborNode = edge[1]
            potentialDistance = distance + self.graph.edges[edge]
            if neighborNode in self.distance and potentialDistance < self.distance[neighborNode]:
                self.distance[neighborNode] = potentialDistance
                self.pred[neighborNode] = node
                
    def print(self):
        print("Distance", self.distance)
        print("Done", self.done)
        print("Pred", self.pred)


# Test
#edges = {
#    ('Frankfurt', 'Mannheim'): 85,
#    ('Frankfurt', 'Würzburg'): 217,
#    ('Frankfurt', 'Kassel'): 173,
#    ('Mannheim', 'Karlsruhe'): 80,
#    ('Würzburg', 'Erfurt'): 186,
#    ('Würzburg', 'Nürnberg'): 103,
#    ('Stuttgart', 'Nürnberg'): 183,
#    ('Karlsruhe', 'Augsburg'): 250,
#    ('Augsburg', 'München'): 84,
#    ('Nürnberg', 'München'): 167,
#    ('Kassel', 'München'): 502,
#    ('T', 'München2'): 502,
#}
#
#graph = Graph(edges)
#graph.makeBiDirectional()
#dijkstra = Dijkstra(graph)
#if dijkstra.shortestDistance("Frankfurt", "München") != 487:
#    print("error")
    