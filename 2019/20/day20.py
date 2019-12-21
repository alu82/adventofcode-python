import os
from string import ascii_uppercase as UPPER
import math
from operator import add
from Dijkstra import Dijkstra, Graph

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

OUTER = '_OUTER'
INNER = '_INNER'

PASSAGE = '.'
WALL = '#'

def getNeighbors(position):
    adjacents = []
    for direction in DIRECTIONS:
        adjacents.append(tuple(map(add, position, direction)))
    return adjacents

def getPassageTile(maze, neighbors):
    for neighbor in neighbors:
        tile = maze.get(neighbor, WALL)
        if tile == PASSAGE:
            return neighbor
    return None

def getLetterTile(maze, neighbors):
    for neighbor in neighbors:
        tile = maze.get(neighbor, WALL)
        if tile in UPPER:
            return neighbor
    return None

def getMaze(input):
    maze = {}
    col = 0
    row = 0

    for line in input:
        for char in line:
            maze[(col, row)] = char
            col += 1
        row += 1
        col = 0
    return maze

def getPortalName(maze, pos, name):
    if name == 'AA' or name == 'ZZ':
        return name

    maxRow = max(maze.keys(), key=lambda maze:maze[1])[1]
    maxCol = max(maze.keys(), key=lambda maze:maze[0])[0]

    posCol = pos[0]
    posRow = pos[1]

    isOuter = (posCol < 2 or posRow < 2) or (maxCol - posCol < 3 or maxRow - posRow < 3)
    if isOuter:
        name += OUTER
    else:
        name += INNER

    return name
    
    

def getPortals(maze):
    letters = dict(filter(lambda item: item[1] in UPPER, maze.items()))
    portals = {}
    for pos, letter in letters.items():
        neighbors = getNeighbors(pos)
        passageTile = getPassageTile(maze, neighbors)
        letterTile = getLetterTile(maze, neighbors)
        if passageTile is not None and letterTile is not None:
            diff = letterTile[0] - pos[0] + letterTile[1] - pos[1]
            if diff < 0:
                portalName = maze[letterTile] + letter
            else:
                portalName = letter + maze[letterTile]

            portalName = getPortalName(maze, pos, portalName)
            portals[portalName] = passageTile
    return portals

def getNextNodes(maze, position, nodes):
    mazeCopy = maze.copy()
    nextNodes = set()
    distance = 0
    starts = set([position])

    while len(starts) > 0:
        distance += 1
        starts = nextStep(mazeCopy, starts)
        tmpStarts = set()
        for start in starts:
            if start in nodes:
                nextNodes.add((start, distance))
                tmpStarts.add(start)
        starts = starts - tmpStarts
    return nextNodes

def nextStep(maze, starts):
    newStarts = set([])
    for start in starts:
        adjacents = getNeighbors(start)
        maze.pop(start, None)
        for adjacent in adjacents:
            if adjacent in maze and maze[adjacent] == PASSAGE:
                newStarts.add(adjacent)
    return newStarts

def isStartOrEndEdge(edge):
    isStartEdge = isStart(edge[0]) or isStart(edge[1])
    isEndEdge = isEnd(edge[0]) or isEnd(edge[1])
    return isStartEdge or isEndEdge

def isStart(node):
    return node == 'AA'

def isEnd(node):
    return node == 'ZZ'

def isOuter(node):
    return OUTER in node

def isInner(node):
    return INNER in node

def part1(edges, portals):

    # add the portals to the edges
    for portal in portals.keys():
        if portal[-len(OUTER):] == OUTER:
            otherPortal = portal.replace(OUTER, INNER)
            edge1 = (portal, otherPortal)
            edge2 = (otherPortal, portal)
            edges[edge1] = 1
            edges[edge2] = 1

    graph = Graph(edges)
    dijkstra = Dijkstra(graph)
    print(dijkstra.shortestDistance('AA', 'ZZ'))
    #print(dijkstra.shortestPath('AA', 'ZZ'))

def part2(edges, portals):
    maxLevel = 60
    recursiveEdges = {}
    for level in range(maxLevel):
        levelSuffix = '_' + str(level)
        levelUpSuffix = '_' + str(level-1)
        levelDownSuffix = '_' + str(level+1)
        
        for edge in edges:
            if level == 0 and isStartOrEndEdge(edge):
                if isStart(edge[0]) or isEnd(edge[0]):
                    levelEdgeCol = edge[0]
                else:
                    levelEdgeCol = edge[0] + levelSuffix
                if isStart(edge[1]) or isEnd(edge[1]):
                    levelEdgeRow = edge[1]
                else:
                    levelEdgeRow = edge[1] + levelSuffix
                
                levelEdge = (levelEdgeCol, levelEdgeRow)
                recursiveEdges[levelEdge] = edges[edge]
                
            if not isStartOrEndEdge(edge):
                levelEdge = (edge[0] + levelSuffix, edge[1] + levelSuffix)
                recursiveEdges[levelEdge] = edges[edge]

        for portal in portals.keys():
            if isInner(portal): # go down a level
                levelEdgeCol = portal + levelSuffix
                levelEdgeRow = portal.replace(INNER, OUTER) + levelDownSuffix
            elif isOuter(portal) and level > 0: # go up a level
                levelEdgeCol = portal + levelSuffix
                levelEdgeRow = portal.replace(OUTER, INNER) + levelUpSuffix
            else: # start or end portal
                continue
            
            portalEdge = (levelEdgeCol, levelEdgeRow)
            recursiveEdges[portalEdge] = 1

    graph = Graph(recursiveEdges)
    dijkstra = Dijkstra(graph)
    print(dijkstra.shortestDistance('AA', 'ZZ'))
    #print(dijkstra.shortestPath('AA', 'ZZ'))


# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

maze = getMaze(inputFile)
portals = getPortals(maze)

edges = {}
for portal in portals:
    nextNodes = getNextNodes(maze, portals[portal], list(portals.values()))
    for nextNode in nextNodes:
        nextPortal = list(filter(lambda node: portals[node] == nextNode[0], portals))[0]
        edge = (portal, nextPortal)
        distance = nextNode[1]
        edges[edge] = distance

part1(edges.copy(), portals.copy())
part2(edges.copy(), portals.copy())

