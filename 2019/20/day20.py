import os
from string import ascii_uppercase as UPPER
import math
from operator import add

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)
DIRECTIONS = [UP, RIGHT, DOWN, LEFT]

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
            portalTiles = portals.get(portalName, [])
            portalTiles.append(passageTile)
            portals[portalName] = portalTiles
    return portals

def getNextNodes(maze, position, nodes, portals):
    mazeCopy = maze.copy()
    nextNodes = set()
    distance = 0
    starts = set([position])

    while len(starts) > 0:
        distance += 1
        starts = nextStep(mazeCopy, starts, portals)
        tmpStarts = set()
        for start in starts:
            if start in nodes:
                nextNodes.add((start, distance))
                tmpStarts.add(start)
        starts = starts - tmpStarts
    return nextNodes

def nextStep(maze, starts, portals):
    newStarts = set([])
    for start in starts:
        adjacents = getNeighbors(start)
        if start in portals:
            adjacents.append(portals[start])
        maze.pop(start, None)
        for adjacent in adjacents:
            if adjacent in maze and maze[adjacent] == PASSAGE:
                newStarts.add(adjacent)
    return newStarts

def djikstra(nodes, maze, portals, start, end):
    print(nodes)
    distance = {}
    pred = {}
    done = {}
    for node in nodes:
        distance[node] = math.inf
        pred[node] = None
    
    
    done[start] = 0
    
    currentNode = start

    nextNodes = getNextNodes(maze, currentNode, nodes, portals)
    for nextNode in nextNodes:
        distance[nextNode[0]] = nextNode[1]
        pred[nextNode[0]] = nextNode[1]

    while len(distance.keys()) > 0:
        print(distance)
        nearest = min(distance, key=distance.get)
        print(currentNode, nearest)
        print("----------------------")
        done[nearest] = distance.pop(nearest)
        currentNode = nearest

        nextNodes = getNextNodes(maze, currentNode, nodes, portals)
        baseDistance = done[nearest]
        for nodeItem in nextNodes:
            newDistance = baseDistance + nodeItem[1]
            currentDistance = distance[nextNode[0]]
            if newDistance < currentDistance:
                distance[nodeItem[0]] = newDistance
                pred[nodeItem[0]] = currentNode



# Open input files and get intcodeprogram
script_dir = os.path.dirname(__file__)
inputFile = open(script_dir + "/input", "r")

maze = getMaze(inputFile)
portals = getPortals(maze)

tmpPortals = {}
for portal in portals.values():
    if len(portal) > 1:
        tmpPortals[portal[0]] = portal[1]
        tmpPortals[portal[1]] = portal[0]

allPortalNodes = []
for portalNodes in portals.values():
    allPortalNodes = allPortalNodes + portalNodes

djikstra(allPortalNodes, maze, tmpPortals, portals['AA'][0], portals['ZZ'][0])

