import os

def getMapEntries(map):
    mapEdges = []
    mapNodes = set()
    for mapEntry in map:
        nodes = mapEntry.split(')')
        node1 = nodes[0].strip()
        node2 = nodes[1].strip()
        mapNodes.add(node1)
        mapNodes.add(node2)
        mapEdges.append((node1, node2))
    return (mapNodes, mapEdges)

def calcOrbits(node, edges):
    for edge in edges:
        if edge[1] == node:
            return [edge] + calcOrbits(edge[0], edges)
    return []


script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

mapEntries = getMapEntries(inputFile)

nodes = mapEntries[0]
edges = mapEntries[1] 

# part 1
totalOrbits = 0
for node in nodes:
    t = calcOrbits(node, edges)
    totalOrbits += len(calcOrbits(node, edges))
print(totalOrbits)

# part 2
myOrbits = calcOrbits('YOU', edges)
santasOrbits = calcOrbits('SAN', edges)

totalOrbits = len(myOrbits) + len(santasOrbits)
uniqueOrbits = len(set(myOrbits + santasOrbits))

# we substract the common orbits for both (you and san) from the total orbits
# then we have to substract another 2 (1 for you, 1 for san) because the length of the orbits is 1 longer than the transfers needed
orbitTransfers = totalOrbits - (totalOrbits-uniqueOrbits)*2 - 2
print(orbitTransfers)
